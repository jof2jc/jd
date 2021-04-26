from jd.api.base import RestApi

class ComJdQlBasicWsGlscGlscBasicSecondaryWSGetAssortByFidRequest(RestApi):
		def __init__(self,domain,port=80):
			RestApi.__init__(self,domain, port)
			self.assFid = None

		def getapiname(self):
			return 'jingdong.com.jd.ql.basic.ws.glsc.GlscBasicSecondaryWS.getAssortByFid'

			




