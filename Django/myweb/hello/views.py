from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flight, Topic, companies, category, Questions
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        "topics": Topic.objects.all()
        }
    return render(request, "index.html",context)

def book(request):
    try:
        name = request.POST["name"]
        company = request.POST["company"]
        review = request.POST["review"]
    except KeyError:
        return "Error"
    f= Flight(destination = name, origin = company, duration = review)
    f.save()
    return HttpResponseRedirect(reverse("index"))

def contentbycompany(request):
    context = {
        "companies": companies.objects.all()
        }
    return render(request, "contentbycompany.html",context)

def categories(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    context = {
        "topic": topic,
        "categories": topic.categories.all()
    }
    return render(request, "categories_2.html",context)

def questions(request, category_id):
    print(category_id)
    Category = category.objects.get(pk=category_id)
    context={
        "category": Category,
        "questions" : Category.questions.all()
    }
    return render(request, "questions.html",context) 

def companycategories(request, company_id):
    Company = companies.objects.get(pk=company_id)
    context = {
        "topic": Company,
        "categories": Company.categories.all()
    }
    return render(request, "categories_2.html",context)
