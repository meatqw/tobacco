from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Availability(models.Model):
    """Availability of a product"""
    in_stock_rest = models.IntegerField('Остаток в наличии', blank=True, null=True)
    on_way_rest = models.IntegerField('Остаток в пути', blank=True, null=True)
    remote_rest = models.IntegerField('Остаток в удаленный склад', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"В наличии: {self.in_stock_rest}\nВ пути: {self.on_way_rest}\nУдаленный склад: {self.remote_rest}"

    class Meta:
        verbose_name = 'Доступность'
        verbose_name_plural = 'Доступность товаров'


# Create your models here.
class Product(models.Model):
    """Product model"""
    name = models.CharField('Наименование', max_length=40, blank=True)
    img = models.ImageField('Изображение', upload_to="img/%Y/%m/%d", blank=True)
    # rest = models.IntegerField('Остаток', blank=True)
    price = models.IntegerField('Цена', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    # avalability
    availability = models.ForeignKey(Availability, on_delete=models.PROTECT) #


    category = models.ForeignKey('Subcategory', on_delete=models.PROTECT, null=True)
    product_status = models.ForeignKey('ProductStatus', on_delete=models.PROTECT, null=True)  # статус товара(new, sale..)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Список товаров'


class Category(models.Model):
    """Category of a product"""
    name = models.CharField('Название', max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Основные категории товаров'


class Subcategory(models.Model):
    """Subcategory of a product"""
    name = models.CharField('Название', max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)
    info = models.TextField('Информация', blank=True, null=True)
    img = models.ImageField('Изображение', upload_to="img/%Y/%m/%d", blank=True)
    parent_category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории товаров'


class ProductStatus(models.Model):
    """Status of a product"""
    name = models.CharField('Название', max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы товаров'

class Account(models.Model):
    """User account data"""
    name = models.CharField('Имя', max_length=300)
    phone = models.CharField('Телефон', max_length=300)
    email = models.CharField('Почта', max_length=300)
    agents = models.CharField('Контрагенты', max_length=300)
    address = models.CharField('Адреса', max_length=300)

    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Order(models.Model):
    """Intermediate order data"""
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    order = models.JSONField("Ордер лист", null=True, blank=True)
    status = models.BooleanField("Status", default=False)
    # time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Промежуточные данные заказа'

class Banners(models.Model):
    """Banners img"""
    name = models.CharField('Название', max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)
    img = models.ImageField('Изображение', upload_to="img/%Y/%m/%d", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

class DeliveryAddresses(models.Model):
    """Addresses for delivery"""
    address = models.CharField('Адрес', max_length=300)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'

class UserOrder(models.Model):
    "Orders that the user has confirmed"
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    number = models.CharField('Номер заказа', max_length=300)
    items = models.JSONField("Ордер лист", null=True, blank=True)
    pay_status = models.CharField('Статус оплаты', max_length=300)
    order_status = models.CharField('Статус заказа', max_length=300)
    address = models.ForeignKey(DeliveryAddresses, on_delete=models.PROTECT, null=True)
    comment = models.TextField('Комментарий', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField('Цена', blank=True)
    payment_method = models.CharField('Способ оплаты', max_length=300)
    way_get = models.CharField('Способ получения', max_length=300)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



class ProductAdminFields(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Product._meta.fields]

class AvailabilityAdminFields(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Availability._meta.fields]

class CategoryAdminFields(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Category._meta.fields]

class SubcategoryAdminFields(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Subcategory._meta.fields]

class ProductStatusAdminFields(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in ProductStatus._meta.fields]

class AccountAdminFields(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Account._meta.fields]

class OrderAdminFields(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Order._meta.fields]

class BannersAdminFields(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Banners._meta.fields]

class DeliveryAddressesAdminFields(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in DeliveryAddresses._meta.fields]

class UserOrderAdminFields(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in UserOrder._meta.fields]
