# -*- coding: utf-8 -*-

from common.mymako import render_mako_context, render_json
from django.http import HttpResponse
import ump
import json
# from django.http import JsonResponse
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
    a= request.COOKIES['bk_token']

    print server_info
    print a
    return HttpResponse(json.dumps(server_info))
    #return render_mako_context(request, '/home_application/home.html', ctx)


def multiplication_computer(request):
    multiplier = int(request.POST.get('multiplier'))
    multiplicand = int(request.POST.get('multiplicand'))
    mult_result = multiplier * multiplicand
    mult_record = MultRecord(multiplier=multiplier, multiplicand=multiplicand, mult_result=mult_result)
    mult_record.save()
    return render_json({'result': True, 'mult_result': mult_result})

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


home()