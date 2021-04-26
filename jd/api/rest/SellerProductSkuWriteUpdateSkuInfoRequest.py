from jd.api.base import RestApi

class SellerProductSkuWriteUpdateSkuInfoRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.skuName = None
			self.spuId = None
			self.skuId = None
			self.sellerSkuId = None
			self.jdPrice = None
			self.costPrice = None
			self.stock = None

		def getapiname(self):
			return 'jingdong.seller.product.sku.write.updateSkuInfo'

			




