from django.urls import path
from myapp import views
urlpatterns=[
    path('index_page/', views.index_page, name='index_page'),
    path('add_session/', views.add_session, name='add_session'),
    path('display_session/', views.display_session, name='display_session'),
    path('save_session/', views.save_session, name='save_session'),
    path('session_edit/<int:dataid>/', views.session_edit, name='session_edit'),
    path('update_session/<int:dataid>/', views.update_session, name='update_session'),
    path('delete_session/<int:dataid>/', views.delete_session, name='delete_session'),
    path('log/', views.log, name='log'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('display_blog/', views.display_blog, name='display_blog'),
    path('save_blog/', views.save_blog, name='save_blog'),
    path('blog_edit/<int:dataid>/', views.blog_edit, name='blog_edit'),
    path('update_blog/<int:dataid>/', views.update_blog, name='update_blog'),
    path('delete_blog/<int:dataid>/', views.delete_blog, name='delete_blog'),

]