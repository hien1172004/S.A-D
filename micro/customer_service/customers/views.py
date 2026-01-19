from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer

@api_view(['POST'])
def register(request):
    c = Customer.objects.create(
        name=request.data['name'],
        email=request.data['email'],
        password=request.data['password']
    )
    return Response({"id": c.id, "email": c.email})

@api_view(['POST'])
def login(request):
    try:
        c = Customer.objects.get(
            email=request.data['email'],
            password=request.data['password']
        )
        return Response({"id": c.id})
    except:
        return Response({"error": "Invalid"}, status=400)
