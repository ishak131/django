from itertools import product
from django.db import models
from ckeditor.fields import RichTextField 


class Brand(models.Model):
    brand = models.CharField(
        max_length=400, primary_key=True)

    def __str__(self):
        return self.brand

class Size(models.Model):
    size = models.CharField(max_length=6,primary_key=True)
    
    def __str__(self):
        return self.size

class Color(models.Model):
    color = models.CharField(max_length=100,primary_key=True)
    
    def __str__(self):
        return self.color


class Category(models.Model):
    category = models.CharField(max_length=100,primary_key=True)
    
    def __str__(self):
        return self.category


class Product(models.Model):   
    title = models.CharField(max_length=500)
    caption = models.TextField(max_length=10000)
    description = models.TextField(max_length=10000)
    specification = models.TextField(max_length=10000)
    thumbnail = models.ImageField(upload_to='thumbnail/')
    cover = models.ImageField(upload_to='cover/')
    price = models.FloatField(default=1)
    available_colors = models.ManyToManyField(Color)
    available_sizes = models.ManyToManyField(Size)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE,unique=True)
    productQuantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.title

# class Article(models.Model):
#     article_link = models.CharField(
#         max_length=100000, verbose_name=' رابط المقال', primary_key=True)
#     article_title = models.CharField(
#         max_length=500, verbose_name='عنوان المقال')
#     article_caption = models.TextField(max_length=10000, verbose_name="الوصف")
#     my_field = RichTextField(blank=True , null=True,verbose_name=' محرر المقال')
#     article_lang = models.ForeignKey(
#         Languages, on_delete=models.CASCADE, default=None, verbose_name='لغة المقال')
#     article_category = models.ForeignKey(
#         Category, on_delete=models.CASCADE, default=None, verbose_name='نوع المقال')
#     aritcle_image = models.ImageField(
#         upload_to='uploads/', verbose_name='صورة المقال')
#     aritcle_thumbnail = models.ImageField(
#         upload_to='uploads/', verbose_name='الصورة المصغرة للمقال')
#     pub_date = models.DateTimeField('تاريخ النشر')

#     def __str__(self):
#         return self.article_title


# class Choice(models.Model):
#     question = models.ForeignKey(Article, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
