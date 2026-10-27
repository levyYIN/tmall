from flask import Flask, request, jsonify

app = Flask(__name__)

# 1. 认证文件路由（关键！）
@app.route('/aligenie/f921262f703431d377b919265c9bdaec.txt')
def aligenie_auth():
    # 直接返回认证文件内容，Content-Type 设为 text/plain
    return "Jfc4Z4Ur15JwUBuvUQD5wg7Nu8+l+HscqYlfofbyJdbjRDcIzoV08n5+c0kt2kbf", 200, {'Content-Type': 'text/plain; charset=utf-8'}

# 2. 对话请求路由
@app.route('/', methods=['POST'])
def deepseek_chat():
    try:
        data = request.json
        user_query = data.get('query') or data.get('request', {}).get('utterance', '你好')
        
        # 调用 DeepSeek API（记得替换你的 Key）
        import requests
        api_key = "sk-你的密钥填这里"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": user_query}],
            "stream": False
        }
        resp = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload, timeout=25)
        answer = resp.json()['choices'][0]['message']['content']
        
        return jsonify({
            "returnCode": "0",
            "returnValue": {"reply": answer, "result": answer},
            "returnErrorSolution": "",
            "returnMessage": ""
        })
    except Exception as e:
        return jsonify({"returnCode": "1", "returnValue": {"reply": f"出错了：{str(e)}"}})