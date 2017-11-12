from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, View
from .forms import UserRegForm

class IndexView(ListView):
    template_name = 'UserPoll/index.html'
    def get_queryset(self):
        pass
        

class UserRegView(View):
    form_class = UserRegForm 
    template_name = 'UserPoll/register.html'
    #!CREATE TEMPLATE

    def get(self, req):
        form = self.form_class(None)
        return render(req, self.template_name, {'form':form})
    
    def post(self, req):
        form = self.form_class(req.post)
        if form.is_valid():
            user = form.save(commit = False)
            
            #Cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.username = username
            user.set_password(password)
            #Commit&Authenticate
            user.save()
            user = authenticate(username = username, password = password)
            
            if user is not None and user.is_active:
                login(req, user)
                return redirect('UserPoll:loggedin')#?
