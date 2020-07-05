# Generated by Django 3.0.8 on 2020-07-05 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('platform', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.Platform', verbose_name='Platform')),
            ],
        ),
    ]