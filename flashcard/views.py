from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flashcard = context['flashcard']
        flashcards = Flashcard.objects.all()

        current_index = list(flashcards).index(flashcard)

        previous_flashcard = None
        next_flashcard = None

        if current_index > 0:
            previous_flashcard = flashcards[current_index - 1]
        if current_index < len(flashcards) - 1:
            next_flashcard = flashcards[current_index + 1]

        context['previous_flashcard'] = previous_flashcard
        context['next_flashcard'] = next_flashcard

        return context