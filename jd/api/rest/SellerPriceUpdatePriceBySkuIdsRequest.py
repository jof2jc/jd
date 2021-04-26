from jd.api.base import RestApi

class SellerPriceUpdatePriceBySkuIdsRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.salePrice = None
			self.skuId = None

		def getapiname(self):
			return 'jingdong.seller.price.updatePriceBySkuIds'

			




