from mitmproxy import ctx
import json,os

class ModifyResponse:
    def response(self,flow):
        #拦截指定的url
        if flow.request.url.startswith("http://mooc1.chaoxing.com/ananas/videojs-ext/videojs-ext.min.js"):
            #返回数据json，绝对路径
            with open('./video.js','rb') as f:
                #res = json.load(f)
            #设置返回数据
                s = 'var sendLog_=function(player,isdrag,currentTimeSec,callback){'
                a = flow.response.get_text().replace(s, s+ 'currentTimeSec = params.duration; ')
                flow.response.set_text(a)
                ctx.log.info('modify words-template response')
            #log中打印

addons = [
    ModifyResponse()
]
#https://passport2.chaoxing.com/login?loginType=4&fid=62991&newversion=true&refer=http://i.mooc.chaoxing.com
