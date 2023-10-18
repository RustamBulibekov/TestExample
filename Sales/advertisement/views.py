from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Advertisement, Rubric

# Create your views here.

class MyOwnListView(ListView):
    model = Advertisement
    context_object_name = 'adv'
    template_name = 'advertisement.html'


class MyOwnDetailView(DetailView):
    model = Advertisement

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rubric'] = Rubric.objects.all()


