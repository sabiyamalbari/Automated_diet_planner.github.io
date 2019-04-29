
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('diets.urls')),
    path('admin/', admin.site.urls),
    #path('admin/', include('django.contrib.auth.urls')), # new
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    ]