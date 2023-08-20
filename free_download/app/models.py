from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse
from django.contrib.auth.models import User


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'



class Programs(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Автор", blank=True, null=True)
    content = models.TextField(blank=True)
    size = models.FloatField(default=0, verbose_name="Размер")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_post', kwargs={'post_slug': self.slug})


    class Meta:
        verbose_name = 'Программу'
        verbose_name_plural = 'Программы'


class Comments(models.Model):
    post = models.ForeignKey(Programs, on_delete=models.PROTECT, verbose_name="Пост", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Автор", blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    text = models.TextField(verbose_name="Текст комментария")



    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'