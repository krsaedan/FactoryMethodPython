from dto.vo.productVo import ProductVo
from dto.bo.productBo import ProductBo

class ProductService():
    def createProduct(product: ProductVo):
        productBo = ProductBo()
        return productBo.createProduct(product)
