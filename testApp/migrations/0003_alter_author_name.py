# Generated by Django 4.1.3 on 2022-12-01 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_alter_book_options_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='name'),
        ),
    ]