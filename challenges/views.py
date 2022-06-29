from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges_dic = {
    "january":"January view",
    "february":"february view",
    "march":"march view",
    "april":"april view",
    "may":"may view",
    "june":"june view",
    "july":"july view",
    "august":"august view",
    "spetember":"september view",
    "october":"october view",
    "november":"november view",
    "december":None}

#Simple /challenge form

def index(request):
   # list_items = ""
    months_list = list(monthly_challenges_dic.keys())

 #   for month in months_list:
 #       capitalized_month = month.capitalize()
 #       month_path = reverse("monthly-challenge",args=[month])
 #       list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"


 #  response_data = f"<ul>{list_items}</ul>"
 #   return HttpResponse(response_data)

# Monthly challenge by using month as a String Value
    return render(request,"challenges/index.html",{
        "months":months_list
    })
def monthly_challenges(request,month):
   # try:
        challenges_text = monthly_challenges_dic[month]
        return render(request,"challenges/challenge.html",{
            "text":challenges_text,
            "month_html":month
        })
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
    #except:
     #   return HttpResponseNotFound("This month is not supported")

# Monthly challenge by using month as a Numeric Value


def monthly_challenges_by_number(requets,month):
    months = list(monthly_challenges_dic.keys())
    if month > len(months):
        return HttpResponseNotFound("INVALID MONTH")
    redirect_month = months[month-1]
    redirectPath = reverse("monthly-challenge",args=[redirect_month])
    #return HttpResponseRedirect("/challenges/"+redirect_month)
    return HttpResponseRedirect(redirectPath)