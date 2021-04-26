from jd.api.base import RestApi

class SellerProductSkuReadGetSkuBySkuIdsRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.skuId = None

		def getapiname(self):
			return 'jingdong.seller.product.sku.read.getSkuBySkuIds'

			




