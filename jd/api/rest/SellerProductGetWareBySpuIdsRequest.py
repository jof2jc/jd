from jd.api.base import RestApi

class SellerProductGetWareBySpuIdsRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.spuId = None
			self.spuDescription = None
			self.spuImgs = None
			self.brandInfo = None
			self.skuIds = None

		def getapiname(self):
			return 'jingdong.seller.product.getWareBySpuIds'

			




