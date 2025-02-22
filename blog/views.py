from django.shortcuts import render

from django.http import HttpResponse

from .models import Post

# Create your views here.

def home(request):

    # posts = Post.objects.all()
    # #print(posts)
    
    # result = ""
    # for post in posts:
    #     #result = result +post.title + "<br />"
    #     result += f"{post.title} - {post.content} - {post.created_at}<br>"
    #     print(result)

    # return HttpResponse(result)

    person = {
        "name":"Arafat"
    }


    return render(request,"post_list.html",person)
