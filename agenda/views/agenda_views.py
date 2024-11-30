from agenda.models import Contact
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView


class ListViewBase(LoginRequiredMixin, ListView):
    login_url = 'authors:login_author'
    template_name = 'agenda/pages/home.html'
    model = Contact
    paginate_by = 2
    context_object_name = 'contacts'
    paginator_class = Paginator

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        queryset = queryset.filter(
            user=self.request.user
        ).order_by('-id')

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Home',
            'user': self.request.user
        })

        return context


class ListViewHome(LoginRequiredMixin, ListViewBase):
    login_url = 'authors:login_author'
    template_name = 'agenda/pages/home.html'


class ListViewSearch(LoginRequiredMixin, ListViewBase):
    login_url = 'authors:login_author'
    template_name = 'agenda/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        search_term = self.request.GET.get('q', '').strip()

        queryset = queryset.filter(
            Q(user=self.request.user) & (
                Q(id__icontains=search_term) |
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term) |
                Q(phone__icontains=search_term) |
                Q(email__icontains=search_term)
            )
        ).order_by('-id')

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('q', '').strip()

        context.update({
            'search_term': search_term,
            'title': 'Search'
        })

        return context


class DetalViewContact(LoginRequiredMixin, DetailView):
    login_url = 'authors:login_author'
    template_name = 'agenda/pages/view_contact.html'
    model = Contact
    context_object_name = 'contact'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        queryset = queryset.filter(
            pk=self.kwargs.get('pk'),
            user=self.request.user
        )

        return queryset
