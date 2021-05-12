from dto.vo.productVo import ProductVo
from fastapi import FastAPI
from dto.vo.productVo import ProductVo
from services.productService import ProductService

app = FastAPI()

@app.post("/product")
async def createProduct(product: ProductVo):
    return ProductService.createProduct(product)
