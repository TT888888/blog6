from django.shortcuts import render,HttpResponse,redirect

from post.models import Article,Comment


# 首页看文章
def home(request):
    article =Article.objects.all()
    return render(request,'home.html',{'aeticle':article})
#
def article(request):
    # 获取aid,如果没有就默认值1
    aid = int(request.GET.get('aid',1))
    article = Article.objects.get(id=aid)
    comments=Comment.objects.filter(aid=aid)
    return render(request,'article.html',{'article':article,'comments':comments})


# 写文章
def create(request):
    if request.method=="POST":
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        article = Article.objects.create(title=title,content=content)
        return redirect('/post/article/?aid=%s' % article.id)
        # return HttpResponse(12321)

    else:
        return render(request,'create.html')



# 编辑
def editor(request):
    if request.method =="POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        aid = int(request.POST.get('aid'))

        article=Article.objects.get(id=aid)
        # 提交到数据库
        article.title=title
        article.content=content
        article.save()
        return redirect('/post/article/?aid=%s' % article.id)
        # return render(request, 'editor.html', {'article': article})
    else:
        aid = int(request.GET.get('aid',1))
        article = Article.objects.get(id=aid)

        return render(request,'editor.html',{'article':article})

#评论
def comment(request):

    if request.method == "POST":
        name = request.POST.get('name')
        content = request.POST.get('content')
        aid = request.POST.get('aid')

        Comment.objects.create(name=name,content=content,aid=aid)

        return redirect('/post/article/?aid={}'.format(aid))
    return redirect('/post/home/')

# 评论
def search():
    return None