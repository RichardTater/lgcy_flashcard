from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView

from .models import Flashcard

# Create your views here.
# Request -> Response
# Request handler
# Action

class FlashcardListView(ListView):
    model = Flashcard
    template_name = "flashcard.html"
    context_object_name = "flashcard_list"

class FlashcardDetailsView(DetailView):
    model = Flashcard
    template_name = "flashcard_details.html"