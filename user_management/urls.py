from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('', RedirectView.as_view(url='/accounts/login/'), name='home'),
    path('__debug__/', include('debug_toolbar.urls')),
]