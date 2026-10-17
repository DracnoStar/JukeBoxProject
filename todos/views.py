from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import PersonForm
# Create your views here.
def hello_world_view(request):
    return HttpResponse('Hello World')

def hello_python_view(request):
    return HttpResponse('Hello Python')

def hello_html_view(request):
    return render(request, 'todos/hello.html')

def hello_path(request, name):
    return HttpResponse(f'Hello {name}!')

def hello_add(request, num1, num2):
    return HttpResponse(f'Sum is {num1 + num2}!')

def hello_multiply(request, num1, num2):
    product = num1*num2
    return HttpResponse(f'Product is {product}!')

def hello_query(request):
    return HttpResponse(f'Your query was {request.GET.get("q")}')

def special_view(request):
    return redirect('hello_html')

def post_example(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            job = form.cleaned_data['job']

            return HttpResponse(f'You Posted: {name}, {age}, {job}')

    else:
        return HttpResponseNotAllowed(['POST'])


def submit_example(request):
    return render(request, 'todos/submit.html')    

def submit_django_form(request):
    form = PersonForm()
    return render(request, 'todos/submit_django_form.html', {'form': form})    

def template_view(request):
    context = {
        "name": "Mike",
        "age" : 30,
        "skills": ["Python", "SQL"]
    }
    return render(request, 'todos/template_demo.html', context)