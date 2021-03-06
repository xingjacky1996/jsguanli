# Generated by Django 2.1.3 on 2019-09-29 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(blank=True, max_length=20, null=True, verbose_name='课程名')),
            ],
            options={
                'verbose_name_plural': '课程名表',
            },
        ),
        migrations.CreateModel(
            name='Coursefour',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('coursename', models.CharField(blank=True, max_length=20, null=True, verbose_name='课程名')),
            ],
            options={
                'verbose_name_plural': '顺序为4的课程表',
            },
        ),
        migrations.CreateModel(
            name='Courseone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('coursename', models.CharField(blank=True, max_length=20, null=True, verbose_name='课程名')),
            ],
            options={
                'verbose_name_plural': '顺序为1的课程表',
            },
        ),
        migrations.CreateModel(
            name='Coursethree',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('coursename', models.CharField(blank=True, max_length=20, null=True, verbose_name='课程名')),
            ],
            options={
                'verbose_name_plural': '顺序为3的课程表',
            },
        ),
        migrations.CreateModel(
            name='Coursetwo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('coursename', models.CharField(blank=True, max_length=20, null=True, verbose_name='课程名')),
            ],
            options={
                'verbose_name_plural': '顺序为2的课程表',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=8, verbose_name='学生姓名')),
                ('t_name', models.CharField(max_length=8, verbose_name='教师姓名')),
                ('date', models.DateField(auto_now_add=True, verbose_name='发布日期')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='发布时间')),
                ('content', models.TextField(max_length=200, verbose_name='发布内容')),
                ('direction', models.CharField(choices=[('0', '学生给教师'), ('1', '教师给学生')], default='0', max_length=20, verbose_name='消息的发送或接收')),
            ],
            options={
                'verbose_name_plural': '消息',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=20, verbose_name='新闻标题')),
                ('news_author', models.CharField(max_length=10, verbose_name='新闻作者')),
                ('r_time', models.DateTimeField(verbose_name='发布时间')),
                ('news_picture', models.FileField(upload_to='./newsimg/', verbose_name='新闻图片储存路径')),
                ('news_content', models.TextField(max_length=300, verbose_name='新闻内容')),
            ],
            options={
                'verbose_name_plural': '新闻',
            },
        ),
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=10, verbose_name='发布者名称')),
                ('r_time', models.DateTimeField(verbose_name='发布时间')),
                ('p_content', models.TextField(max_length=300, verbose_name='发布内容')),
            ],
            options={
                'verbose_name_plural': '通知',
            },
        ),
        migrations.CreateModel(
            name='Uploadfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='用户名')),
                ('headImg', models.FileField(upload_to='./upload/')),
            ],
            options={
                'verbose_name_plural': '上传文件',
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='教师名')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('userid', models.CharField(default='', max_length=16, verbose_name='用户ID')),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('0', '男'), ('1', '女')], default='男', max_length=32, verbose_name='性别')),
                ('c_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('idtype', models.CharField(choices=[('0', '教师'), ('1', '学生')], default='教师', max_length=32, verbose_name='身份类别')),
            ],
            options={
                'verbose_name_plural': '教师信息',
            },
        ),
    ]
