# -*- coding: utf-8 -*-

from common.mymako import render_mako_context, render_json
from django.http import HttpResponse
import ump
import json
from django.http import JsonResponse
from account.decorators import login_exempt

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
    #a= request.COOKIES['bk_token']
    print server_info
    return JsonResponse(server_info)
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