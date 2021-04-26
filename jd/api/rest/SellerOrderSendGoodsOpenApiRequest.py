from jd.api.base import RestApi

class SellerOrderSendGoodsOpenApiRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.expressNo = None
			self.expressCompany = None

		def getapiname(self):
			return 'jingdong.seller.order.sendGoodsOpenApi'

			




