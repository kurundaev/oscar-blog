from django.conf.urls import patterns, url
from mydashboard.views import BlogView, AddBlogView, BlogEditView

urlpatterns = patterns('',

    url(r'^blog/$', BlogView.as_view(), name='blog'),
    url(r'^add/blog/$', AddBlogView.as_view(), name='add_blog'),
    url(r'^edit/blog/(?P<pk>\d+)/$', BlogEditView.as_view(), name='edit_blog'),
)
