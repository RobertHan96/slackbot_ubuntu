import json
from slacker import Slacker
from flask import Flask, request, make_response
from selenium import webdriver

from Coin import Coin
from Programmers import Programmers
from Wanted import Wanted
API_KEY = 'xoxb-1212367717746-1198395599847-AAIkHF7CgFUIsEAcPZdkDOLv'
# 이전 봇 토큰키 'xoxb-1212367717746-1198395599847-pgjFdold2da9j5xSvPeqFPyF'
slack = Slacker(API_KEY)

app = Flask(__name__)
default_answer = '안녕하세요! :) 원하는 명령어를 입력해주세요.\n1.코인 : 가상화페 시세\n2. 채용정보 보기 : 원티드 또는 프로그래머스 입력'


@app.route("/")
def get_answer(request_type):
    if '코인' in request_type:
        obj_coin = Coin()
        return obj_coin.getCoinInfo()
    elif '원티드' in request_type:
        obj_wanted = Wanted()
        return obj_wanted.getWantedInfo()
    elif '프로그래머스' in request_type:
        obj_prgrammers = Programmers()
        return obj_prgrammers.getProgrammersInfo()
    return default_answer

@app.route("/slack", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)
    return make_response("슬랙 요청에 이벤트가 없습니다.", 404, {"X-Slack-No-Retry": 1})



# 이벤트 핸들하는 함수
def event_handler(event_type, slack_event):
    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]

        if len(slack_event["event"]["blocks"][0]["elements"][0]['elements']) == 2 :
            user_req_type = slack_event["event"]["blocks"][0]["elements"][0]['elements'][1]['text']
            print('[Log] 유저 메세지 - ',user_req_type)
            response_text = get_answer(user_req_type)

            slack.chat.post_message(channel, response_text)
            return make_response("앱 멘션 메시지가 보내졌습니다.", 200, )
        else :
            slack.chat.post_message(channel, default_answer)
            return make_response("앱 멘션 메시지가 보내졌습니다.", 200, )
    message = "[%s] 이벤트 핸들러를 찾을 수 없습니다." % event_type
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
