# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class container_abstract():
    def __init__(self,template_path):
        self.container=loader.get_template(template_path)
        self.context={"test":1,}

    def default_template(self):
        return self.container.render(self.context)




def index(request):
    template = loader.get_template('Entry_FW/index.html')
    container=container_abstract('Entry_FW/container_template.html')

    # (菜单名,图标), {菜单项:urls,...}
    mproject1=(('工作','fa-cog'),
               {'关键词图谱':'url1','研究者':'url2','病毒机理':'url3'})
    mproject2=(('成果','fa-wrench'),
               {'知识体系':'url1','医学术语表':'url2','药物关联':'url3'})
    # [(文字，图，url),...]
    rt_info=[('疫情趋势','fa-chart-area','url1'),('各国数据','fa-table','url2')]

    context = {
        'title': 'COVID-19知识图谱',
        'projects':[mproject1,mproject2],
        'rt_info':rt_info,
        'container':container.default_template()
    }
    return HttpResponse(template.render(context, request))



#
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'Entry_FW/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'Entry_FW/results.html', {'question': question})

