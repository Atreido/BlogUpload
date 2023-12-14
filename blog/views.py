from django.contrib.auth.decorators import login_required
from django.db.models import Q  # для нескольких запросов
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Post, Cathegories, Comments
from .forms import PostForm, AddComment
def get_categories():
    all= Cathegories.objects.all()
    count = all.count()
    return {'cat1': all[:count / 2 + count % 2],'cat2': all[count / 2 + count % 2:]}

def index(request):
   posts = Post.objects.all().order_by("-published_date")
   # categories = Cathegories.objects.all()
   # context = {"posts": posts, "categories": categories}
   context = {"posts": posts}
   context.update(get_categories())


   # postid = Post.object.get(pk=1) #primary key
   # context = {"posts": posts, "postid":postid }

   # post = Post.objects.filter(title__icontains="python") #filtred
   # context = {"posts": post}

   # post = Post.objects.filter(category__name__exact="Python")  # filtred category__name__iexact і = без учета регистра
   # context = {"posts": post}

   # post = Post.objects.filter(published_date__day="28") #filtred by date
   # context = {"posts": post}

   return render(request, 'blog/index.html', context=context)

# post without form
#  def post(request, id=None): # id=None - значение по умолчанию
#     post = get_object_or_404(Post, title=id) #import function, filter by primary key
#     context = {"post": post}
#     context.update(get_categories())
#     return render(request, 'blog/post.html', context=context)

def post(request, id=None): # id=None - значение по умолчанию
    posted = get_object_or_404(Post, title=id) #import function, filter by primary key
    comments = Comments.objects.all().order_by("-publish_date")
    form = AddComment()
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.publish_date = timezone.now()
            comment.user_id = posted.user_id
            comment.posted_id = posted.id #posted
            comment.save()
            return post(request)

    context = {"post": posted, "form": form, "comments": comments}
    context.update(get_categories())
    return render(request, 'blog/post.html', context=context)



def about(request):
    context = {   }
    return render(request, 'blog/about.html', context=context)


def services(request):
    context = {   }
    return render(request, 'blog/services.html', context=context)


def contacts(request):
    context = {   }
    return render(request, 'blog/contact.html', context=context)


def category(request, name=None):
    c = get_object_or_404(Cathegories, name=name)
    posts = Post.objects.filter(category=c).order_by("-published_date")
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context=context)


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query)).order_by("-published_date")
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context=context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.published_date = timezone.now()
            newpost.user = request.user
            newpost.save()
            return index(request)

    form = PostForm()
    context = {"form": form}
    context.update(get_categories())
    return render(request, 'blog/create.html', context=context)


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'blog/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'blog/register.html', {'form': form})

