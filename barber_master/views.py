from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
from . import models
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def form(request):
    # the form for adding info about master
    form_for_master = forms.MasterForm
    context = {
        'form_for_master': form_for_master
    }
    return render(request, 'form_master.html', context)


@login_required
def add_master(request):
    # adding info about master to
    add_form = forms.MasterForm(request.POST, request.FILES)
    add_form.instance.user = request.user
    if request.method == "POST" and add_form.is_valid():
        data = add_form.cleaned_data
        add_form.save()
        print(data['masters_name'])
        return HttpResponseRedirect("/barber_master/set_time_for_haircut/", 'Master added')


def time_for_haircut(request):
    form_time_for_haircut_man = forms.TimeForHaircutManForm
    form_time_for_haircut_woman = forms.TimeForHaircutWomanForm
    # current_master = models.Masters.objects.filter(user=request.user)
    if models.Masters.objects.filter(user=request.user, man_master=True, woman_master=False):
        context = {'form_time_for_haircut_man': form_time_for_haircut_man}
        return render(request, 'time_for_haircut.html', context)
    if models.Masters.objects.filter(user=request.user, man_master=False, woman_master=True):
        context = {'form_time_for_haircut_woman': form_time_for_haircut_woman}
        return render(request, 'time_for_haircut.html', context)
    if models.Masters.objects.filter(user=request.user, man_master=True, woman_master=True):
        context = {'form_time_for_haircut_man': form_time_for_haircut_man,
                   'form_time_for_haircut_woman': form_time_for_haircut_woman}
        return render(request, 'time_for_haircut.html', context)


def add_time_for_haircut(request):
    add_form_time_for_haircut_man = forms.TimeForHaircutManForm(request.POST)
    add_form_time_for_haircut_woman = forms.TimeForHaircutWomanForm(request.POST)
    add_form_time_for_haircut_man.instance.user = request.user
    add_form_time_for_haircut_woman.instance.user = request.user
    if add_form_time_for_haircut_woman and add_form_time_for_haircut_man:
        if request.method == "POST" and add_form_time_for_haircut_woman.is_valid() \
                and add_form_time_for_haircut_man.is_valid():
            add_form_time_for_haircut_woman.save()
            add_form_time_for_haircut_man.save()
            return HttpResponseRedirect("/barber_master/")
    if add_form_time_for_haircut_woman:
        if request.method == "POST" and add_form_time_for_haircut_woman.is_valid():
            add_form_time_for_haircut_woman.save()
            return HttpResponseRedirect("/barber_master/")
    if add_form_time_for_haircut_man:
        #if request.method == "POST" and not add_form_time_for_haircut_man.is_valid():
        #    return HttpResponse('invalid')
        #add_form_time_for_haircut_man.full_clean()
        if request.method == "POST" and add_form_time_for_haircut_man.is_valid():
            add_form_time_for_haircut_man.save()
            return HttpResponseRedirect("/barber_master/")
    else:
        return HttpResponse('Something goes wrong')


def current_master_info(request):
    current_master = models.Masters.objects.filter(user=request.user)
    ctx = {}
    ctx['current_master'] = current_master
    return render(request, 'current_master.html', ctx)


def change_masters_info(request):
    template_name = 'change_masters_info.html'
    changing = get_object_or_404(models.Masters, user_id=request.user)
    if request.method == 'POST':
        form1 = forms.MasterForm(request.POST, instance=changing)
        if form1.is_valid():
            changing = form1.save(commit=False)
            changing.save()
            return HttpResponseRedirect("/barber_master/", 'Master edited')
    else:
        form1 = forms.MasterForm(instance=changing)
    ctx = {'form1': form1}
    return render(request, template_name, ctx)


class MainView(TemplateView):
    template_name = 'main_master.html'

    def get(self, request):
        if request.user.is_authenticated:
            masters = models.Masters.objects.all()
            ctx = {}
            ctx['masters'] = masters
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/barber_master/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        check_existing_info = models.Masters.objects.filter(user_id=self.request.user)
        if check_existing_info:
            self.success_url = "/barber_master/"
            return str(self.success_url)
        else:
            self.success_url = "/barber_master/master_info/"
            return str(self.success_url)  # success_url may be lazy

    def form_valid(self, form):
        # получаем обьект пользователя на основе введенных в форму данных
        self.user = form.get_user()
        # выполняем аутентификацию пользователя
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/barber_master/")
