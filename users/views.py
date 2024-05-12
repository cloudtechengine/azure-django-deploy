from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserRegistrationForm, UserUpdateForm,ProfileUpdateForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login_page')
            # return redirect('home_page')
        else:
            username = request.POST.get('username')
            messages.warning(request, f'Account not created for {username}')
            return redirect('register_page')
    else:
            form = UserRegistrationForm()
            context = {'form': form}
            return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login_page')



'''
@login_required(login_url='/user/login')
def profile(request):
    return render(request,'users/profile.html')
'''


@login_required(login_url='/user/login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(
            request.POST, instance=request.user
        )
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfuully!')
            return redirect('profile_page')
        else:
            messages.warning(request, f'Your account not updated successfuully!')
            return redirect('profile_page')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'users/profile.html', context)






