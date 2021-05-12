from daoFactory.productDao import ProductDao
from daoFactory.daoFactory import DaoFactory
from dto.vo.productVo import ProductVo

class ProductBo():

    productDao: ProductDao

    def __init__(self):
        self.productDao = DaoFactory.GetProductDao()

    def createProduct(self, product: ProductVo):
        return self.productDao.createProduct(product)



