
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home,name='home'),  
    url(r'^post/$', views.post_project, name='post_project'),
    url(r'^accounts/edit',views.edit_profile, name='edit_profile'),
    url(r'^profile', views.profile, name='profile'), 
    # url(r'^comments/(\d+)',views.comments,name="comments")    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)