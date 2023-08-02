from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Sum
from django.shortcuts import redirect
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, DetailView, UpdateView
from .forms import RegisterUserForm, EditProfileForm
from django.views.generic import TemplateView
from .models import PlattypusUser
from ..finances.models import Income, Expense

UserModel = get_user_model()


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'account/profile-page.html'
    model = UserModel

    profile_picture = static('images/platypus.png')


class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = EditProfileForm
    model = PlattypusUser
    template_name = 'account/edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'account/delete-profile.html'  # Replace with your actual template name
    success_url = reverse_lazy('index')  # Replace 'home' with your desired success URL name


class ProfileCreateView(CreateView):
    template_name = 'account/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("dashboard")

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class ProfileLoginView(LoginView):
    template_name = 'account/login-page.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('dashboard')


class ProfileLogoutView(LogoutView):
    next_page = reverse_lazy('profile_login')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        incomes = Income.objects.filter(user=user)
        total_incomes = incomes.aggregate(Sum('amount'))['amount__sum'] or 0

        expenses = Expense.objects.filter(user=user)
        total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

        balance = total_incomes - total_expenses

        context['user'] = user
        context['balance'] = balance

        return context
