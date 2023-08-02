def get_user(request):
    context = {}
    user = request.user
    context['user'] = user
    return context
