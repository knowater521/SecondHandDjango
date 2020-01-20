# Generated by Django 2.2.5 on 2020-01-06 06:37

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
                ('name', models.CharField(max_length=10, verbose_name='类别名称')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(default='', max_length=20)),
                ('profile', models.CharField(default='', max_length=50)),
                ('head_portrait', models.ImageField(blank=True, null=True, upload_to='portraits', verbose_name='头像')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, verbose_name='电子邮件')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='商品描述')),
                ('display_image', models.ImageField(upload_to='display_images', verbose_name='展示图片')),
                ('price', models.FloatField(verbose_name='价格')),
                ('express_fee', models.FloatField(verbose_name='快递费')),
                ('belong_to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.User', verbose_name='商品拥有者')),
                ('category', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='trade.Category', verbose_name='商品类别')),
            ],
        ),
    ]