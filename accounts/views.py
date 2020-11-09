from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import SignupForm

# Create your views here.
class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('accounts:login')
    template_name = "accounts/signup.html"