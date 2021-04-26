from jd.api.base import RestApi

class SellerCategoryApiReadGetCategoryByCatIdsRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.catId = None

		def getapiname(self):
			return 'jingdong.seller.category.api.read.getCategoryByCatIds'

			




