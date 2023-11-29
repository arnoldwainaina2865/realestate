from django.contrib import admin
from django.urls import path
from estateapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name = 'register'),
    path('login/',views.login, name = 'login'),
    path('index/',views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('propertygrid/', views.propertygrid, name = 'propertygrid'),
    path('propertysingle/', views.propertysingle, name = 'propertysingle'),
    path('blog/', views.blog, name = 'bloggrid'),
    path('blogsingle/', views.blogsingle, name = 'blogsingle'),
    path('agentsgrid/', views.agentsgrid, name = 'agentsgrid'),
    path('agentsingle/', views.agentsingle, name = 'agentsingle'),
    path('contact/', views.contact, name = 'contact'),


]
