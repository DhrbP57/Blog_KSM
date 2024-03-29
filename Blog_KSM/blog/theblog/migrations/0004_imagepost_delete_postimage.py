# Generated by Django 4.0.5 on 2022-06-27 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_postimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theblog.post')),
            ],
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
