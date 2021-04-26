from jd.api.base import RestApi

class SellerOrderGetOrderInfoByOrderIdRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.orderId = None

		def getapiname(self):
			return 'jingdong.seller.order.getOrderInfoByOrderId'

			




