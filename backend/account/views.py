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
    data = json.load(request)
    accountCheck = Account.objects.filter(email=data["email"])
    # 회원가입
    if request.method == "POST":
        if accountCheck.exists():
            return JsonResponse('이미 가입 이력이 존재합니다', safe=False)
        else:
            newAccount = Account(
                email=data["email"], password=data["password"])
            newAccount.save()
            result = model_to_dict(newAccount, fields=('email'))
            return JsonResponse(result, safe=False)

    # 로그인
    if request.method == "GET":
        if accountCheck.exists():
            account = Account.objects.get(email=data["email"])
            if account.password == data["password"]:
                accountDict = model_to_dict(account, fields=("email"))
                return JsonResponse(accountDict, safe=False)
            else:
                return JsonResponse('비밀번호가 일치하지 않습니다', safe=False)
        else:
            return JsonResponse('계정이 존재하지 않습니다', safe=False)
    # 회원 수정
    if request.method == "PATCH":
        return HttpResponse(request)
    # 회원탈퇴
    if request.method == "DELETE":
        return HttpResponse(request)
