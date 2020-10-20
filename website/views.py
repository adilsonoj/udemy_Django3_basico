from django.shortcuts import render
from .models import Post, Contact


def hello_blog(request):
    lista = [
        'Django', 'Python', 'nginx',
        'Templates'
    ]
    # lista todos objetos do bd
    # posts = Post.objects.all()

    posts = Post.objects.filter(deleted=False)
    data = {'name': 'Aprendendo Django',
            'lista': lista,
            'posts': posts}
    return render(request, 'index.html', data)


def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_details.html', {'post': post})


def save_form(request):
    print(request.POST)
    name = request.POST['name']
    Contact.objects.create(
        name=name,
        email=request.POST['email'],
        message=request.POST['message']
    )

    return render(request, 'contact_success.html', {'name': name})
