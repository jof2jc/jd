from jd.api.base import RestApi

class SellerCategoryApiReadGetAllCategoryRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.venderId = None

		def getapiname(self):
			return 'jingdong.seller.category.api.read.getAllCategory'

			




