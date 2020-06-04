from django.urls import path
from . import views

## 指定url次级路径
app_name = 'Entry_FW'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
]
