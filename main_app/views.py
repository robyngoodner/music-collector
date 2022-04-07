from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

songs = [
    Song("Radioactive", "Imagine Dragons"),
    Song("Yellow", "Coldplay")
]

class Song_List(TemplateView):
    template_name = 'song_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["songs"] = songs
        return context