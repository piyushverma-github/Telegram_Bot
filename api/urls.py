from django.urls import path
from .views import PublicView, ProtectedView, RegisterView, LoginView

urlpatterns = [
    path('public/', PublicView.as_view(), name='public'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]