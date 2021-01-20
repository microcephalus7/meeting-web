from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .models import Account, Profile
import json
from django.utils import timezone
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import bcrypt
import jwt
from backend.settings import SECRET_KEY
from core.utils import tokenCheckDecorator

# Create your views here.


@csrf_exempt
def index(request):
    try:
        requestData = json.load(request)
    except:
        return JsonResponse("규격에 맞는 데이터를 넣어주세요", safe=False)

    accountCheck = Account.objects.filter(email=requestData["email"])
    # 회원가입
    if request.method == "POST":
        if accountCheck.exists():
            return JsonResponse('이미 가입 이력이 존재합니다', safe=False)

        password = requestData["password"].encode('utf-8')
        passwordCrypt = bcrypt.hashpw(password, bcrypt.gensalt())
        passwordCrypt = passwordCrypt.decode('utf-8')
        newAccount = Account(
            email=requestData["email"], password=passwordCrypt)
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
            account = Account.objects.get(email=requestData["email"])
            if bcrypt.checkpw(requestData["password"].encode('utf-8'), account.password.encode('utf-8')):
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
        empty = None
        result = JsonResponse("token delete", safe=False)
        result.set_cookie('token', empty)
        return result

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


# 프로필 관리
@csrf_exempt
@tokenCheckDecorator
def profile(request):

    account = request.account
    try:
        requestData = json.load(request)
    except:
        return JsonResponse("규격에 맞는 데이터를 넣어주세요", safe=False)
    if request.method == "GET":
        accountProfile = get_object_or_404(Profile, account=account)
        result = model_to_dict(accountProfile)
        jsonResult = JsonResponse(result, safe=False)
        return jsonResult
    if request.method == "POST":
        newProfile = Profile(username=requestData["username"], phoneNumber=int(
            requestData["phoneNumber"]), male=requestData["male"], birthday=requestData["birthday"], latitude=requestData["latitude"], longitude=requestData["longitude"],
            account=account)
        newProfile.save()
        newProfile = model_to_dict(newProfile)
        result = JsonResponse(newProfile, safe=False)
        return result
    if request.method == "PATCH":
        accountProfile = get_object_or_404(Profile, account=account)
        requestKey = requestData.keys()
        if not requestKey:
            return JsonResponse("request 객체가 비었습니다", safe=False)
        return JsonResponse("request 확인", safe=False)
    if request.method == "DELETE":
        return request
