from fastapi import APIRouter

from api.services.product_service import (
    get_top_products,
    get_product
)

router = APIRouter()


@router.get("/top-products")
def top_products():

    return get_top_products().to_dict(
        orient="records"
    )


@router.get("/products/{product_id}")
def product(product_id: int):

    return get_product(
        product_id
    ).to_dict(
        orient="records"
    )
