from jd.api.base import RestApi

class SellerProductSkuWriteDelSkuRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.skuIds = None

		def getapiname(self):
			return 'jingdong.seller.product.sku.write.delSku'

			




