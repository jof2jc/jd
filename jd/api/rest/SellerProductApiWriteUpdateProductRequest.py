from jd.api.base import RestApi

class SellerProductApiWriteUpdateProductRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.packLong = None
			self.spuName = None
			self.commonAttributeIds = None
			self.keywords = None
			self.description = None
			self.countryId = None
			self.warrantyPeriod = None
			self.productArea = None
			self.minQuantity = None
			self.crossProductType = None
			self.packHeight = None
			self.taxesType = None
			self.appDescription = None
			self.weight = None
			self.subtitleHrefM = None
			self.qualityDays = None
			self.packWide = None
			self.catId = None
			self.whetherCod = None
			self.piece = None
			self.brandId = None
			self.subtitle = None
			self.isQuality = None
			self.spuId = None
			self.packageInfo = None
			self.afterSale = None
			self.clearanceType = None
			self.subtitleHref = None
			self.maxQuantity = None
			self.shopCategoryIds = None

		def getapiname(self):
			return 'jingdong.seller.product.api.write.updateProduct'

			




