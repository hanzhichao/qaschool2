# Generated by Django 2.1 on 2018-11-26 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
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
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('keywords', models.CharField(blank=True, max_length=80, null=True, verbose_name='关键字')),
                ('slug', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='网址')),
                ('sn', models.IntegerField(null=True, verbose_name='排序')),
                ('abstract', models.CharField(blank=True, max_length=200, null=True, verbose_name='摘要')),
                ('content', mdeditor.fields.MDTextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('status', models.CharField(choices=[('d', '草稿'), ('p', '发布')], default='p', max_length=1, verbose_name='状态')),
            ],
            options={
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
                'ordering': ['-last_modified_time'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮件')),
                ('content', models.TextField(null=True, verbose_name='评论内容')),
                ('visible', models.BooleanField(default=True, verbose_name='显示')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='course.Chapter', verbose_name='所属章节')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ('created_time',),
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('template', models.CharField(choices=[('bootstrap', 'bootstrap'), ('bootswatch', 'bootswatch')], max_length=20, verbose_name='模板')),
                ('theme', models.CharField(choices=[('bootstrap', 'bootstrap'), ('litera', 'litera'), ('litera', 'litera'), ('materia', 'materia'), ('stadstone', 'stadstone'), ('yeti', 'yeti')], max_length=20, verbose_name='模板')),
                ('gen_static_pages', models.BooleanField(default=False, verbose_name='是否生成静态页面')),
            ],
            options={
                'verbose_name': '配置',
                'verbose_name_plural': '配置',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='课程名称')),
                ('slug', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='课程网址')),
                ('sn', models.IntegerField(null=True, verbose_name='排序')),
                ('intro', models.CharField(max_length=100, verbose_name='课程简介')),
                ('visible', models.BooleanField(default=True, verbose_name='显示')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='', verbose_name='缩略图')),
                ('star', models.IntegerField(default=3, verbose_name='评星')),
                ('star_eval_num', models.IntegerField(default=1, verbose_name='评星人数')),
                ('keywords', models.CharField(blank=True, max_length=80, null=True, verbose_name='关键字')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Category', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='归属课程'),
        ),
    ]
