from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static


from core.views import register, user_login, user_logout, index, resources, feedback, profile

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^', include('qa.urls')),
    url(r'^index/$', index, name='index'),
	url(r'^resources/$', resources, name='resources'),
	url(r'^feedback/$', feedback, name='feedback'),
	url(r'^profile/$', profile, name='profile'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	
