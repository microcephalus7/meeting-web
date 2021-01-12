from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .models import Post, Comment
import json
from django.utils import timezone
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):

    # 글 전체 list
    if request.method == "GET":
        posts = Post.objects.all()
        postList = serializers.serialize('json', posts)
        return HttpResponse(postList, content_type='application/json')

    # 글 쓰기
    if request.method == 'POST':
        data = json.load(request)
        post = Post(title=data["title"],
                    body=data["body"], pubDate=timezone.now())
        post.save()
        result = JsonResponse(model_to_dict(post))
        return result


@csrf_exempt
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = json.load(request)

    # 글 디테일
    if request.method == "GET":
        obj = model_to_dict(post)
        comments = [model_to_dict(i) for i in post.comment_set.all()]
        obj["comments"] = comments
        obj["commentsLength"] = post.comment_set.count()

        result = JsonResponse(obj, safe=False)
        return result

    # 글 수정
    if request.method == "PATCH":
        post.title = data["title"]
        post.body = data["body"]
        post.save()
        result = JsonResponse(model_to_dict(post))
        return result
    if request.method == "DELETE":
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return JsonResponse(model_to_dict(post))


# 댓글 쓰기


def commentPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = json.load(request)
    comment = model_to_dict(post.comment_set.create(
        body=data["body"], pubDate=timezone.now()))
    return JsonResponse(comment)


# 댓글 수정


def commentModify(request, pk, comment_id,):
    data = json.load(request)
    comment = get_object_or_404(comment, pk=comment_id)
    comment.body = data["body"]
    comment.save()
    result = JsonResponse(model_to_dict(comment))
    return result

# 댓글 삭제


def commentDelete(request, pk, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return JsonResponse(model_to_dict(comment))
