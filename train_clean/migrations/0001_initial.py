# Generated by Django 2.0 on 2018-06-10 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CleanRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clean_front', models.BooleanField(default=True, verbose_name='是否端洗')),
                ('clean_date', models.DateTimeField(auto_now=True, verbose_name='清洗日期')),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='线路名')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='车体号')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train_clean.Line')),
            ],
        ),
        migrations.AddField(
            model_name='cleanrecords',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train_clean.Train'),
        ),
    ]
