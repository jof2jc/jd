from jd.api.base import RestApi

class CategoryApiReadGetAttributesByCatIdRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.catId = None

		def getapiname(self):
			return 'jingdong.category.api.read.getAttributesByCatId'

			




