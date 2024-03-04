# file : p56_slackMsg.py
# desc : 슬랙으로 스마트폰 메시지 보내기
'''순서
1. https://api.slack.com 에서 your apps > Create first app
2. From Scratch
3. 워크스페이스 선택
4. Incoming Webhooks > On > Add new Webhook to Workspace 클릭 > 채널 선택 > 허용
'''
 
import requests
import json
# url 재입력 후 실행
slack_url = 'https://hooks.slack.com/services/T06***F6***/B*6****A**D/***Bv1******qCk***cm****'

headers = { ' Content=type' : 'application/json'}
data = { 'text' : 'Python에서 보내는 메시지'}

res = requests.post(slack_url, headers=headers, data=json.dumps(data))
if res.status_code == 200:
    print('전송 성공')
else:
    print('전송 실패!')
