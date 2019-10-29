from django.shortcuts import HttpResponseRedirect
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, render

from polls.models import Responses, Question

def detail(request):
    question = get_object_or_404(Question, pk=1)
    return render(request, 'index.html', {'question': question})

def index(request):
    return HttpResponseRedirect('/polls/wq123/vote/')

