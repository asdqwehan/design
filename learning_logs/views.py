#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .forms import TopicForm, EntryForm, CommentForm, UserPermForm
from .models import Topic, Entry, Comment, UserPerm
from django.contrib.auth.decorators import login_required
from guardian.shortcuts import assign, remove_perm
from guardian.decorators import permission_required
# Create your views here.
def index(request):
    """学习笔记的主页"""
    topics = Topic.objects.all().order_by('-date_added')[:5]

    entry = Entry.objects.all()
    entryviews = entry.order_by("-views")[:5]
    entrydate = entry.order_by("-date_added")[:5]
    context = {'entry': entry, 'entryviews': entryviews, 'entrydate': entrydate, 'topics': topics}
    return render(request, 'learning_logs/index.html', context)

@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.all().order_by('date_added')
    topics_random = Topic.objects.all().order_by('?')[:2]
    context = {'topics': topics, 'topics_random': topics_random}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    #确认请求的主题属于当前用户
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据：创建一个表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #未提交数据，创建一个空表单
        form = EntryForm()
    else:
        #POST提交的表单，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            #permission
            assign('learning_logs.canchange_entry', new_entry.owner, new_entry)
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """编辑现有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        #初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        #POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

def entry(request, entry_id):
    """"""
    entry = Entry.objects.get(id=entry_id)
    entry.increase_views()
    comments = Comment.objects.filter(entry=entry)
    context = {'entry': entry, 'comments': comments}
    return render(request, 'learning_logs/entry.html', context)

def comment(request, entry_id):
    """Add new comments"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        commentform = CommentForm()
    else:
        commentform = CommentForm(data=request.POST)
        if commentform.is_valid():
            add_comment = commentform.save(commit=False)
            add_comment.entry = entry
            add_comment.owner = request.user
            add_comment.save()
            return HttpResponseRedirect(reverse('learning_logs:entry', args=[entry.id]))

    context = {'entry': entry, 'topic': topic, 'commentform': commentform}
    return render(request, 'learning_logs/comment.html', context)

def userapply(request, entry_id):
    """"""
    entry = Entry.objects.get(id=entry_id)
    userperm = UserPerm.objects.filter(entry=entry)
    applykey = 0
    for each in userperm:
        if request.user == each.applicant:
            applykey = 1
    context = {'entry': entry, 'userperm': userperm, 'applykey': applykey}
    return render(request, 'learning_logs/userapply.html', context)

def applying(request, entry_id):
    """"""
    entry = Entry.objects.get(id=entry_id)
    userperm = UserPerm.objects.filter(entry=entry)
    topic = entry.topic

    if request.method != "POST":
        userpermform = UserPermForm()
    else:
        add_userperm = UserPerm()
        add_userperm.entry = entry
        add_userperm.applicant = request.user
        add_userperm.save()
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'userperm': userperm}
    return render(request, 'learning_logs/applying.html', context)

