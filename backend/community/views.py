from django.http import HttpResponse
from .models import Post
import json

# 글 전체 list


def index(request):
    user = json.load(request)
    return HttpResponse(json.dumps({'username': user['username']}))

# 글 id 별 세부


def detail(request):
    request

# 글 쓰기


def posting(request):
    request

# 글 수정


def postModify(request):
    request

# 글 삭제


def postDelete(request):
    request

# 댓글 쓰기


def commentPosting(request):
    request

# 댓글 수정


def commentModify(request):
    request

# 댓글 삭제


def commentDelete(request):
    request
