# Generated by Django 4.2 on 2023-06-13 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Навык', 'verbose_name_plural': 'Навыки'},
        ),
    ]
