from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Category
from django.contrib.auth.decorators import login_required

#cree sus vistas aqui
@login_required(login_url="login")
def list(request):
    # Muestra todos los articulos
    articles = Article.objects.all()

    #paginar los articulos
    paginator = Paginator(articles, 3)

    #recorer numero de pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    
    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_articles
    })

@login_required(login_url="login")
def category(request,category_id):
    category = get_object_or_404(Category, id=category_id)
    #articles = Article.objects.filter(categories=category)

    return render(request,'categories/category.html',{
        'category' : category,
        #'articles' : articles
    })

@login_required(login_url="login")
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html',{

    })
