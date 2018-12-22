from django.shortcuts import render

from article.models import Article, Comment

def article(request):
    '''
    Render the article page
    '''
    articles = {}
    for article in Article.objects.all():
        articles.update({article:Comment.objects.filter(article=article)})
    context = {'articles':articles}
    return render(request, 'article/article.html', context)

def articleCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the article page
    '''
    # TODO: finish the code
    return render(request, 'article/article.html')