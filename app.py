from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def get_qa():
    """读取并返回当前文件夹下QA.json的内容"""
    try:
        # 获取当前文件所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 拼接QA.json文件路径
        file_path = os.path.join(current_dir, 'data','QA.json')
        
        # 检查文件是否存在
        if not os.path.exists(file_path):
            return jsonify({"error": "QA.json文件不存在"}), 404
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            qa_data = json.load(f)
        
        # 返回JSON数据
        return jsonify(qa_data)
    
    except json.JSONDecodeError:
        return jsonify({"error": "QA.json文件格式不正确"}), 500
    except Exception as e:
        return jsonify({"error": f"读取文件时发生错误: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)