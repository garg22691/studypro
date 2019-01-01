from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book", views.book, name = "book"),
    path("contentbycompany", views.contentbycompany, name = "contentbycompany"),
    path("<int:topic_id>", views.categories, name = "categories"),
    path("topic/<int:category_id>", views.questions, name = "questions"),
    path("company/<int:company_id>", views.companycategories, name = "companycategories")
]