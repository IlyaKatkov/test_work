from django.db import models
from django.conf import settings
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    email = models.EmailField(verbose_name='имэйл', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='Страна')
    city = models.CharField(max_length=25, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(
        max_length=10,
        verbose_name='Номер дома',
        **NULLABLE
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Создатель',
        **NULLABLE
    )

    def __str__(self):
        return f"{self.city}, {self.country}"

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактные данные'


class Supplier(models.Model):

    LINK_TYPE_CHOICES = (
        ('Factory', 'Завод'),
        ('Retail Network', 'Розничная сеть'),
        ('Individual Entrepreneur', 'ИП'),
    )

    company_name = models.CharField(
        max_length=100,
        verbose_name='Название компании',
    )
    link_type = models.CharField(
        max_length=100,
        choices=LINK_TYPE_CHOICES,
        verbose_name='Тип звена'
    )
    contacts = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        verbose_name='Контактная информация',
        **NULLABLE
    )
    supplier_name = models.ForeignKey(
        'Supplier',
        on_delete=models.SET_NULL,
        verbose_name='Поставщик',
        **NULLABLE
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Задолженность'
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Время создания'
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        **NULLABLE
    )

    def __str__(self):
        return f"{self.company_name}"

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    launch_date = models.DateField(verbose_name='Дата выхода', **NULLABLE)
    supplier = models.ForeignKey(
        'Supplier',
        on_delete=models.CASCADE,
        verbose_name='Поставщик',
        **NULLABLE
    )

    def __str__(self):
        return f"{self.title} ({self.model})"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
