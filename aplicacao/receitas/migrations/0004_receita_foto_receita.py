# Generated by Django 2.2.6 on 2022-08-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='foto/%d/%m/%Y/'),
        ),
    ]
