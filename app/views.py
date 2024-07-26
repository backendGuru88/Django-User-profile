# from django.shortcuts import render, redirect
# from .forms import SignUpForm
# from django.contrib.auth import authenticate, login

# # Create your views here.
# def index(request):
#     username = request.user.username if request.user.is_authenticated else None
#     return render(request, 'home.html', {'username': username})

# def signup(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password1")
#             form.save()
#             new_user = authenticate(username=username, password=password)
#             if new_user is not None:
#                 login(request, new_user)
#                 return redirect("index")
#             else:
#                 print("Authentication failed")
#         else:
#             print("Form is not valid")
#             print(form.errors)  # Print form errors to debug why form is not valid
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


# views.py
# views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# views.py
def index(request):
    if request.user.is_authenticated:
        profile_form = ProfileForm(instance=request.user.profile)

        if request.method == 'POST':
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('index')

        return render(request, 'home.html', {
            'username': request.user.username,
            'profile_form': profile_form,
        })
    else:
        return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("index")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
