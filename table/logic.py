from django.contrib.auth import authenticate, login
from rest_framework import request

from table.models import Record


def get_all_records():
    return Record.objects.all()


def login_user(username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return True
    else:
        return False
