from fastapi import APIRouter, HTTPException
from app.database import product_collection
from app.schemas.product import ProductCreate
from bson import ObjectId

router = APIRouter(prefix="/products", tags=["Products"])

def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product.get("description"),
        "price": product["price"],
        "in_stock": product["in_stock"],
    }

@router.post("/")
async def create_product(product: ProductCreate):
    new_product = await product_collection.insert_one(product.dict())
    created = await product_collection.find_one({"_id": new_product.inserted_id})
    return product_helper(created)

@router.get("/")
async def get_products():
    products = []
    async for product in product_collection.find():
        products.append(product_helper(product))
    return products
