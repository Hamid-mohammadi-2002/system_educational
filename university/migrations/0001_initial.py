# Generated by Django 3.2.6 on 2021-09-02 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_in_rent', models.BooleanField(default=True)),
                ('rent_start_date', models.DateTimeField()),
                ('rent_end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('unit', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.customuser')),
                ('grade', models.CharField(choices=[('BACHELOR', 'Bachelor'), ('MASTER', 'Master'), ('PhD', 'PhD'), ('POSTDOC', 'Postdoc')], max_length=8)),
                ('books_in_rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.book')),
                ('lesson', models.ManyToManyField(to='university.Lesson')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.customuser',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.customuser')),
                ('college_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.college')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.customuser',),
        ),
        migrations.AddField(
            model_name='lesson',
            name='professor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.professor'),
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('class_day', models.CharField(choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], max_length=9)),
                ('class_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('college_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.college')),
                ('professor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.professor')),
                ('students', models.ManyToManyField(to='university.Student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='college',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='university.college'),
        ),
    ]
