# persondetails_app/views.py
from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
from .models import InterestInput
from django.contrib.auth import authenticate, login
from django.contrib import messages



def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page or wherever you want
    else:
        form = PersonForm()

    return render(request, 'create_person.html', {'form': form})


def home_page(request):
    ret_dict  = {'calculate':'calculate',
                 'person': 'person',
                 'entry':'entry',
                 }
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page or wherever you want
    else:
        form = PersonForm()

    return render(request, 'create_person.html', {'form': form})


def person_details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        person = {
            'name': name,
            'age': age,
            'email': email,
        }
        print(person)
        return render(request, 'index.html', {'person': person})
    else:
        return render(request, 'index.html')


from .forms import InterestInputForm

def calculate_interest(request):
    if request.method == 'POST':
        form = InterestInputForm(request.POST)
        if form.is_valid():
            interest_input = form.save(commit=False)
            interest_input.save()
            return redirect('interest_result', pk=interest_input.pk)
    else:
        form = InterestInputForm()

    return render(request, 'calculate_interest.html', {'form': form})

def interest_result(request, pk):
    interest_input = InterestInput.objects.get(pk=pk)
    return render(request, 'interest_result.html', {'interest_input': interest_input})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Change 'home' to your desired home page URL
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')

