from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.
class JOPSITEView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "JOPSITE"
        return context


class HomeView(JOPSITEView):
    template_name = "mish/home.html"