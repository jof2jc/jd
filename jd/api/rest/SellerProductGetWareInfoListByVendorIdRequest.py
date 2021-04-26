from jd.api.base import RestApi

class SellerProductGetWareInfoListByVendorIdRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.page = None
			self.size = None

		def getapiname(self):
			return 'jingdong.seller.product.getWareInfoListByVendorId'

			




