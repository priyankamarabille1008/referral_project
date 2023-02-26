from django.shortcuts import render, redirect
from referral.forms import SignupForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data['referral_code']:
                referrer = User.objects.filter(referral_code=form.cleaned_data['referral_code']).first()
                if referrer:
                    user.referrer = referrer
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    referrals = User.objects.filter(referrer=user)
    num_referrals = referrals.count()
    return render(request, 'dashboard.html', {'user': user, 'num_referrals': num_referrals})
