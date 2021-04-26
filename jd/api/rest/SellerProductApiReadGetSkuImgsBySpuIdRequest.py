from jd.api.base import RestApi

class SellerProductApiReadGetSkuImgsBySpuIdRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.spuId = None
			self.currentPage = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.seller.product.api.read.getSkuImgsBySpuId'

			




