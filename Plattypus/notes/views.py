from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, ListView

from Plattypus.notes.forms import NotesForm
from Plattypus.notes.models import Notes


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        notes = Notes.objects.filter(recipient=user).order_by('-timestamp')
        context['user'] = user
        context['notes'] = notes
        return context


class UserNoteCreateView(LoginRequiredMixin, CreateView):
    form_class = NotesForm
    template_name = 'notes/create_note.html'
    success_url = reverse_lazy('all_notes')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = Notes(sender=self.request.user)
        return kwargs

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)


class NoteDetailsView(LoginRequiredMixin, DetailView):
    model = Notes
    template_name = 'notes/detail_note.html'
    context_object_name = 'note'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        return context


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    template_name = 'notes/delete_note.html'
    success_url = reverse_lazy('all_notes')
    context_object_name = 'note'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        return context
