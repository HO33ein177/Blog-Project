from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=' دسته بندی مقاله')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='دسته بندی مقاله')
    status = models.BooleanField(default=True, verbose_name="ایا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['position']

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', "پیش نویس"),
        ('p', "منتشر شده"),
    )
    title = models.CharField(max_length=100, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='ادرس مقاله')
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    description = models.TextField(verbose_name='محتوا')
    thumbnail = models.ImageField(upload_to="images", verbose_name='تصویر مقاله')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت انتشار')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
