from jd.api.base import RestApi

class EpistockQueryEpiMerchantWareStockRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.wareStockQueryListStr = None

		def getapiname(self):
			return 'jingdong.epistock.queryEpiMerchantWareStock'

			




