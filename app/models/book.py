from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base 

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    published_year = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey('authors.id', ondelete='RESTRICT'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='RESTRICT'), nullable=False)

    cover_image = Column(String(255), nullable=True)  
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    author = relationship('Author', back_populates='books')
    category = relationship('Category', back_populates='books')