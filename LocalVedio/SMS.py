import urllib, sys
import ssl
from urllib.request import Request,urlopen


host = 'https://cxkjsms.market.alicloudapi.com'
path = '/chuangxinsms/dxjk'
method = 'POST'
appcode = 'df4fbb3124154b538de64cac18ae5a0c'#开通服务后 买家中心-查看AppCode
querys = 'content=%E3%80%90%E5%88%9B%E4%BF%A1%E3%80%91%E4%BD%A0%E7%9A%84%E9%AA%8C%E8%AF%81%E7%A0%81%E6%98%AF%EF%BC%9A5873%EF%BC%8C3%E5%88%86%E9%92%9F%E5%86%85%E6%9C%89%E6%95%88%EF%BC%81&mobile=1582149533'
bodys = {}
url = host + path + '?' + querys

request = Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)