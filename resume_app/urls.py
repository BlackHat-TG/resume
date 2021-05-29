from django.urls import path
from . import views
from resume_app import views

urlpatterns = [
	path('',views.home,name='home'),
	path('basic',views.basic),
	path('login',views.login),
	path('candidate',views.candidate),
	path('basic_info',views.basic_info),
	path('select_post',views.select_post),
	path('upload_cv',views.upload_cv),
	path('technical_info',views.technical_info),
	path('success',views.success),
]