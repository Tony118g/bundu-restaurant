from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


def home_page(request):
    return render(request, "index.html")


def profile_page(request):

    if request.user.is_authenticated:
        f_name = request.user.first_name
        l_name = request.user.last_name
        username = request.user.username
        email_address = request.user.email

        context = {
            'f_name': f_name,
            'l_name': l_name,
            'username': username,
            'email_address': email_address,
        }
        return render(request, 'profile.html', context)
    else:
        return redirect('home')


class EditAccount(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'edit_account.html'
    fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]
    success_url = reverse_lazy('profile_page')
    success_message = 'Account successfully Updated'

    def get_queryset(self):
        query_set = User.objects.filter(id=self.request.user.id)
        return query_set
