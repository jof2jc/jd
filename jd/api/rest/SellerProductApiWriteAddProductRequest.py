from jd.api.base import RestApi

class SellerProductApiWriteAddProductRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.spuInfo = None
			self.skuList = None

		def getapiname(self):
			return 'jingdong.seller.product.api.write.addProduct'

			
	

class SpuInfo(object):
		def __init__(self):
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
			self.packageInfo = None
			self.afterSale = None
			self.clearanceType = None
			self.subtitleHref = None
			self.maxQuantity = None
			self.shopCategorys = None


class SkuApiVo(object):
		def __init__(self):
			self.saleAttributeIds = None
			self.costPrice = None
			self.upc = None
			self.sellerSkuId = None
			self.saleAttrValueAlias = None
			self.skuName = None
			self.jdPrice = None
			self.stock = None




