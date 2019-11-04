# Generated by Django 2.2.6 on 2019-11-04 13:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('Chatroom_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('abort', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='counsellor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=100)),
                ('user_status', models.BooleanField(default=False)),
                ('user_information', models.TextField(max_length=1000)),
                ('user_dp', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('student_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=1000)),
                ('message_from', models.BooleanField()),
                ('message_time', models.DateTimeField()),
                ('chat_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Chatroom')),
            ],
        ),
        migrations.AddField(
            model_name='chatroom',
            name='Counsellor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.counsellor'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.student'),
        ),
    ]
