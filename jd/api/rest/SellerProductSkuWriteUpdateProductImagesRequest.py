from jd.api.base import RestApi

class SellerProductSkuWriteUpdateProductImagesRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.imageApiVo = None

		def getapiname(self):
			return 'jingdong.seller.product.sku.write.updateProductImages'

			
	

class ImageApiVo(object):
		def __init__(self):
			self.colorId = None
			self.order = None
			self.productId = None
			self.imageByteBase64 = None




