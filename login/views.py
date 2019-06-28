from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate ,logout ,login
from .forms import LoginForm
 
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from blog import views


def auth_view(request):
    if request.method == 'POST':#判断是否为一个POST请求    
            username = request.POST.get("username")#获取表单中用户名称
            password = request.POST.get("password")#获取表单中用户密码
            user = authenticate(username=username, password=password)#调用authenticate认证用户
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return views.index(request)
                    # Redirect to a success page
             
            else:
                response = HttpResponse()
                response.write('<html><script type="text/javascript">alert("密码错误"); window.location=""</script></html>')
                return response
                # Return an 'invalid login' error message.
    
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})

def log_out(request):
    logout(request)
    return auth_view(request)

