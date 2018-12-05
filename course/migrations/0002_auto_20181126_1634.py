# Generated by Django 2.1 on 2018-11-26 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='分类名称')),
                ('visible', models.BooleanField(default=True, verbose_name='显示')),
                ('show_in_nav', models.BooleanField(default=False, verbose_name='导航显示')),
                ('slug', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='分类网址')),
                ('sn', models.IntegerField(null=True, verbose_name='排序')),
                ('intro', models.CharField(blank=True, max_length=200, null=True, verbose_name='分类简介')),
                ('created_time', models.DateTimeField(null=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('keywords', models.CharField(blank=True, max_length=80, null=True, verbose_name='关键字')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='负责人')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='chapter',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='course',
            name='column',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='course.Column', verbose_name='所属分类'),
            preserve_default=False,
        ),
    ]