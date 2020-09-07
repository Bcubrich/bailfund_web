from django.urls import path
from signup.views import SignUpView, ActivateAccount

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='all'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]