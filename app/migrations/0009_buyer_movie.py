# Generated by Django 3.0.5 on 2022-11-15 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20221115_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Movie'),
        ),
    ]
