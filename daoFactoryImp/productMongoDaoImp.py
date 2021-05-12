from daoFactory.productDao import ProductDao
from fastapi.encoders import jsonable_encoder
from dto.vo.productVo import ProductVo
from bd.mongo import MongoDb

class ProductMongoDaoImp(ProductDao):
    def createProduct(self, product: ProductVo):
        mongo = MongoDb()
        db = mongo.getDb()
        db["products"].insert_one(jsonable_encoder(product))
        return "product created"

    def readProduct(self):
        pass

    def updateProduc(self):
        pass

    def deleteProduct(self):
        pass