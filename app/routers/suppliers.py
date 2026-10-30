from fastapi import APIRouter, HTTPException, status
from app.schemas.suppliers import SupplierRead


router = APIRouter(
    prefix="/suppliers",
    tags=["suppliers"],
)

# Временное хранилище учебного этапа.
suppliers: list[dict[str, int | str]] = [
    {"id": 1, "name": "Alex"},
    {"id": 2, "name": "Bob"},
]


@router.get(
    "",
    summary="Получить список поставщиков",
    response_model= list[SupplierRead]
)
def list_suppliers() -> list[dict[str, int | str]]:
    return suppliers


@router.get(
    "/{supplier_id}",
    summary="Получить поставщика по ID",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Поставщик не найден",
        },
    },
    response_model=SupplierRead
)
def get_supplier(supplier_id: int) -> dict[str, int | str]:
    for supplier in suppliers:
        if supplier["id"] == supplier_id:
            return supplier

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Supplier not found.",
    )
