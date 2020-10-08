"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from new_profile import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('new_profile/',include('new_profile.urls')),
    path('',views.dashbord,name="dashbord"),
    path('members/',views.members,name="members"),
    path('members/member/<int:pk>',views.view_profile,name="member"),
    path('members/member/<int:pk>/clear_due',views.clear_due,name="clear_due"),
    path('members/member/receipt/<int:pk>',views.update_receipt,name="receipt"),
    path('members/member/payment/<int:pk>',views.payment,name="payment"),
    path('members/member/delete/<int:pk>',views.delete_receipt,name="delete_receipt"),
    path('members/delete/<int:pk>',views.delete_member,name="delete_member"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
