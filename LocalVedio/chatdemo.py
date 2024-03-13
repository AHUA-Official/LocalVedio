from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
#星火认知大模型v3.5的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
SPARKAI_APP_ID = '6c075a28'
SPARKAI_API_SECRET = 'ZGFjMDAzYWNiMzIwMzJkYTRjNzYzZjUz'
SPARKAI_API_KEY = '137ffdff7b42b854003df44f91e6848f'
#星火认知大模型v3.5的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_DOMAIN = 'generalv3.5'


import  re

def getmessage():
    messages = [ChatMessage(
        role="user",
        content=input("输入你")
        #input("请输入你的问题")
    )]
    return  messages
def getexit():
    return True
def wordjeixi(input_string):
    # 使用正则表达式匹配字符串中的 content 部分
    content_match = re.search(r"content='(.*?)'", input_string)
    if content_match:
        # 如果匹配成功，则提取并返回 content 部分的值
        return str(content_match.group(1))
    else:
        # 如果未找到匹配，则返回 None
        return "rtyui"
def main():
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    while(getexit()!=False):
        messages = getmessage()
        handler = ChunkPrintHandler()
        a = spark.generate([messages], callbacks=[handler])
        print(a)
        print(wordjeixi(str(a)))


def getmessagesss(query):
    messages = [ChatMessage(
        role="user",
        content=str(query)
        # input("请输入你的问题")
    )]
    return messages


def liaotian(query):
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    while (getexit() != False):
        messages = getmessagesss(query)
        handler = ChunkPrintHandler()
        a = spark.generate([messages], callbacks=[handler])
        print(a)
        print(wordjeixi(str(a)))
        return  a

if __name__ == '__main__':
    main()

