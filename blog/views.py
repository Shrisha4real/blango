from django.shortcuts import render , get_object_or_404
from .models import Posts
# Create your views here.
def index(request):
    all_Post = Posts.objects.all()
    return render(request , "blog/index.html" , {"posts":all_Post , "title":"Posts"})

def post_detail(request , slug):
    post = get_object_or_404(Posts , slug=slug)
    # print(f"size of the POsts is {len(post)}")
    return render(request , "blog/post-detail.html", {"post": post})