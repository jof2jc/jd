from jd.api.base import RestApi

class SellerPromoSingleTerminatePromoRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.processId = None
			self.promoId = None

		def getapiname(self):
			return 'jingdong.seller.promo.singleTerminatePromo'

			




