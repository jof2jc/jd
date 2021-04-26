from jd.api.base import RestApi

class CategoryApiReadGetAttrValueByValueIdRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.valueId = None

		def getapiname(self):
			return 'jingdong.category.api.read.getAttrValueByValueId'

			




