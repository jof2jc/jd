from jd.api.base import RestApi

class SellerOrderPrintOrderRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.printType = None
			self.printNum = None
			self.orderId = None

		def getapiname(self):
			return 'jingdong.seller.order.printOrder'

			




