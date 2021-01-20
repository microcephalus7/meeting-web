from django.shortcuts import get_object_or_404
import jwt
import json
from django.http import JsonResponse, request
from django.core.exceptions import ObjectDoesNotExist
from backend.settings import SECRET_KEY
from account.models import Account, Profile


def tokenCheckDecorator(func):
    def wrapper(request, *args, **kwargs):
        try:
            token = request.COOKIES["token"]
        except:
            return JsonResponse("토큰값이 없습니다", status=400, safe=False)
        try:
            token = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            account = Account.objects.get(email=token["email"])
            request.account = account
        except jwt.exeptions.DecodeError:
            return JsonResponse('유효하지 않은 토큰', status=400)
        except Account.DoesNotExist:
            return JsonResponse('해당 유저가 없습니다', status=400)
        return func(request, *args, **kwargs)
    return wrapper


def profileCheckDecorator(func):
    def wrapper(request, *args, **kwargs):
        account = request.account
        try:
            profile = Profile.objects.get(Profile, account=account)
            request.profile = profile
        except Profile.DoesNotExist:
            return JsonResponse("해당 유저가 프로필을 생성하지 않았습니다", status=400)
        return func(request, *args, **kwargs)

    return wrapper
