from abc import abstractmethod
from abc import ABCMeta

class ProductDao(metaclass=ABCMeta):
    @abstractmethod
    def createProduct(self):
        pass

    @abstractmethod
    def readProduct(self):
        pass

    @abstractmethod
    def updateProduc(self):
        pass

    @abstractmethod
    def deleteProduct(self):
        pass