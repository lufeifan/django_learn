from django.shortcuts import render,render_to_response
from .models import Test
from django.http import HttpResponse
# Create your views here.

def hello(request):
    data='data添加成功'
    return render(request,'base.html',{"data":data})


def dbadd(request):
    test=Test(name='ok4')
    test.save()
    return HttpResponse('添加成功')

def dbfind(request):
    # test=Test.objects.all()
    reponsel=Test.objects.get(id=4)
    return HttpResponse(reponsel)

def dbupdate(request):
    Test.objects.filter(id=5).update(name='ok5')
    return HttpResponse('修改成功')

def dbdelete(request):
    Test.objects.filter(name='ok').delete()
    return HttpResponse('删除成功')

def search_from(request):
    return render_to_response('search.html')

def search(request):
    # request.encoding='utf-8'
    if 'q' in request.GET:
        mes=request.GET['q'].encode('utf-8')
    else :
        mes='null'
    return HttpResponse(mes)