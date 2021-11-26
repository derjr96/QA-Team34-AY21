from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .token import account_activation_token


# Register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Customer')
            user.groups.add(group)

            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, f'Account created for {username}!')
            messages.success(request, 'Please confirm your email address to complete the registration')
            # return HttpResponse('Please confirm your email address to complete the registration')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        print('load login page1')
        username = request.POST['username']
        password = request.POST['password']
        account = authenticate(username=username, password=password)
        if account is not None:
            login(request, account)
            print('Account Active')
            # Redirect to index page.
            # return render(request, 'website/home.html', {'form': form})
            messages.success(request, 'Login Success')
            return redirect('rock-home')

        else:
            print('Account is not authenticated')
            # Return a 'disabled account' error message
            messages.success(request, 'Error')
            return redirect('login')
    else:
        print('load login page2')
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    # Redirect back to index page.
    messages.success(request, 'Logout Success')
    return redirect('rock-home')


# Profile view
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'profile updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


# Error 404
def error404(request, exception):
    context = {

        'title': '404'
    }
    return render(request, 'users/404.html', context)


# Activating account using email view
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        print('UID:', uid)
        user = User.objects.get(pk=uid)
        print('User id:', user.id)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        print('After None ')
    print('Before If ')
    if user is not None and account_activation_token.check_token(user, token):
        print('Inside If ')
        user.is_active = True
        user.save()
        print('Inside If, After Save ')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return render(request, 'users/email_success.html')
    else:
        # return HttpResponse('Activation link is invalid!')
        return render(request, 'users/email_fail.html')


# AboutPage
def security(request):
    return redirect('2fa')
