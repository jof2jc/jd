from jd.api.base import RestApi

class EpistockUpdateEpiMerchantWareStockRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.wareStockUpdateListStr = None

		def getapiname(self):
			return 'jingdong.epistock.updateEpiMerchantWareStock'

			




