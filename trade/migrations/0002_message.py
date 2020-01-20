# Generated by Django 2.2.5 on 2020-01-07 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('belong_to_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.Goods', verbose_name='所属商品')),
                ('belong_to_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='trade.User', verbose_name='接收方')),
                ('belong_to_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='trade.User', verbose_name='发送方')),
            ],
        ),
    ]
