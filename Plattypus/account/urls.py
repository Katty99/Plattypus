from django.urls import path, include

from Plattypus.account.views import ProfileDetailsView, ProfileEditView, ProfileCreateView, ProfileLoginView, \
    ProfileDeleteView, DashboardView, ProfileLogoutView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='profile_create'),
    path('login/', ProfileLoginView.as_view(), name='profile_login'),
    path('logout/', ProfileLogoutView.as_view(), name='profile_logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('<int:pk>/', include([
        path('details/', ProfileDetailsView.as_view(), name='profile_details'),
        path('edit/', ProfileEditView.as_view(), name='profile_edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    ]))
]