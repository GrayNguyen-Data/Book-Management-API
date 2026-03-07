from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    connect_args = {
        "check_same_thread": False
    } if settings.SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}
)

'''
- autocommit = false: không tự động lưu thay đổi vào database, cần gọi commit để lưu
- autoflush = false: không tự động đẩy query vào database
- bind = engine: kết nối session với engine đã tạo
'''
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine) 
