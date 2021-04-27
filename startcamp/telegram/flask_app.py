
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello!'

# 챗봇이 메세지를 받으면 여기에서 업데이트 내용을 확인할거임
@app.route('/ssafy')
def ssafy():
    # 누가 메세지를 보냈는지 확인 => chat_id를 확인
    
    # 어떤 메세지를 보냈는지 확인 (미세먼지)
    
    # 메세지에 따라서 다른 답변을 chat_id 에 전송

    return True