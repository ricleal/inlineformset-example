from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from .models import Book, Author
from .forms import AuthorForm, BookFormSet, BookForm


class FormsetMixin(object):
    object = None

    def get(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def get_formset_class(self):
        return self.formset_class

    def get_formset(self, formset_class):
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {
            'instance': self.object
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return redirect(self.object.get_absolute_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class AuthorCreateView(FormsetMixin, CreateView):
    template_name = 'books/author_and_books_form.html'
    model = Author
    form_class = AuthorForm
    formset_class = BookFormSet


class AuthorUpdateView(FormsetMixin, UpdateView):
    template_name = 'books/author_and_books_form.html'
    is_update_view = True
    model = Author
    form_class = AuthorForm
    formset_class = BookFormSet


class BookList(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')

class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm

class AuthorList(ListView):

    model = Author


class AuthorDetail(DetailView):

    model = Author
