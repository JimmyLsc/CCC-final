from django.shortcuts import render
import couchdb
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from myapp import couchdb_url
import json
import os

path = os.getcwd()

with open(path + '/myapp/education_level.json', encoding='utf-8') as f:
    education = json.load(f)
with open(path + '/myapp/election.json', encoding='utf-8') as f:
    election = json.load(f)

states = ['vic', 'nsw', 'southern', 'western', 'tas', 'queens']

instance_object = [{},{},{},{}]


def index(request):
    return render(request, 'index.html')


def get_view_data(DB, state, viewname, type='reduce'):
    if type == 'reduce':
        result = DB[state].view(viewname)
        if len(result) == 0:
            return 0
        else:
            return [row.value for row in result][0]
    if type == 'text':
        result = DB[state].view(viewname, limit=5)
        return [row.value for row in result]


@require_http_methods(["GET"])
# 给piechart提供每一部分的数据 格式为[{value: , name;''}]
def get_geodata(request):
    response = {}
    try:
        response['msg'] = 'Success'
        response['pieChartData'] = [
            {'value': 10, 'name': 'shandong'},
            {'value': 55, 'name': 'beijing'},
            {'value': 45, 'name': 'yunnan'}]
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_data(request):
    DB = couchdb.Server(couchdb_url.url)
    print(couchdb_url.url)
    for i in DB:
        print(i)
    response = {}
    try:
        for state in states:
            if request.GET.get('state') == state:
                pos_num = int(get_view_data(DB, state, 'tweeterData/pos'))
                neg_num = int(get_view_data(DB, state, 'tweeterData/neg'))
                china_pos_num = int(get_view_data(DB, state,'tweeterData/china_pos'))
                china_neg_num = int(get_view_data(DB, state,'tweeterData/china_neg'))
                pos_value = 100 * pos_num / (pos_num + neg_num) if pos_num + neg_num != 0 else 0
                neg_value = 100 * neg_num / (pos_num + neg_num) if pos_num + neg_num != 0 else 0
                china_pos_value = 100 * china_pos_num / (china_pos_num + china_neg_num) if china_pos_num + china_neg_num != 0 else 0
                china_neg_value = 100 * china_neg_num / (china_pos_num + china_neg_num) if china_pos_num + china_neg_num != 0 else 0
                response['LabelData'] = [
                    {'name': 'positive',
                     'value': '%.2f%%' % (pos_value)},
                    {'name': 'negtive',
                     'value': '%.2f%%' % (neg_value)}
                ]
                response['LabelData_China'] = [
                    {'name': 'China positive',
                     'value': '%.2f%%' % (china_pos_value)},
                    {'name': 'China negtive',
                     'value': '%.2f%%' % (china_neg_value)}
                ]
                response['TextData_pos'] = get_view_data(DB, state, 'tweeterData/pos_text', type='text')
                response['TextData_neg'] = get_view_data(DB, state, 'tweeterData/neg_text', type='text')
                response['TextData_china_pos'] = get_view_data(DB, state, 'tweeterData/china_pos_text', type='text')
                response['TextData_china_neg'] = get_view_data(DB, state, 'tweeterData/china_neg_text', type='text')
                response['education'] = [
                    {'name': 'has no qualification',
                     'value': 1 - float(education[state]['persons_with_qualification_percentage'])},
                    {'name': 'lower than bachelor qualification',
                     'value': float(education[state]['persons_with_qualification_percentage']) - float(education[state]['persons_with_bachdeg_above_percentage'])},
                    {'name': 'above bachelor degree', 'value': education[state]['persons_with_bachdeg_above_percentage']},
                ]
                response['election'] = [
                    {'name': 'labor party', 'value': election[state]['australian_labor_party_votes']},
                    {'name': 'national coalition', 'value': election[state]["liberal_national_coalition_votes"]}
                ]
                response['msg'] = 'Success'
                response['msg'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
# 给piechart提供每一部分的数据 格式为[{value: , name;''}]
def get_information_data(request):
    response = {}
    try:
        print('cool')
        print(request.GET.get('instance_num'))
        instance = {'instance_num' : request.GET.get('instance_num')
                     ,'cpu_num' : request.GET.get('cpu_num')
                     ,'storage_usage' : request.GET.get('storage_usage')
                     ,'cpu_usage': request.GET.get('cpu_usage')
                     ,'disk_usage' : request.GET.get('disk_usage')}

        instance_object[int(request.GET.get('instance_num'))-1] = instance
        response['msg'] = 'ok'

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def get_combine_data(request):
    education_values = []
    election_values = []
    pos_values = []
    china_pos_values = []
    response = {}
    DB = couchdb.Server(couchdb_url.url)
    print(couchdb_url.url)
    for i in DB:
        print(i)
    try:
        for state in states:
            pos_num = int(get_view_data(DB, state, 'tweeterData/pos'))
            neg_num = int(get_view_data(DB, state, 'tweeterData/neg'))
            china_pos_num = int(get_view_data(DB, state, 'tweeterData/china_pos'))
            china_neg_num = int(get_view_data(DB, state, 'tweeterData/china_neg'))
            pos_value = pos_num / (pos_num + neg_num) if pos_num + neg_num != 0 else 0
            china_pos_value = china_pos_num / (
                        china_pos_num + china_neg_num) if china_pos_num + china_neg_num != 0 else 0
            education_values.append(education[state]['persons_with_bachdeg_above_percentage'])
            election_values.append(election[state]["liberal_national_coalition_votes_percentage"])
            pos_values.append(pos_value)
            china_pos_values.append(china_pos_value)
        response['education']={
            'name' : 'High Education Proportion',
            'type' : 'bar',
            'data' : education_values
        }
        response['election']={
            'name' :  'Liberal National Coalition Proportion',
            'type' : 'bar',
            'data' : election_values
        }
        response['pos']={
            'name': 'Overall Positive Tweet Proportion',
            'type': 'line',
            'data': pos_values
        }
        response['china_pos']={
            'name': 'Positive Tweet About China Proportion',
            'type': 'line',
            'data': china_pos_values
        }
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    print(response)
    return JsonResponse(response)




@require_http_methods(["GET"])
# 给piechart提供每一部分的数据 格式为[{value: , name;''}]
def send_information_data(request):
    response = {}
    try:
        for i in range(4):
            response['instance' + str(i+1)] = instance_object[i]

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)