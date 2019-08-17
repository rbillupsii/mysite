from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from myblog.models import Post, Category
from myblog.forms import PostModelForm

from rest_framework import viewsets
from .serializers import post_serializer, category_serializer

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'list.html', context)

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'detail.html', context)

class post_view(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_date')
    serializer_class = post_serializer

class category_view(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = category_serializer
