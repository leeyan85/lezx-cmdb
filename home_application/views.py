# -*- coding: utf-8 -*-

from common.mymako import render_mako_context, render_json
from django.http import HttpResponse
import ump
import json
from django.http import JsonResponse
from account.decorators import login_exempt
from blueking.component.shortcuts import get_client_by_request
from django.conf import settings

@login_exempt
def home(request):
    server_info=ump.http_get()
    a= request.COOKIES['bk_token']
    return HttpResponse(json.dumps(server_info,ensure_ascii=False))
    #return render_mako_context(request, '/home_application/home.html', ctx)

@login_exempt
def get_app_list(request):
    client = get_client_by_request(request) #初始化client
    App_list=[]
    kwargs = {
        "app_code": settings.APP_ID,
        "app_secret": settings.APP_TOKEN,
        "bk_token": request.COOKIES['bk_token'],
        #"app_id": "4",
    }
    api_ret = client.cc.get_app_list(kwargs)
    #if api_ret['result'] is True:
    for app_name in api_ret['data']:
        App_info={'ApplicationName':app_name['ApplicationName'],'ApplicationID':app_name['ApplicationID']}
        App_list.append(App_info)
    return HttpResponse(json.dumps(App_list,ensure_ascii=False))


