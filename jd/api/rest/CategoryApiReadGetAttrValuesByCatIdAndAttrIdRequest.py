from jd.api.base import RestApi

class CategoryApiReadGetAttrValuesByCatIdAndAttrIdRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.catId = None
			self.attrId = None
			self.currentPage = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.category.api.read.getAttrValuesByCatIdAndAttrId'

			




