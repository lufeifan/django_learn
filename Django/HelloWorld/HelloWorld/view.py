# from django.http import HttpResponse
 
# def hello(request):
#     return HttpResponse("Hello world !!!! ")

from django.shortcuts import render
 
def hello(request):
    import requests
    import json
    api_request = requests.get("http://jsonplaceholder.typicode.com/posts")
    api=json.loads(api_request.content)
    # context          = {}
    # context['hello'] = 'Hello World!!!!!!'
    return render(request, 'hello.html', {"api":api})

def index(request):
    sitename = 'Django中文网'
    url = 'www.django.cn'
    #新加一个列表
    list=[
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    #在来的基础上新加一个字典
    mydict={
        'name': '吴秀峰',
        'qq': '445813',
        'wx': 'vipdjango',
        'email': '445813@qq.com',
        'Q群': '10218442',
    }
    context = {
        'sitename': sitename,
        'url':url, 
        'list':list, #把list封装到context
        'mydict':mydict,
    }
    return render(request,'index.html',context)