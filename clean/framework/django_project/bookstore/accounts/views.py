from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from interfaces.controllers.account_controller import AccountController

controller = AccountController()

# =====================
# API VIEWS (JSON)
# =====================

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        customer = controller.register(data)
        return JsonResponse({
            "id": customer.id,
            "email": customer.email
        })

    return JsonResponse({"error": "POST required"}, status=405)


@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            customer = controller.login(data)
            return JsonResponse({
                "id": customer.id,
                "email": customer.email
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "POST required"}, status=405)


# =====================
# UI VIEWS (HTML)
# =====================

def register_page(request):
    if request.method == "POST":
        try:
            controller.register({
                "name": request.POST["name"],
                "email": request.POST["email"],
                "password": request.POST["password"],
            })
            return render(
                request,
                "accounts/register.html",
                {"message": "Register success"}
            )
        except Exception as e:
            return render(
                request,
                "accounts/register.html",
                {"message": str(e)}
            )

    return render(request, "accounts/register.html")


from django.shortcuts import render, redirect

def login_page(request):
    if request.method == "POST":
        try:
            customer = controller.login({
                "email": request.POST["email"],
                "password": request.POST["password"],
            })

            # 🔐 LƯU SESSION
            request.session["customer_id"] = customer.id
            request.session["customer_email"] = customer.email

            return redirect("/books/")
        except Exception as e:
            return render(
                request,
                "accounts/login.html",
                {"message": str(e)}
            )

    return render(request, "accounts/login.html")

def logout_page(request):
    request.session.flush()   # ❗ xóa toàn bộ session
    return redirect("/login/")