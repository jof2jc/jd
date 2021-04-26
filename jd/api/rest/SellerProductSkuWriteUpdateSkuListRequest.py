from jd.api.base import RestApi

class SellerProductSkuWriteUpdateSkuListRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.spuId = None
			self.costPrice = None
			self.sellerSkuId = None
			self.skuName = None
			self.jdPrice = None
			self.skuId = None

		def getapiname(self):
			return 'jingdong.seller.product.sku.write.updateSkuList'

			




