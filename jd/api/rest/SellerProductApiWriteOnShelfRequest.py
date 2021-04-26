from jd.api.base import RestApi

class SellerProductApiWriteOnShelfRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.spuId = None

		def getapiname(self):
			return 'jingdong.seller.product.api.write.onShelf'

			




