"""mysite URL Configuration

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
from django.conf.urls import url,include,patterns
from django.contrib import admin
from dashboard import views
import settings

urlpatterns = [
	url(r'^$',views.fault_list,name='fault_list'),
	url(r'^admin/', admin.site.urls),
	url(r'^ucs_list_data/$',views.ucs_list_data,name='ucs_list_data'),
	url(r'^ucs_list/$',views.ucs_list,name='ucs_list'),
	url(r'^vm_list_data/$',views.vm_list_data,name='vm_list_data'),
	url(r'^vm_list/$',views.vm_list,name='vm_list'),
	url(r'^inc_list_data/$',views.inc_list_data,name='inc_list_data'),
	url(r'^inc_list/$',views.inc_list,name='inc_list'),
	url(r'^change_list_data/$',views.change_list_data,name='change_list_data'),
	url(r'^change_list/$',views.change_list,name='change_list'),
	url(r'^fault_list_data/$',views.fault_list_data,name='fault_list_data'),
	url(r'^fault_list/$',views.fault_list,name='fault_list'),
	url(r'^creation_list_data/$',views.creation_list_data,name='creation_list_data'),
	url(r'^creation_list/$',views.creation_list,name='creation_list'),
	url(r'^event_list_data/$',views.event_list_data,name='event_list_data'),
	url(r'^event_list/$',views.event_list,name='event_list'),

]
