from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


# def index(request):
#     latest_question_list = Question.objects.order_by("pub_date")[:2]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:2]
#     output = "</br> ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


class IndexView(generic.ListView):
    template_name = 'jacob/index.html'
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("pub_date")[:2]
    

class DetailView(generic.DetailView):
    model = Question
    template_name = 'jacob/detail.html'


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})

class ResultsView(generic.DetailView): 
    model = Question
    template_name = 'jacob/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "jacob/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("jacob:results", args=(question.id,)))