# Generated by Django 3.1.4 on 2020-12-25 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ManyToApp', '0006_linguagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_fisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ManyToApp.pessoa')),
                ('cpf', models.CharField(max_length=11)),
            ],
            bases=('ManyToApp.pessoa',),
        ),
        migrations.CreateModel(
            name='P_juridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ManyToApp.pessoa')),
                ('cnpj', models.CharField(max_length=11)),
            ],
            bases=('ManyToApp.pessoa',),
        ),
    ]
