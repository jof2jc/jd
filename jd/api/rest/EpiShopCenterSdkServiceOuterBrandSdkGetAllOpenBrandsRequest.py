from jd.api.base import RestApi

class EpiShopCenterSdkServiceOuterBrandSdkGetAllOpenBrandsRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)

		def getapiname(self):
			return 'jingdong.epi.shop.center.sdk.service.outer.BrandSdk.getAllOpenBrands'

			




