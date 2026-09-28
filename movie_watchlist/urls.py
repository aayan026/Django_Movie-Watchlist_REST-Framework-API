from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('movies/', include('movies.urls')),
    path('accounts/', include('accounts.urls')),

    # REST API
    path('api/', include('movies.api_urls')),
    path('api-auth/', include('rest_framework.urls')),
]
