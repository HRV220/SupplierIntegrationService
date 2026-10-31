from app.db.base import Base
from sqlalchemy import String, Text, DateTime, func, true
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Supplier(Base):
  __tablename__ = 'suppliers'

  id:Mapped[int] = mapped_column(primary_key=True)
  name:Mapped[str] = mapped_column(String(255))
  base_url:Mapped[str] = mapped_column(Text)
  is_active:Mapped[bool] = mapped_column(server_default=true())
  created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default = func.now())