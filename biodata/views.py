from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


def first_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'biodata/first_page.html', {'posts': posts})
def second_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'biodata/second_page.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('second_page', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'biodata/page_edit.html', {'form': form})
def page_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('second_page', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'biodata/page_edit.html', {'form': form})


def niit(request):
    return render(request,"biodata/niit.html")

def bca(request):
    return render(request,"biodata/bca.html")

def hse(request):
    return render(request,"biodata/hse.html")

def sslc(request):
    return render(request,"biodata/sslc.html")

def contact(request):
    return render(request,"biodata/contact.html")