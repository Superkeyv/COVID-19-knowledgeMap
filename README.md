# 功能创建

（包含数据模型、视图、Html模板、静态资源等)



# install

使用pycharm加载工程(IDE=pycharm)

加载了pycharm以后，部署一下机器的运行环境，使用命令

```
pip install -e .
```

安装软件依赖库

使用命令，安装开发环境依赖库

```
pip install -e . "[dev]"
```



# run

django的运行，需要使用python运行如下命令

```
python manage.py runserver
```

> 注意，这里不需要自己打开一个python的终端，也不需要打开windows的cmd面板。在pycharm的下方有`Terminal`，在这个地方就可以开启python终端



html模板文件修改，网页自动刷新功能需要使用`livereload`插件，推荐使用firefox、Chrome开发网页。

Django端开启livereload 服务，需要使用如下命令，(此处我已经配置好Django)

```
python manage.py livereload
```



# Django的开发逻辑

建议阅读Django的官方开发指南

https://docs.djangoproject.com/zh-hans/2.1/

阅读快速入门部分是一个不错的选择