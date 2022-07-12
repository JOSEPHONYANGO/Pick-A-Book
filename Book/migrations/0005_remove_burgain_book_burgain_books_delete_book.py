# Generated by Django 4.0.6 on 2022-07-12 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_alter_cart_options_remove_cart_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='burgain',
            name='book',
        ),
        migrations.AddField(
            model_name='burgain',
            name='books',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Book.books'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
