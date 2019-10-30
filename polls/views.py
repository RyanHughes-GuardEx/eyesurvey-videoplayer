from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.shortcuts import render

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
        video_num = '0000000'
        return HttpResponseRedirect(reverse('polls:results', args=(user_id, video_num)))   # reverse() constructs the link for the name='results' line in polls/urls.py

def results(request, user_id, video_num):
    response = "Here is the user: {usr} and the video number is: {vid}".format(usr=user_id, vid=video_num)
    # should call utils.get_next_video() function here to redirect to the proper video
    return HttpResponse(response)
