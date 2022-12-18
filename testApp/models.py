from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField("title", max_length=255)
    author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, null=True, blank=False)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    name = models.CharField("name", max_length=255, db_index=True)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self) -> str:
        return self.name


class Tovars(models.Model):
    iddoc = models.CharField("ID Чека", max_length=340, default="Test")
    kolvo = models.FloatField("Кол-во товара", default=1.0)
    summa = models.FloatField("Сумма", default=1.0)
    name = models.CharField("Имя товара", max_length=340)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"
        ordering = ('id',)

        