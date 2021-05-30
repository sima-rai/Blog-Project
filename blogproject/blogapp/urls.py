from django.urls import path
from .views import *

app_name = 'blogapp'


urlpatterns = [

    path("", HomeView.as_view(), name="home"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("blog/create/", BlogCreateView.as_view(), name="blogcreate"),
    path("blog/list/", BlogListView.as_view(), name="bloglist"),

]