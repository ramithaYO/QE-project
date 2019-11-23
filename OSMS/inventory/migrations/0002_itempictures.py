# Generated by Django 2.2.7 on 2019-11-20 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='itempictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='item_pics')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory.Items')),
            ],
        ),
    ]