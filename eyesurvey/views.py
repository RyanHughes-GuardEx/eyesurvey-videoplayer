from django.shortcuts import HttpResponseRedirect
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, render

from polls.models import Responses, Question

def detail(request):
    question_id = 1
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'index.html', {'question': question})

#class ResponseView(CreateView):
#    response = Responses
#    fields = ('user', 'nystagmus_present', 'video_link')

def index(request):
    return HttpResponseRedirect('/polls/wq123/vote/')

