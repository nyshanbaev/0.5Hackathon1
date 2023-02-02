# Generated by Django 4.1.6 on 2023-02-02 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='test1.post')),
            ],
        ),
    ]
