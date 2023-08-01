from django.urls import path, include

from Plattypus.notes.views import NotesListView, UserNoteCreateView, NoteDetailsView, NoteDeleteView

urlpatterns = [
    path('', NotesListView.as_view(), name='all_notes'),
    path('create/', UserNoteCreateView.as_view(), name='create_note'),
    path('<int:pk>/', include([
        path('details/', NoteDetailsView.as_view(), name='note_details'),
        path('delete/', NoteDeleteView.as_view(), name='note_delete'),
    ])),
]