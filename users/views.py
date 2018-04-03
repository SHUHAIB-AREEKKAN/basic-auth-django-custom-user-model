from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class=CustomUserCreationForm
    succes_url=reverse_lazy('login')
    template_name = 'signup.html'

# Create your views here.
