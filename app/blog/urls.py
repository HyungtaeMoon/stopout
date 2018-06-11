from django.conf.urls import url

# from blog.views import post_list
from .views import (
    school_list
)
urlpatterns = [

    url(r'^$', school_list, name='school-list'),
]