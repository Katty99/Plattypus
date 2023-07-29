from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, template_name='common/index.html')


class AboutView(View):
    def get(self, request):
        return render(request, template_name='common/about-page.html')