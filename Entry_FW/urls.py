from django.urls import path
from . import views

## 指定url次级路径
app_name = 'Entry_FW'
urlpatterns = [
    path('', views.index, name='index'),
    path('abstract',views.abstractpage,name="abstract"),
    path('researcher', views.researcher, name='researcher'),
    path('rtinfo',views.rtinfo,name='rtinfo'),
    path('keywordmap', views.keywordmappage, name='keywordmap'),
    path('keywordrel_data',views.keywordmapdata,name='keywordrel_data'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
]
