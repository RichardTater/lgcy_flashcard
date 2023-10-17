from django.contrib import admin
from .models import Flashcard

# Register your models here.
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'answer_text')

admin.site.register(Flashcard, FlashcardAdmin)


