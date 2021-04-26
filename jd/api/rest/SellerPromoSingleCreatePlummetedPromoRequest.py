from jd.api.base import RestApi

class SellerPromoSingleCreatePlummetedPromoRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.riskLevel = None
			self.promoChannel = None
			self.bindToken = None
			self.promoNum = None
			self.limitBuyType = None
			self.quota = None
			self.promoAdword = None
			self.beginTime = None
			self.areaId = None
			self.pId = None
			self.areaTag = None
			self.skuId = None
			self.childType = None
			self.userGrade = None
			self.promoType = None
			self.promoName = None
			self.activityUrl = None
			self.limitBuyMaxNum = None
			self.limitBuyMinNum = None
			self.endTime = None
			self.mobileActivityUrl = None
			self.promoReason = None
			self.storeId = None

		def getapiname(self):
			return 'jingdong.seller.promo.singleCreatePlummetedPromo'

			




