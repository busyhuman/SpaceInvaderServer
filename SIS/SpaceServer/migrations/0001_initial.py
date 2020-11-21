# Generated by Django 3.0.8 on 2020-07-05 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('PW', models.TextField(default='spaceadmin', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('RecordNum', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('Score', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpaceServer.User')),
            ],
        ),
    ]