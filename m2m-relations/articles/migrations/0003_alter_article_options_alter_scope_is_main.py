# Generated by Django 4.0.4 on 2022-05-22 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope_article_scopes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Дата публикации'),
        ),
    ]
