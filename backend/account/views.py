from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .models import Account
import json
from django.utils import timezone
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import bcrypt
import jwt
from backend.settings import SECRET_KEY

# Create your views here.


@csrf_exempt
def index(request):
    data = json.load(request)
    accountCheck = Account.objects.filter(email=data["email"])
    # 회원가입
    if request.method == "POST":
        if accountCheck.exists():
            return JsonResponse('이미 가입 이력이 존재합니다', safe=False)

        password = data["password"].encode('utf-8')
        passwordCrypt = bcrypt.hashpw(password, bcrypt.gensalt())
        passwordCrypt = passwordCrypt.decode('utf-8')
        newAccount = Account(
            email=data["email"], password=passwordCrypt)
        newAccount.save()
        token = jwt.encode({'email': newAccount.email, 'exp': timezone.now()+timezone.timedelta(days=7)},
                           SECRET_KEY, algorithm="HS256")
        result = JsonResponse(model_to_dict(
            newAccount, fields=('email')), safe=False)
        result.set_cookie('token', token)
        return result

    # 로그인
    if request.method == "GET":
        if accountCheck.exists():
            account = Account.objects.get(email=data["email"])
            if bcrypt.checkpw(data["password"].encode('utf-8'), account.password.encode('utf-8')):
                token = jwt.encode({'email': account.email, 'exp': timezone.now(
                )+timezone.timedelta(days=7)}, SECRET_KEY, algorithm="HS256")
                result = JsonResponse(model_to_dict(
                    account, fields=("email")), safe=False)
                result.set_cookie('token', token)
                return result

            return JsonResponse('비밀번호가 일치하지 않습니다', safe=False)

        return JsonResponse('계정이 존재하지 않습니다', safe=False)
    # 회원 수정
    if request.method == "PATCH":
        return JsonResponse(request)

    # 회원탈퇴
    if request.method == "DELETE":
        return HttpResponse(request)


@csrf_exempt
def tokenCheck(request):
    token = request.COOKIES["token"]
    userTokenInfo = jwt.decode(token, SECRET_KEY, algorithms="HS256")
    if Account.objects.filter(email=userTokenInfo["email"]).exists():
        result = JsonResponse("검증된 사용자", safe=False)
        return result
    return JsonResponse("미검증 사용자", safe=False)
