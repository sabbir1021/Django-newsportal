from django.shortcuts import render , get_object_or_404,redirect
from . models import Article , Category , Comment
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CommentForm ,CreateForm



def index(request):
    cat = Category.objects.all()
    breking = Article.objects.all().order_by("-id")

    fontlead = Article.objects.all().filter(lead=True).order_by("-id")
    paginator = Paginator(fontlead, 1)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagfontlead = paginator.get_page(page)

    sidelead = Article.objects.all().filter(lead2=True).exclude(lead=True).order_by("-id")
    paginator = Paginator(sidelead, 2)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagsidelead = paginator.get_page(page)

    ban = Article.objects.all().filter(category__id=1).exclude(lead3=True).order_by("-id")
    paginator = Paginator(ban, 3)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagban = paginator.get_page(page)

    banlead = Article.objects.all().filter(category__id=1).filter(lead3=True).order_by("-id")
    paginator = Paginator(banlead, 1)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagbanlead = paginator.get_page(page)

    inter = Article.objects.all().filter(category__id=2).order_by("-id")
    paginator = Paginator(inter, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    paginter = paginator.get_page(page)

    latest = Article.objects.all().order_by("-id")
    paginator = Paginator(latest, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    paglatest = paginator.get_page(page)

    sport = Article.objects.all().filter(category__id=3).order_by("-id")
    paginator = Paginator(sport, 6)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagsport = paginator.get_page(page)

    tain = Article.objects.all().filter(category__id=4).exclude(lead3=True).order_by("-id")
    paginator = Paginator(tain, 3)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagtain = paginator.get_page(page)

    tainlead = Article.objects.all().filter(category__id=4).filter(lead3=True).order_by("-id")
    paginator = Paginator(tainlead, 1)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagtainlead = paginator.get_page(page)

    popular = Article.objects.all().order_by("-id")
    paginator = Paginator(popular, 4)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagpopular = paginator.get_page(page)

    ict = Article.objects.all().filter(category__id=5).exclude(lead3=True).order_by("-id")
    paginator = Paginator(ict, 4)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagict = paginator.get_page(page)

    ictlead = Article.objects.all().filter(category__id=5).filter(lead3=True).order_by("-id")
    paginator = Paginator(ictlead, 1)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagictlead = paginator.get_page(page)

    life = Article.objects.all().filter(category__id=5).exclude(lead3=True).order_by("-id")
    paginator = Paginator(life, 4)  # Show 25 contacts per page
    page = request.GET.get('page')
    paglife = paginator.get_page(page)

    lifelead = Article.objects.all().filter(category__id=5).filter(lead3=True).order_by("-id")
    paginator = Paginator(lifelead, 1)  # Show 25 contacts per page
    page = request.GET.get('page')
    paglifelead = paginator.get_page(page)

    job = Article.objects.all().filter(category__id=5).exclude(lead3=True).order_by("-id")
    paginator = Paginator(job, 4)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagjob = paginator.get_page(page)

    joblead = Article.objects.all().filter(category__id=5).filter(lead3=True).order_by("-id")
    paginator = Paginator(joblead, 1)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagjoblead = paginator.get_page(page)

    search = request.GET.get("q")
    if search:
        breking=breking.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )





    return render(request, "index.html", {
        "cat":cat,
        "breking":breking , 
        "ban":pagban, 
        "inter":inter,
        "banlead":pagbanlead,
        "fontlead":pagfontlead,
        "sidelead":pagsidelead,
        "inter":paginter,
        "latest":paglatest,
        "sport":pagsport,
        "tain":pagtain,
        "tainlead":pagtainlead,
        "popular":pagpopular,
        "ict":pagict,
        "ictlead":pagictlead,
        "life":paglife,
        "lifelead":paglifelead,
        "job":pagjob,
        "joblead":pagjoblead,


        })


def singel(request, id):
    cat = Category.objects.all()
    breking = Article.objects.all().order_by("-id")
    post = get_object_or_404(Article, pk=id)

    latest = Article.objects.all().exclude(id=id).order_by("-id")
    paginator = Paginator(latest, 8)  # Show 25 contacts per page
    page = request.GET.get('page')
    paglatest = paginator.get_page(page)

    popular = Article.objects.all().order_by("-id")
    paginator = Paginator(popular, 4)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagpopular = paginator.get_page(page)

    first = Article.objects.first()
    last = Article.objects.last()
    if True:
        if post.id > 1:
            firstpost = get_object_or_404(Article, pk=id-1)
        else:
            firstpost = get_object_or_404(Article, pk=id)
    if True:
        if post.id < last.id:
            lastpost = get_object_or_404(Article, pk=id+1)
        else:
            lastpost = get_object_or_404(Article, pk=id)
    com = Comment.objects.filter(post=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.post=post
        instance.save();

    return render(request, "single.html", {
        "cat":cat,
        "breking":breking,
        "post": post , 
        "latest":paglatest,
        "popular":pagpopular,
        "com":com,
        "form":form,
        "first":first,
        "last":last,
        "firstpost":firstpost,
        "lastpost":lastpost
     })

def topic(request, id):
    cat = Category.objects.all()
    breking = Article.objects.all().order_by("-id")

    popular = Article.objects.all().order_by("-id")
    paginator = Paginator(popular, 4)  # Show 25 contacts per page
    page = request.GET.get('page')
    pagpopular = paginator.get_page(page)

    cate = get_object_or_404(Category, pk=id)

    post = Article.objects.all().filter(category__id=id)
    paginator = Paginator(post, 8)  # Show 25 contacts per page
    page_number = request.GET.get('page')
    pagpost = paginator.get_page(page_number)

    latest = Article.objects.all().order_by("-id")
    paginator = Paginator(latest, 8)  # Show 25 contacts per page
    page = request.GET.get('page')
    paglatest = paginator.get_page(page)

    return render(request, "category.html", {
        "cat":cat,
        "breking":breking,
        "popular":pagpopular,
        "post":pagpost,
        "latest":paglatest,
        "cate":cate,


    })

def create(request):
    cat = Category.objects.all()
    breking = Article.objects.all().order_by("-id")
    if request.user.is_authenticated:
        form = CreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save();
            return redirect('home')
    else:
        return redirect('home')
    return render(request, "create.html" , {"form":form,"cat":cat,"breking":breking })