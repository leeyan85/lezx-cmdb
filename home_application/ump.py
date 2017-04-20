#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib2
import re

USLA = re.compile(ur"洛杉矶")  # 洛杉矶机房
CNBJ = re.compile(ur"北京")  # 北京机房
CNSZ = re.compile(ur"深圳")  # 深圳机房
CNGZ = re.compile(ur"广州")  # 广州机房
USWT = re.compile(ur"华盛顿")  # 华盛顿
INND = re.compile(ur"新德里")  # 印度新德里
CNHK = re.compile(ur"香港")  # 中国香港


def http_get():
    url = "http://ump.letv.cn/api/cmdb/servicetree/androidDevice?token=fc87fcc85afcbb9bc0585ef1154143ea"
    response = urllib2.urlopen(url)
    result_js = json.loads(response.read())
    print result_js
    return result_js


def get_tree_list(ump_server_data):
    tree_nodes = []
    for server in ump_server_data['data']:
        a = server['servicetree'][0]['parents'] + '_' + server['servicetree'][0]['name']
        if a not in tree_nodes:
            tree_nodes.append(a)

    for node in tree_nodes:
        print node
        print '_'.join(node.split('_')[2:])


def get_city_list(IDC, ump_server_data):
    server_list = []
    for server in ump_server_data['data']:
        if eval(IDC).search(server['lingshu_idc']):  # 洛杉矶机房
            tmp = {}
            server['lingshu_idc'], server['ip_data'][0]['ipaddr'], server['servicetree'][0]['parents'] + '_' + \
            server['servicetree'][0]['name']
            tmp['IDC'] = IDC
            tmp['ipaddr'] = server['ip_data'][0]['ipaddr']
            a = server['servicetree'][0]['parents'] + '_' + server['servicetree'][0]['name']
            server_list.append(tmp)
    return len(server_list), server_list

#http_get()