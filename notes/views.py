from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin


from django.template.context_processors import csrf
from django.shortcuts import render

from . import models
from django.db.models import Q


def note_list(request):
    if not request.user.is_active:
        return HttpResponseRedirect(reverse('login'))
    else:
        queryset_list = models.Note.objects.filter(user=request.user)
        context = {}
        context.update(csrf(request))

        filter_name = request.POST.get('filter')
        sort_name = request.POST.get('sort')
        query = request.POST.get('query')


        category_list = []
        date_list = []
        for note in queryset_list:
            if note.category not in category_list:
                category_list.append(note.category)
        for note in queryset_list:
            if note.publish not in date_list:
                date_list.append(note.publish)

        if sort_name:
            queryset_list = queryset_list.order_by(sort_name)

        if filter_name:
            if filter_name == "all":
                queryset_list = queryset_list.all()
            elif filter_name == "favourite":
                queryset_list = queryset_list.filter(favourite=True)
            elif filter_name[0] == "cat":
                queryset_list = queryset_list.filter(category__name=filter_name[1:])
            else:
                queryset_list = queryset_list.filter(publish=filter_name)

        if query:
            queryset_list = queryset_list.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()


        page_request_var = 'page'
        context = {
            "query": query,
            "cat_list": category_list,
            "date_list": date_list,
            "object_list": queryset_list,
            "sort": sort_name,
            "filter": filter_name,
            "page_request_var": page_request_var
        }
        return render(request, "note_list.html", context)


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
    fields = ['title', 'content', 'user', 'favourite', 'category']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
