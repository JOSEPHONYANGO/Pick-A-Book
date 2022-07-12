# Generated by Django 4.0.6 on 2022-07-11 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='books',
            new_name='book',
        ),
        migrations.AlterField(
            model_name='books',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='Book.user'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_user', to='Book.user'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_delivery', to='Book.user'),
        ),
        migrations.AlterField(
            model_name='makeoffer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_offer', to='Book.user'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.user'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_payment', to='Book.user'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='Book.user'),
        ),
    ]
