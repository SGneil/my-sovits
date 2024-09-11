from flask import Flask, request, jsonify
from flask_cors import CORS  # 导入 CORS 扩展
import run

app = Flask(__name__)
CORS(app)  # 允许所有域名的跨域请求

@app.route('/get_audio', methods=['POST'])
def run_demo():
    data = request.json
    text = data.get('text')
    sovits_role = data.get('sovits_role')
    save_audio_path = data.get('save_audio_path')
    
    try:
        url = 'http://127.0.0.1:5004/tts'
        characterEmotion = 'default'
        run.send_request(url, sovits_role, characterEmotion, text, save_audio_path)
        # print(text, sovits_role, save_audio_path)
        return jsonify({'status': 'OK'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
