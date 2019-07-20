from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class NoteListView(LoginRequiredMixin, ListView):
    model = models.Note
    template_name = 'note_list.html'
    login_url = 'login'


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = models.Note
    template_name = 'note_detail.html'
    login_url = 'login'


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Note
    fields = ['title', 'content', 'favourite',]
    template_name = 'note_edit.html'
    login_url = 'login'

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Note
    template_name = 'note_delete.html'
    success_url = reverse_lazy('note_list')
    login_url = 'login'


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = models.Note
    template_name = 'note_new.html'
    fields = ['title', 'content', 'author', 'favourite', 'category']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
