from django.conf.urls import url, include
from django.contrib import admin
from LMList import views 

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),
    #url(r'^company$', views.company, name='company'),
    url(r'^reg$', views.reg_list, name='reg_list'),
    url(r'^ulogin$', views.ulogin, name='ulogin'),
    url(r'^user_log$', views.user_log, name='user_log'),
    url(r'^(\d+)/user_status$', views.user_status, name='user_status'),
    url(r'^admin_log$', views.admin_log, name='admin_log'),
    url(r'^uregister$', views.uregister, name='uregister'),
    url(r'^update$', views.update, name='update'),
    url(r'^adminn$', views.adminn_list, name='adminn_list'),
    url(r'^about$', views.about_list, name='about_list'),
    url(r'^applicant$', views.applicant_list, name='applicant_list'),
    url(r'^table$', views.table_list, name='table_list'),
    url(r'^login$', views.login_list, name='login_list'),
    url(r'^contact$', views.contact_list, name='contact_list'),
    url(r'^applicantinfo$', views.applicantinfo_list, name='applicantinfo_list'),
    url(r'^last$', views.last_list, name='last_list'),
    #url(r'^LMList/admin$', views.admin_list, name='admin_list'),
    url(r'^new$', views.new_list, name='new_list'),
   
    url('admin/', admin.site.urls),

    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'), 
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'), 
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),

   
    url(r'^(\d+)/next/user_status$', views.user_status, name='user_status'),
    url(r'^applicant_status$', views.applicant_status, name='applicant_status'),  
    url(r'^applicant_status/statusupdate$', views.statusupdate, name='statusupdate'), ]

    #path('register/', views.registerPage, name="register"),
    #path('login/', views.loginPage, name="login"),  
    #path('logout/', views.logoutUser, name="logout"),]

    
    #url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'), 
    #url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'), 
    #url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),]
    #url(r'^LMList/new$', views.new_list, name='new_list'),    
    #url(r'^LMList/(\d+)/$', views.view_list, name='view_item'),
    #url(r'^LMList/next_list$', views.next_list, name='next_list'),  
    #url(r'^LMList/third$', views.third_list, name='third_list'),  
    #url(r'^LMList/fourth$', views.fourth_list, name='fourth_list'), 
    #url(r'^LMList/confirmation$', views.confirmation_list, name='confirmation_list'),
    #url(r'^LMList/contact$', views.contact_list, name='contact_list'), 
    #url(r'^LMList/(\d+)/add_item$', views.add_item, name='add_item'),
    

