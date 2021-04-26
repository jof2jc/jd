from jd.api.base import RestApi

class ComJdOrderTrackSiteExportQueryOrderFlowLogsForAPIRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.orderId = None

		def getapiname(self):
			return 'jingdong.com.jd.OrderTrackSiteExport.queryOrderFlowLogsForAPI'

			




