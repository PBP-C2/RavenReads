# Generated by Django 4.1 on 2023-10-27 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0004_remove_mainthread_user_remove_thread_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=5000)),
                ('person', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
        ),
    ]
