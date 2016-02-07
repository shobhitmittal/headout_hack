"""headout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hd_hack import views as hd_views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^user_reg/', hd_views.first_page),
    url(r'^user_login/', hd_views.login),
    url(r'^create_event/', hd_views.create_event),
    url(r'^invite_members/', hd_views.invite_members),
    url(r'^user_loc_update/', hd_views.user_loc_update),
    url(r'^gcm_inbound/', hd_views.gcm_inbound),
    url(r'^gcm_outbound/', hd_views.gcm_outbound_message),
    url(r'^user_req_location/', hd_views.send_location),
    url(r'^add_tag/', hd_views.add_tag),
    url(r'^list_tags/', hd_views.list_tag),
    url(r'^event_done/', hd_views.event_completed),
    url(r'^add_callback_url/', hd_views.add_callback_url),
]
