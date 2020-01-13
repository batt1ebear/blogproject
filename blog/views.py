from django.shortcuts import render, get_object_or_404
import markdown
from .models import Post, Category
from comments.forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
import json
import time
from PIL import Image
from django.conf import settings
from django.http import HttpResponse

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    post.body=markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])

    #增加一次阅读量
    post.increase_viewed()
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)

def category(request,pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
    
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


static_base = 'http://127.0.0.1:8000'
static_url = static_base + settings.STATIC_URL + 'blog/img/blog-img/'  # 上传文件展示路径前缀
#re_STATIC_ROOT = settings.STATIC_ROOT.replace("\\","/")

@csrf_exempt
def upload_img(request):
    file = request.FILES['file']
    data = {
        'error':True,
        'path':'',
    }
    if file:
        timenow = int(time.time()*1000)
        timenow = str(timenow)
        try:
            img = Image.open(file)
            img.save("C:/Users/Microsoft/source/repos/blogproject/blog/static/blog/img/blog-img/"+ timenow + str(file))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps(data), content_type="application/json")
        imgUrl = static_url + timenow + str(file)
        data['error'] = False
        data['path'] = imgUrl
    return HttpResponse(json.dumps(data), content_type="application/json")