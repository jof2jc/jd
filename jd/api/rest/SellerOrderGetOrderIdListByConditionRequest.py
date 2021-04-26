from jd.api.base import RestApi

class SellerOrderGetOrderIdListByConditionRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.bookTimeEnd = None
			self.userPin = None
			self.orderType = None
			self.updateTimeEnd = None
			self.startRow = None
			self.deliveryType = None
			self.orderStatus = None
			self.createdTimeEnd = None
			self.updateTimeBegin = None
			self.createdTimeBegin = None
			self.bookTimeBegin = None
			self.pageNo = None
			self.pageSize = None
			self.siteIdListQuery = None

		def getapiname(self):
			return 'jingdong.seller.order.getOrderIdListByCondition'

			




