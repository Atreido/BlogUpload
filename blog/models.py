from django.db import models
from django.contrib.auth.models import User

class Cathegories(models.Model):
    name = models.CharField(max_length=20, verbose_name="Назва")
    def __str__(self):
        return self.name # замена вывода на админке

    class Meta:     # создание перевода
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class Tags(models.Model):
    name = models.CharField(max_length=50, verbose_name="Заголовок")
    fk_post = models.IntegerField(verbose_name='id поста')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField()
    published_date = models.DateTimeField(auto_created=True, verbose_name="дата і час")
    category = models.ForeignKey(Cathegories, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="користувач")
    image = models.ImageField(upload_to='uploads', blank=True)
    description = models.CharField(max_length=50, blank=True)
    poster = models.URLField(default="http://placehold.it/900x300", verbose_name="постер")
    fk_tag = models.ManyToManyField(Tags, blank=True, related_name="posts")

    def __str__(self): # замена вывода на админке
        return self.title
    class Meta:     # создание перевода
        verbose_name = "Пост"
        verbose_name_plural = "Пости"



class Comments(models.Model):
    comment = models.TextField(verbose_name="Коментар")
    publish_date = models.DateTimeField(auto_created=True, verbose_name="Дата і час")
    posted = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    def __str__(self): # замена вывода на админке
        return f"{self.user.username} к посту '{self.posted.title}' написал: {self.comment[:10]}..."
    class Meta:     # создание перевода
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"


# python .\manage.py shell
# from blog.models import Cathegories
# c = Cathegories(name="C++")
# c.save()
#  categories = Cathegories.objects.all()
# print(categories)
# # <QuerySet [<Cathegories: python>, <Cathegories: Навчання>, <Cathegories: Автомобілі>, <Cathegories: Книги>, <Cathegories: Кіно>, <Cathegories: Info>, <Cathegories: C++>]>
# print(categories.count())