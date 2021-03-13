from django.db import models
from django.urls import reverse
import datetime
import hashlib
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Uniques Value for Product Page URL')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
                                     help_text='Comma-Deliminated set of SEO Keywords for Meta Tags')
    meta_description = models.CharField("Meta Description", max_length=255, help_text="Content for Meta Tags")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "categories"
        ordering = ['-created_at']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalogue_category', (), {'category_slug': self.slug})


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, help_text='Unique value for product page URL')
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    image = models.ImageField(upload_to='shop/images/products', default="")
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255, help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = "products"
        ordering = ['-created_at']
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'catalog_product', (), {'product_slug': self.slug}

    def sale_price(self):
        if self.old_price > self.price:
            return self.price

        else:
            return None

    @staticmethod
    def get_products_by_category(category_id):
        if category_id:
            Product.objects.filter(categories=category_id, )
        else:
            Product.objects.all()


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=500)

    class Meta:
        db_table = "customer"
        verbose_name_plural = "customers"

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(default='', max_length=150, blank=True)
    phone = models.CharField(default='', max_length=150, blank=True)
    date = models.DateTimeField(default=datetime.datetime.today)

    class Meta:
        db_table = "orders"
        verbose_name_plural = "Orders"
