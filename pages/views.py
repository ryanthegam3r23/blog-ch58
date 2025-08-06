from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
# Class based views
class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

#Function-based views
#def about_view(request):
 #   return render(request, "pages/about.html")