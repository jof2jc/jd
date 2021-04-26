from jd.api.base import RestApi

class SellerPromoQueryPlummetedInfoByConditionRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.thirdArea = None
			self.pageSize = None
			self.ltCreateTime = None
			self.secondArea = None
			self.promoId = None
			self.skuId = None
			self.childType = None
			self.userGrade = None
			self.ltBeginTime = None
			self.promoState = None
			self.firstArea = None
			self.page = None
			self.gtCreateTime = None
			self.riskLevel = None
			self.gtBeginTime = None
			self.gtEndTime = None
			self.promoName = None
			self.ltEndTime = None
			self.spuId = None
			self.storeIds = None

		def getapiname(self):
			return 'jingdong.seller.promo.queryPlummetedInfoByCondition'

			




