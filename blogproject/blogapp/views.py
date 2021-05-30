from django.views.generic import *
from django.db.models import Q
from .forms import *
from .models import*
from django.conf import settings
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            pass
        else:
            return redirect("/login")
        return super().dispatch(request, *args, **kwargs)



class HomeView(TemplateView):
    template_name = 'home.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     myList = ['leeza', 'seema', 'alish', 'sujan']
    #     if 'leeza' in myList:
    #         print("true")

    #     return context


class SignupView(FormView):
    template_name = "signup.html"
    form_class = SignupForm
    success_url = "/"

    def form_valid(self, form): #formview use garda yo formvalid chai banaunai parcha
        uname = form.cleaned_data["username"] #esle chai khali value matri limcha aru input ma huune aru tags haru lai chai elimiate gardincha...you can check by doing inspect in the field ..ani khali value matri pathaucha
        email = form.cleaned_data["email"]
        pword = form.cleaned_data["password"]

        print(uname, email, pword)
        User.objects.create_user(uname, email, pword)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        a = form.cleaned_data["username"]
        b = form.cleaned_data["password"]
        usr = authenticate(username=a, password=b)
        if usr is not None:
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"error":"Invalid username or password",
            "form":form})
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)

        return redirect("/login")


class BlogCreateView(UserRequiredMixin, CreateView):
    template_name = "blogcreate.html"
    form_class = BlogForm
    success_url = reverse_lazy("blogapp:bloglist")

    def form_valid(self, form):
        logged_in_user = self.request.user
        form.instance.author = logged_in_user
        return super().form_valid(form)


class BlogListView(ListView):
    template_name = "bloglist.html"
    queryset = Blog.objects.all()
    context_object_name = "allblogs"










