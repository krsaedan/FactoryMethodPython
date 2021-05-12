import uuid
from fastapi.encoders import jsonable_encoder
from dto.vo.productVo import ProductVo
from daoFactory.productDao import ProductDao
from bd.cosmos import container

class ProductCosmosDaoImp(ProductDao):
    def createProduct(self, product: ProductVo):
        product.id = str(uuid.uuid4())
        productJson = jsonable_encoder(product)
        # product = {'id': str(uuid.uuid4()), 'description': 'product1','price': '5000'}
        container.create_item(productJson)
        return "ProductCosmosDaoImp"

    def readProduct(self):
        pass

    def updateProduc(self):
        pass

    def deleteProduct(self):
        pass