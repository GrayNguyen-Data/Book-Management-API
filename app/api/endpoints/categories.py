from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.api.deps import get_db 

from app import models
from app.schemas.category import CategoryCreate, Category, CategoryUpdate


router = APIRouter()

@router.get('/', response_model=List[Category])
def list_categories(skip: int = 0,
                    limit:int = 100,
                    db: Session = Depends(get_db)):
    categories  = db.query(models.Category).offset(skip).limit(limit).all()
    return categories

@router.get("/{category_id}", response_model=Category)
def get_category(category_id:int, db: Session = Depends(get_db)):
    categories = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not categories:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    
    return categories

@router.post('/', response_model = Category, status_code = status.HTTP_201_CREATED)
def create_category(category_in: CategoryCreate,
                    db: Session = Depends(get_db)):
    existing = db.query(models.Category).filter(models.Category.name == category_in.name).first()

    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category already exists")

    category = models.Category(name=category_in.name, description=category_in.description)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category