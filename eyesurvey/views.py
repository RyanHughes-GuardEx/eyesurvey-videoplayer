from django.shortcuts import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect('/index.html/')
