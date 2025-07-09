import requests
import json
from django.shortcuts import render, redirect
from django.db import connection

def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM users WHERE username=%s AND password=%s",
                [username, password]
            )
            user = cursor.fetchone()

        if user:
            # Notify Flask (Master App) of login success
            login_data = {
                "username": username
            }
            try:
                requests.post(
                    "http://localhost:5001/store-login",
                    data=json.dumps(login_data),
                    headers={"Content-Type": "application/json"}
                )
            except Exception as e:
                print("Failed to notify Flask Master App:", e)

            # return redirect('/success')
            return redirect(f'http://localhost:8082/vote?username={username}')
        else:
            error = "Invalid username or password"

    return render(request, "login.html", {"error": error})
