from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
# from django.template import loader

from .models import Question

# from django.http import Http404
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]  #order_by y filteri nman e, gnum e baza berum e bolor parametrern u asuma sortavori 
#     # -pub_date" sortavorum e nvazman kargov
#     output = "<br>".join([q.question_text for q in latest_question_list])  #<br>-n htmpl-ov nr toxum greln e
#     return HttpResponse(output)
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("jacob/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "jacob/index.html", context)

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "jacob/detail.html", {"question": question})


# tokosi nshany zut dinamik string grelu sintax e 
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "jacob/results.html", {"question": question})

def vote(request, question_id):
    
    return HttpResponse("You're voting on question %s." % question_id)
    