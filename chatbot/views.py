from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render
import json
import os
from pathlib import Path

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, FlexSendMessage
 
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 
BASE_DIR = Path(__file__).resolve().parent

@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                if(event.message.text == 'competition'):
                    FlexMessage = json.load(open(os.path.join(BASE_DIR, 'flex_msg/competition.json'),'r',encoding='utf-8'))
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
                elif (event.message.text == 'skill'):
                    FlexMessage = json.load(open(os.path.join(BASE_DIR, 'flex_msg/skill.json'),'r',encoding='utf-8'))
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
                elif (event.message.text == 'Technical skill'):
                    FlexMessage = json.load(open(os.path.join(BASE_DIR, 'flex_msg/technical_skill.json'),'r',encoding='utf-8'))
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
                elif (event.message.text == 'Office skill'):
                    FlexMessage = json.load(open(os.path.join(BASE_DIR, 'flex_msg/office_skill.json'),'r',encoding='utf-8'))
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
                elif (event.message.text == 'Soft skill'):
                    FlexMessage = json.load(open(os.path.join(BASE_DIR, 'flex_msg/soft_skill.json'),'r',encoding='utf-8'))
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
                elif (event.message.text == 'Language skill'):
                    FlexMessage = json.load(open(os.path.join(BASE_DIR, 'flex_msg/language_skill.json'),'r',encoding='utf-8'))
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
                elif (event.message.text == 'club and activities'):
                    FlexMessage = json.load(open(os.path.join(BASE_DIR, 'flex_msg/club_and_activities.json'),'r',encoding='utf-8'))
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
                elif (event.message.text == 'project'):
                    FlexMessage = json.load(open(os.path.join(BASE_DIR, 'flex_msg/project.json'),'r',encoding='utf-8'))
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
                elif (event.message.text == 'about me'):
                    FlexMessage = json.load(open(os.path.join(BASE_DIR, 'flex_msg/about_me.json'),'r',encoding='utf-8'))
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
                #else :
                #    line_bot_api.reply_message(  # 回復傳入的訊息文字
                #    event.reply_token,
                #    TextSendMessage(text=event.message.text)
                #)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def RESUME(request):
    return render(request, 'RESUME.html')

def meichu_hackathon(request):
    return render(request, 'meichu_hackathon.html')

def LINE_FRESH(request):
    return render(request, 'LINE_FRESH.html')

def about_me(request):
    return render(request, 'about_me.html')

def database(request):
    return render(request, 'database.html')

def machine_learning(request):
    return render(request, 'machine_learning.html')
