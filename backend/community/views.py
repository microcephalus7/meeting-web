from django.http import HttpResponse, JsonResponse
from .models import Post
import json

# 글 전체 list


def index(request):
    postList = Post.objects.all()
    data = list(postList.values())
    data2 = list(map(lambda x: {"title": x["title"], "body": x["body"]}, data))
    result = JsonResponse(data2, safe=False)
    return result

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
