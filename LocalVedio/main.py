#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
from glob import glob
import os

from flask import Flask, request, jsonify, jsonify
from flask import render_template
from flask_cors import CORS





class LampController:
    @staticmethod
    def run_asr(input_queue, output_queue):
        """语音识别模型推理，并返回识别文本。"""
        print('Loading models...')

        print('asr ready')
        while True:
            if input_queue.empty():
                continue
            input_wav_file = input_queue.get()
            text = "fghjkl"
            output_queue.put(text)

    @staticmethod
    def process_lamp_cmd(input_queue, output_queue):
        """接收语音识别文本，发送台灯控制指令。"""
        while True:
            if input_queue.empty():
                continue
            asr_output_txt = input_queue.get()

            cmd = None
            if asr_output_txt == '开灯':
                msg = '灯光已打开。'
                #cmd = f'miiocli yeelight --ip {lamp_ip} --token {lamp_token} on'
            elif asr_output_txt == '关灯':
                msg = '灯光已关闭。'
               # cmd = f'miiocli yeelight --ip {lamp_ip} --token {lamp_token} off'
            else:
                msg = '指令无法识别。当前可识别的指令有：“开灯”，“关灯”。'

            if cmd is not None:
                os.system(cmd)

            response = {
                "code": 200,
                "data": {
                    "isEnd": True,
                    "message": msg
                }
            }
            output_queue.put(response)




def create_flask_app():
    app = Flask(
        __name__,
        # 设置静态文件夹目录
        static_folder='./dist',
        template_folder="./dist",
        static_url_path=""
    )

    CORS(app, resources=r'/*')

    @app.route('/')
    def index():
        return render_template('index.html', name='index')

    @app.route("/chat", methods=["GET"])
    def get_chat():
        args = request.args
        message = args.get("message")
        print('msg received')
        #lamp_cmd_in_q.put(message)
        data = {
            "code": 200,
            "message": ''
        }
        return jsonify(data)

    @app.route("/getMsg", methods=["GET"])
    def get_msg():


        data = "fghjkl"
        print(data)
        return jsonify(data)

    @app.route("/upload", methods=["POST"])
    def save_file():
        """保存录音文件，传给语音识别模型"""
        data = request.json
        asr_output_txt = data['message']



        data = {
            "code": 200,
            "data": {
                "message": asr_output_txt
            }
        }
        return jsonify(data)

    return app


if __name__ == '__main__':


    # 创建并运行flask应用
    flask_app = create_flask_app()
    flask_app.run(
        host="0.0.0.0",
        port=5000
    )
