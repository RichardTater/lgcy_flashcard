from django.urls import path
from . import views
from django.views.generic import TemplateView

#URLConf

app_name = "flashcard"

urlpatterns = [
    path("", views.FlashcardListView.as_view(), name="index"),
    path("<int:pk>/", views.FlashcardDetailsView.as_view(), name="answers"),
    # path("<int:pk>/", views.FlashcardDetailsView.as_view(), name="next"),
    # path("<int:pk>/", views.FlashcardDetailsView.as_view(), name="previous")
]