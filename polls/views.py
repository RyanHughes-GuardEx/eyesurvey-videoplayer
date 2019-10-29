from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Responses, Question

def vote(request, user_id):
    response = Responses()
    try:
        question = get_object_or_404(Question, pk=1)  # only 1 question
        recorded_choice = response.create_response(user=user_id, nystagmus=request.POST['choice'], video='-1', question=question)
    except (KeyError, Responses.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'index.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        recorded_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(user_id,)))


def results(request, user_id):
    response = "Here is the current user: %s."
    return HttpResponse(response % user_id)
