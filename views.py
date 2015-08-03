# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView


from dashboard.models import Blog


class BlogView(ListView):
    template_name = 'mydashboard/blog/list.html'
    model = Blog


class BlogEditView(UpdateView):
    template_name = 'mydashboard/blog/edit.html'
    model = Blog
    success_url = reverse_lazy('mydashboard:blog')
    fields = ['title', 'text', 'photo', 'enable']


class AddBlogView(CreateView):
    template_name = 'mydashboard/blog/add.html'
    model = Blog
    fields = ['title', 'text', 'photo', 'enable']
