#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.forms import UserCreationForm
from guardian.shortcuts import assign, remove_perm
from learning_logs.models import Entry
from django.contrib.auth.models import User
# Create your views here.

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        #显示空的注册表单
        form = UserCreationForm()
    else:
        #处理填写好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #让用户自动登录, 再重定向到主页
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

def mypermissions(request):
    """"""
    myentry = Entry.objects.filter(owner=request.user)
    entries = []
    userperm = None

    for each in myentry:
        entries.append(each)
        userperm = each.userperm_set.all()

    if request.method == "POST":
        usernames = request.POST.getlist('applicants')
        for username in usernames:
            u = User.objects.get(username=username)
            userps = u.userperm_set.all()
            for userp in userps:
                entry = userp.entry
                assign('learning_logs.canchange_entry', u, entry)
        return HttpResponseRedirect(reverse('learning_logs:index'))
    
    context = {'myentry': myentry, 'entries': entries, 'userperm': userperm}
    return render(request, 'users/mypermissions.html', context)