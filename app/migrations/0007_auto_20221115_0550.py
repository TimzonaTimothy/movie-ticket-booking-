# Generated by Django 3.0.5 on 2022-11-15 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_date_buyer_purchase_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/')),
                ('name', models.CharField(max_length=100)),
                ('dis', models.TextField(max_length=500)),
                ('price', models.CharField(max_length=100)),
                ('no_ticket', models.IntegerField(null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=100)),
                ('amount_paid', models.CharField(max_length=100)),
                ('verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.DeleteModel(
            name='producat',
        ),
        migrations.AddField(
            model_name='buyer',
            name='role',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='purchase_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.buyer'),
        ),
    ]