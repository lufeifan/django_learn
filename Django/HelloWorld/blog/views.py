
# 数据查询，就是在视图函数里(views.py文件里)对模型Product进行实例化，并生成对象。生成的对象就是我们要查询的数据。
# 然后我们可以对这个对象的属性进行逐一赋值，对象的属性来自于Product模型中所定义的字段。直白一点的说法就是，
# 我们在视图层里对某一个数据库表进行查询，然后得到一个对象，我们可以通过这个对象能获取到这个表里的所有字段的值。
from django.shortcuts import render

# Create your views here.
#比如我信要查询所有文章，我们就要views.py文件头部把文章表从数据模型导入
# from .models import Article

# def index(request):
#     #对Article进行声明并实例化，然后生成对象allarticle
#     allarticle = Article.objects.all()
#     #把查询到的对象，封装到上下文
#     context = {
#         'allarticle': allarticle,
#     }
#     #把上传文传到模板页面index.html里
#     return render(request,'index.html',context)

#首页
from blog.models import Category, Banner,Article,Tag
#把Banner表导入
def index(request):
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]#查询所有幻灯图数据，并进行切片
    tui = Article.objects.filter(tui__id=1)[:3]#查询推荐位ID为1的文章
    allarticle = Article.objects.all().order_by('-id')[0:10]
    context = {
                'allcategory': allcategory,
                'banner':banner, #把查询到的幻灯图数据封装到上下文
                'tui':tui,
                'allarticle': allarticle,
        }
    return render(request, 'index.html', context)
#列表页
def list(request,lid):
    list = Article.objects.filter(category_id=lid)#获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=lid)#获取当前文章的栏目名
    remen = Article.objects.filter(tui__id=2)[:6]#右侧的热门推荐
    allcategory = Category.objects.all()#导航所有分类
    tags = Tag.objects.all()#右侧所有文章标签
    return render(request, 'list.html', locals())

#内容页
def show(request,sid):
    pass

#标签页
def tag(request, tag):
    pass

# 搜索页
def search(request):
    pass
# 关于我们
def about(request):
    pass