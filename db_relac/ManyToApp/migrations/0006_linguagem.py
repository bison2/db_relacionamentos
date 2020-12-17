# Generated by Django 3.1.4 on 2020-12-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManyToApp', '0005_carro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('pessoa', models.ManyToManyField(related_name='linguagem', to='ManyToApp.Pessoa')),
            ],
        ),
    ]
