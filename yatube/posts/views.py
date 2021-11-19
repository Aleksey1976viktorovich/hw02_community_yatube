from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post, Group


# функция для index.html
def index(request):
    title: str = 'Последние обновления на сайте.'
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к
    # меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


# функция для group_posts.html
def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект из
    # базы данных или возвращает сообщение об ошибке, если объект не
    # найден.
    group = get_object_or_404(Group, slug=slug)
    # Метод .filter позволяет ограничить поиск по критериям.
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

