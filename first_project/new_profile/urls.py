from django.urls import path
from new_profile import views

urlpatterns = [
	path('',views.new_user,name="new_profile"),
	
	
]