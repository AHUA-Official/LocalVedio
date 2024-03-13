import json
import asyncio
import os
from functools import wraps
from flask import Flask, render_template, request, jsonify
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
from werkzeug.utils import secure_filename

from chatdemo import *

# 定义存储聊天记录的文件路径
CHAT_HISTORY_FILE = 'chat_history.json'

def load_chat_history():
    try:
        with open(CHAT_HISTORY_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_chat_history(history):
    with open(CHAT_HISTORY_FILE, 'w') as file:
        json.dump(history, file)

def time_limited(timeout):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                loop = asyncio.get_event_loop()
                result = await asyncio.wait_for(func(*args, **kwargs), timeout=timeout)
                return result
            except asyncio.TimeoutError:
                return {'response': '对不起，我没有明白你的意思'}
        return wrapper
    return decorator

@time_limited(3)  # 设置3秒超时
async def generate_ai_response(query):
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(role="user", content=query)]
    handler = ChunkPrintHandler()

    async def _generate():
        ai_response = await spark.generate_async([messages], callbacks=[handler])  # 假设存在异步方法generate_async
        response_content = wordjeixi(str(ai_response))
        return response_content

    return await _generate()

app = Flask(__name__)
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
SPARKAI_APP_ID = '6c075a28'
SPARKAI_API_SECRET = 'ZGFjMDAzYWNiMzIwMzJkYTRjNzYzZjUz'
SPARKAI_API_KEY = '137ffdff7b42b854003df44f91e6848f'
SPARKAI_DOMAIN = 'generalv3.5'

# 加载聊天记录
chat_history = load_chat_history()

@app.route('/')
def index():
    recent_chats = list(zip(chat_history[-8:], [''] * 8))  # 最近三条聊天记录
    return render_template('index.html', chats=recent_chats)
@app.route('/getpict',method=['GET'])
def getpict():
    #cong假照片生成的网址请求一张花的图片.返回给前端/或者直接返回对应的花的请求路径   给前端也好
    flower_picture_url = "https://example.com/path/to/a/beautiful/flower.jpg"
    return jsonify({"imageUrl": flower_picture_url})
@app.route('/uploadpict',method=['POST'])
def   uploadpict():
    #上传一张图片 ,并且把他注册到一张表里面
    # 检查是否有文件在请求中
    if 'file' not in request.files:
        return jsonify({"imageOK": False, "message": "No file part"}), 400

    file = request.files['file']

    # 如果用户没有选择文件，浏览器可能会提交一个没有文件名的空部分
    if file.filename == '':
        return jsonify({"imageOK": False, "message": "No selected file"}), 400

    if file :
        # 使用 secure_filename 确保安全的文件名
        filename = secure_filename(file.filename)
        # 保存图片
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # 返回 JSON 响应，包括图片的路径
        return jsonify({"imageOK": True, "path": file_path})

    return jsonify({"imageOK": False, "message": "File type is not allowed"}), 400
@app.route('/liaotian', methods=['POST'])
def liaotian():
    query = request.json.get('query')
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(role="user", content=query)]
    handler = ChunkPrintHandler()

    ai_response = spark.generate([messages], callbacks=[handler])
    response_content = wordjeixi(str(ai_response))

    # 更新聊天记录
    chat_history.append((query, response_content))
    save_chat_history(chat_history)

    return jsonify({'response': response_content})
if __name__ == '__main__':
    app.run(debug=True)