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
    """
    首页
    """
    '''
    all_record = MultRecord.objects.all()
    ctx = {
         'all_record': all_record
    }
    '''
    print "hello,world!"
    server_info=ump.http_get()
    a= request.COOKIES['bk_token']
    #print server_info
    return JsonResponse("your cookies key 'bk_token' is %s" %a)
    #return HttpResponse('hello,world!')
    #return render_mako_context(request, '/home_application/home.html', ctx)



def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

@login_exempt
def get_app_list(request):
    client = get_client_by_request(request)
    # 获取作业id
    kwargs = {
        "app_code": settings.APP_ID,
        "app_secret": settings.APP_TOKEN,
        "bk_token": request.COOKIES['bk_token'],
        #"app_id": "4",
    }
    result = client.cc.get_app_list(kwargs)
    print result
    return JsonResponse(json.dumps(result))
    #if not result['result']:
        #return render_json({'result': True, 'message': result['message'] or u'执行失败'})