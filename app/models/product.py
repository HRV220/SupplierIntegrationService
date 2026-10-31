from datetime import datetime
from decimal import Decimal
from sqlalchemy import Numeric, String, Integer, VARCHAR, CheckConstraint, UniqueConstraint, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.supplier import Supplier

class Product(Base):
  __tablename__ = "products"

  id: Mapped[int] = mapped_column(primary_key=True)
  supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"), nullable=False)
  external_id: Mapped[str] = mapped_column(String, nullable=False)
  name: Mapped[str] = mapped_column(String, nullable=False)
  price: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
  currency: Mapped[str] = mapped_column(VARCHAR(3), nullable=False)
  stock: Mapped[int] = mapped_column(Integer, nullable=False)
  updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
  supplier: Mapped["Supplier"] = relationship(back_populates="products")
  __table_args__ = (
    CheckConstraint("stock >= 0", name="ck_stock_positive"),
    UniqueConstraint("supplier_id", "external_id", name="uq_supplier_id_external_id")
  )