from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^signup/$', views.usersignup , name='signup'),
    url(r'^login/$', views.userlogin , name='login'),
    url(r'^logout/$', views.userlogout , name='logout'),


    url(r'^beancreate/$', views.bean_create , name='beancreate'),
    url(r'^beanupdate/(?P<bean_id>[-\w]+)/$', views.bean_update , name='beanupdate'),
    url(r'^beandelete/(?P<bean_id>[-\w]+)$', views.bean_delete , name='beandelete'),
    url(r'^beandetail/(?P<bean_id>[-\w]+)/$', views.bean_detail , name='beandetail'),
    url(r'^beanlist/$', views.bean_list , name='beanlist'), 


    # url(r'^roastcreate/$', views.roast_create , name='roastcreate'),
    # url(r'^roastupdate/(?P<slug>[-\w]+)/$', views.roast_update , name='roastupdate'),
    # url(r'^roastdelete/(?P<slug>[-\w]+)$', views.roast_delete , name='roastdelete'),
    # url(r'^roastdetail/(?P<slug>[-\w]+)/$', views.roast_detail , name='roastdetail'),
    # url(r'^roastlist/(?P<slug>[-\w]+)/$', views.roast_list , name='roastlist'),


    # url(r'^syrupcreate/$', views.syrup_create , name='syrupcreate'),
    # url(r'^syrupupdate/(?P<slug>[-\w]+)/$', views.syrup_update , name='syrupupdate'),
    # url(r'^syrupdelete/(?P<slug>[-\w]+)$', views.syrup_delete , name='syrupdelete'),
    # url(r'^syrupdetail/(?P<slug>[-\w]+)/$', views.syrup_detail , name='syrupdetail'),
    # url(r'^syruplist/(?P<slug>[-\w]+)/$', views.syrup_list , name='syruplist'),


    # url(r'^powdercreate/$', views.powder_create , name='powdercreate'),
    # url(r'^powderupdate/(?P<slug>[-\w]+)/$', views.powder_update , name='powderupdate'),
    # url(r'^powderdelete/(?P<slug>[-\w]+)$', views.powder_delete , name='powderdelete'),
    # url(r'^powderdetail/(?P<slug>[-\w]+)/$', views.powder_detail , name='powderdetail'),
    # url(r'^powderlist/(?P<slug>[-\w]+)/$', views.powder_list , name='powderlist'),    
    
    

	]