from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, DetailView, UpdateView
from .forms import RegisterUserForm, EditProfileForm
from django.views.generic import TemplateView
from .models import PlattypusUser

UserModel = get_user_model()


class ProfileDetailsView(DetailView):
    template_name = 'account/profile-page.html'
    model = UserModel

    profile_picture = static('images/platypus.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_picture


class ProfileEditView(UpdateView):
    form_class = EditProfileForm
    model = PlattypusUser
    template_name = 'account/edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(DeleteView):
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

        pk = self.kwargs.get('pk')

        try:
            user = PlattypusUser.objects.get(pk=pk)
        except PlattypusUser.DoesNotExist:
            redirect('common/home.html')
        else:
            context['user'] = user

        return context
