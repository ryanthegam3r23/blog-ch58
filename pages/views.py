from django.views.generic import TemplateView

# Create your views here.
# Class based views
class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

#Function-based views