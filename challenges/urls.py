from django.urls import path
from . import views

urlpatterns = [
    path("",views.index), #means /challenges/ simple page
    path("<int:month>/",views.monthly_challenges_by_number), #used for numeric month value
    path("<str:month>/",views.monthly_challenges,name="monthly-challenge") #used for string month value
]


