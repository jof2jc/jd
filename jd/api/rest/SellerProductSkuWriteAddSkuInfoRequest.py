from jd.api.base import RestApi

class SellerProductSkuWriteAddSkuInfoRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.spuId = None
			self.packLong = None
			self.saleAttributeIds = None
			self.costPrice = None
			self.upc = None
			self.weight = None
			self.sellerSkuId = None
			self.saleAttrValueAlias = None
			self.skuName = None
			self.packWide = None
			self.piece = None
			self.jdPrice = None
			self.packHeight = None
			self.stock = None

		def getapiname(self):
			return 'jingdong.seller.product.sku.write.addSkuInfo'

			




