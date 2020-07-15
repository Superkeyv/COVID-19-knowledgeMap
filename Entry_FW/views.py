# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .apps import Entry_FWConfig
from urllib import request as rq
from django.conf import settings
import json

# 加载esAPI模块
from esAPI.covidapi import *

app_name = Entry_FWConfig.name

# 一些获取信息的链接
# json格式的实时状况数据，包括国内和国外情况，国外部分位于 'thertotal'
rtjson = 'https://news.sina.com.cn/project/fymap/ncp2020_full_data.json?_=1591602512921&callback=jsoncallback'
# 实时新闻信息
rtnews = 'https://interface.sina.cn/news/country_epidemic_lists.d.json?page=1&pagesize=3&callback=country_epidemic&_=1591602512910'
# 湖北省历史数据
his_province = 'https://gwpre.sina.cn/interface/news/ncp/data.d.json?mod=china_hubei_history&callback=hbApi_data&_=1591602512906'


def test(request):
    '''
    用于前端调试Debug页面
    :param request:
    :return:
    '''
    if (not settings.DEBUG):
        return Http404()
    template = loader.get_template('test.html')
    return HttpResponse(template.render())


def default_mainpage_data():
    '''
    抛弃使用

    :return:
    '''
    # (菜单名,图标), {菜单项:urls,...}
    mproject1 = (('工作', 'fa-cog'),
                 {'关键词图谱': 'keywordmap', '文献检索': 'researcher', })
    mproject2 = (('成果', 'fa-wrench'),
                 {'知识体系': 'url1', '医学术语表': 'url2', '药物关联': 'url3'})
    # [(文字，图，url),...]
    # rt_info = [('疫情趋势', 'fa-chart-area', 'rtinfo'), ('各国数据', 'fa-table', 'url2')]

    context = {
        'title': 'COVID-19知识图谱',
        'projects': [
            mproject1,
            # mproject2,
        ],
        # 'rt_info': rt_info,
        'container': abstractpage(None)
        # 'container': researcher(None)
    }

    return context



def index(request):
    '''
    初始化页面，用于显示摘要信息
    :param request:
    :return:
    '''
    template = loader.get_template(app_name + '/index.html')

    # (菜单名,图标), {菜单项:urls,...}
    mproject1 = (('工作', 'fa-cog'),
                 {'关键词图谱': 'keywordmap', '文献检索': 'researcher', })
    mproject2 = (('成果', 'fa-wrench'),
                 {'知识体系': 'url1', '医学术语表': 'url2', '药物关联': 'url3'})
    # [(文字，图，url),...]
    # rt_info = [('疫情趋势', 'fa-chart-area', 'rtinfo'), ('各国数据', 'fa-table', 'url2')]

    return HttpResponse(template.render(default_mainpage_data(), request))


def abstractpage(request):
    '''
    摘要页面，提供摘要信息的提取
    注意，其中的color项，包括有 color=(primary,success,info,warning,danger,secondary)
    :param request:
    :return:
    '''
    r = rq.urlopen(rtjson)
    rec = str(r.read())
    json_str = json.loads(rec[15:-3])  # 由于包含一些不合适的字符，在这里需要去掉
    othertotal = json_str['data']['othertotal']

    container = loader.get_template(app_name + '/cont_abstract.html')
    dataset = [('累积确诊', othertotal['certain'], 'primary'),
               ('现有确诊', int(othertotal['certain']) - int(othertotal['die']) - int(othertotal['recure']), 'info'),
               ('死亡', othertotal['die'], 'warning'),
               ('累积治愈', othertotal['recure'], 'success')]

    projects = [('疫苗研发', 20, 'primary'),
                ('病理研究', 50, 'success'),
                ('临床救治', 70, 'info'),
                ('医用物资生产', 30, 'warning'), ]
    context = {
        "dataset": dataset,
        # "project": projects,
    }
    if request == None:
        return container.render(context)
    else:
        return HttpResponse(container.render(context, request))


def rtinfo(request):
    '''
    实时信息显示，从api接口获取实时疫情信息，并显示在此。这里使用了其他网站的数据，直接渲染至此
    :param request:
    :return:
    '''
    r = rq.urlopen(rtjson)
    rec = str(r.read())
    json_str = json.loads(rec[15:-3])  # 由于包含一些不合适的字符，在这里需要去掉

    othertotal = json_str['data']['othertotal']
    container = loader.get_template(app_name + '/cont_rtinfo.html')
    dataset = [('累积确诊', othertotal['certain'], 'primary'),
               ('现有确诊', int(othertotal['certain']) - int(othertotal['die']) - int(othertotal['recure']), 'info'),
               ('死亡', othertotal['die'], 'warning'),
               ('累积治愈', othertotal['recure'], 'success')]

    context = {
        'dataset': dataset,

    }
    return HttpResponse(container.render(context, request))


def researcher(request):
    '''
    研究成果信息整理
    :param request:
    :return:
    '''
    container = loader.get_template(app_name + '/cont_researcher.html')

    return HttpResponse(container.render())


def keywordmappage(request):
    '''
    关键词图谱页面，与主界面内容一致
    :param request:
    :return:
    '''
    container = loader.get_template(app_name + '/cont_keywordmap.html')
    return HttpResponse(container.render(default_mainpage_data(), request))


def keywordmapdata(request):
    '''
    用于生成关系图绘图所需的数据
    :param request:
    :return:
    '''
    relation = read_relation()

    return JsonResponse(relation, safe=False)


def request_doclist(request):
    '''
    用于响应用户的POST请求，同时根据用户的参数，返回所需的json信息

    :param request:
    :return:
    '''
    if (request.method == "POST"):
        mode = request.POST['mode']
        info = request.POST['info']

        #     booldata={
        #         "doc_class": "a",
        #         "entity": "mpro"
        #     }
        if ("check_class" == mode):
            return JsonResponse(searchfilter_engine({"doc_class": info}), safe=False)

        if ("check_entry" == mode):
            return JsonResponse(searchfilter_engine({"entity": info}), safe=False)


def request_graph(request):
    '''
    返回对图的查询信息
    :param request:
    :return:
    '''
    if (request.method == "POST"):
        info = request.POST['info']

        res = get_graph(info)
        return JsonResponse(res, safe=False)
