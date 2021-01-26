from django.urls import path

from manager.views import MyPage, RegisterView, logout_user, LoginView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", logout_user, name='logout'),
    path('', MyPage.as_view(), name='the-main-page'),
]


