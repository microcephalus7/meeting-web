from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .models import Account
import json
from django.utils import timezone
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == "POST":
        return HttpResponse(request)
