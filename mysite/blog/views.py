from django.core.handlers import wsgi
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from .models import Post, Comment


# def post_list(request: wsgi.WSGIRequest) -> HttpResponse:
#     post_objects = Post.published.all()
#     paginator = Paginator(post_objects, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request: wsgi.WSGIRequest, year: int, month: int, day: int,
                post: str) -> HttpResponse:
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                             publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)
    comment_form = None
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    if request.method == "GET":
        comment_form = CommentForm
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments,
                                                     'new_comment': new_comment, 'comment_form': comment_form})


def post_share(request: wsgi.WSGIRequest, post_id: int) -> HttpResponse:
    rendered_form = None
    mail_sent = False
    post = get_object_or_404(Post, id=post_id, status='published')

    if request.method == "POST":
        rendered_form = EmailPostForm(data=request.POST)
        if rendered_form.is_valid():
            clean_data = rendered_form.cleaned_data
            who_shares = clean_data["name"]
            comments = clean_data["comments"]
            with_who_shares = clean_data["email_to"]
            post_url = request.build_absolute_uri(post.get_absolute_url)
            subject = f'{who_shares} recommends you check out {post.title}'
            message = f'Post is available at {post_url}. {who_shares}\'s comments: {comments}'
            send_mail(subject, message, '', [with_who_shares])
            mail_sent = True

    if request.method == "GET":
        rendered_form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': rendered_form, 'mail_sent': mail_sent})
