from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DeleteView, CreateView
from django.http import HttpResponseRedirect
from .forms import AccountForm, DeleteAccountForm, LoginForm
from .models import Account
from django.views.generic import TemplateView



def get_account(id):
    account = Account.objects.get(pk=id)
    return account


class ProfileDetailsView(View):
    def get(self, request, pk):
        account = get_account(pk)
        context = {'account': account}
        return render(request, template_name='account/profile-page.html', context=context)


class ProfileEditView(View):
    def get(self, request, pk):
        account = get_account(pk)
        context = {'account': account}
        return render(request, template_name='account/edit-profile.html', context=context)


class ProfileDeleteView(DeleteView):
    model = Account
    template_name = 'account/delete-profile.html'  # Replace with your actual template name
    success_url = reverse_lazy('index')  # Replace 'home' with your desired success URL name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deletion_form'] = DeleteAccountForm(instance=self.object)
        return context

    def delete(self, request, *args, **kwargs):
        account = self.get_object()
        account.delete()
        # Perform any additional actions here, like logging out the user or sending a confirmation email
        return redirect(self.success_url())


class ProfileCreateView(CreateView):
    template_name = 'account/register-page.html'
    form_class = AccountForm
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
