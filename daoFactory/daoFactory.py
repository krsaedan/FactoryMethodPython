from daoFactoryImp.productMongoDaoImp import ProductMongoDaoImp
from daoFactoryImp.productCosmosDaoImp import ProductCosmosDaoImp

class DaoFactory():

    isMongoDb: bool= False

    @staticmethod
    def GetProductDao():
        if(False):
            return ProductMongoDaoImp()
        else:
            return ProductCosmosDaoImp()