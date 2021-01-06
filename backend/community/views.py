from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .models import Post
import json

# 글 전체 list


def index(request):
    postList = Post.objects.all()
    data = list(
        map(lambda x: {"title": x["title"], "body": x["body"], "id": x["id"]}, postList.values()))
    result = JsonResponse(data, safe=False)
    return result

# 글 id 별 세부


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    obj = model_to_dict(post)
    result = JsonResponse(obj, safe=False)
    return result


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
