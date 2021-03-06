# Generated by Django 3.1.7 on 2021-03-21 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('is_archive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('yt_link', models.CharField(blank=True, max_length=255, null=True)),
                ('useful_link', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='CountTake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category_app.category')),
            ],
        ),
    ]
