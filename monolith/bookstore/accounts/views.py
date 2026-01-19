from django.shortcuts import render, redirect
from .models import Customer

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        Customer.objects.create(
            name=name,
            email=email,
            password=password
        )
        return redirect('/login/')

    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            customer = Customer.objects.get(email=email, password=password)
            request.session['customer_id'] = customer.id
            return redirect('/books/')
        except Customer.DoesNotExist:
            return render(request, 'accounts/login.html', {'error': 'Invalid login'})

    return render(request, 'accounts/login.html')
def logout(request):
    request.session.flush()   # xoá toàn bộ session
    return redirect('/login/')