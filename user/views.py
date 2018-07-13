from django.views.generic import ListView, FormView

from user.forms import UserForm, UserDeleteForm
from user.models import User


class Users(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'user_list'


class UserEntryForm(FormView):
    form_class = UserForm
    template_name = 'add_user.html'
    success_url = '../users'

    def form_valid(self, form):
        _first_name = form.cleaned_data['first_name']
        _last_name = form.cleaned_data['last_name']
        User(first_name=_first_name, last_name=_last_name).save()
        return super(UserEntryForm, self).form_valid(form)


class UserDelete(FormView):
    form_class = UserDeleteForm
    template_name = 'delete_user.html'
    success_url = '../users'

    def form_valid(self, form):
        form.cleaned_data["user"].delete()
        return super(UserDelete, self).form_valid(form)
