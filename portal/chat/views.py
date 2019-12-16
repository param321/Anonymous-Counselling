from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from chat import models
from .forms import Counsellorform
from .forms import Counselloreditform
from .forms import Message
from .models import messages


class SignUpView(CreateView):
    form_class = Counsellorform
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Update(LoginRequiredMixin, CreateView):
    form_class = Counselloreditform
    success_url = reverse_lazy('home')
    template_name = 'update.html'


def Chat(request):

    # print(settings.AUTH_USER_MODEL)
    if request.method == 'POST':
        form = Message(request.POST)
        msg = form.save(commit=False)
        if settings.AUTH_USER_MODEL == "chat.counsellor":  # correct this
            msg.message_from = 1
        else:
            msg.message_from = 0
        msg.save()
        form = Message(instance=messages)
        m1 = messages.objects.all().filter(message_from=0)
        m2 = messages.objects.all().filter(message_from=1)

        return render(request, 'chat.html', context={'m1': m1, 'm2': m2, 'form': form},)
    else:
        form = Message(instance=messages)
        args = {'form': form}
        return render(request, 'chat.html', args)
