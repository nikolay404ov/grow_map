# Generated by Django 3.2.8 on 2022-11-19 14:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'card',
                'verbose_name_plural': 'cards',
                'db_table': 'card',
            },
        ),
        migrations.CreateModel(
            name='CardDomen',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField()),
                ('card_id', models.ForeignKey(db_column='card_id', on_delete=django.db.models.deletion.CASCADE, to='grow_map.card')),
            ],
            options={
                'verbose_name': 'card_domen',
                'verbose_name_plural': 'card_domens',
                'db_table': 'card_domen',
            },
        ),
        migrations.CreateModel(
            name='Domen',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='description')),
            ],
            options={
                'verbose_name': 'domen',
                'verbose_name_plural': 'domens',
                'db_table': 'domen',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('grade_name', models.CharField(max_length=255, verbose_name='grade_name')),
                ('unit_name', models.CharField(max_length=255, verbose_name='unit_name')),
                ('grade_number', models.IntegerField(verbose_name='grade_number')),
            ],
            options={
                'verbose_name': 'grade',
                'verbose_name_plural': 'grades',
                'db_table': 'grade',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('person_name', models.CharField(max_length=255, verbose_name='person_name')),
                ('grade_id', models.ForeignKey(db_column='grade_id', on_delete=django.db.models.deletion.PROTECT, to='grow_map.grade')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='Commitments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=1023, verbose_name='description')),
                ('active', models.BooleanField()),
                ('card_id', models.ForeignKey(db_column='card_id', on_delete=django.db.models.deletion.CASCADE, to='grow_map.card')),
            ],
            options={
                'verbose_name': 'commitment',
                'verbose_name_plural': 'commitments',
                'db_table': 'commitments',
            },
        ),
        migrations.CreateModel(
            name='CardDomenTasks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=1023, verbose_name='description')),
                ('tracker_link', models.CharField(max_length=1023, verbose_name='description')),
                ('definition_of_done', models.CharField(max_length=1023, verbose_name='description')),
                ('status', models.CharField(max_length=255, verbose_name='description')),
                ('card_domen_id', models.ForeignKey(db_column='card_domen_id', on_delete=django.db.models.deletion.CASCADE, to='grow_map.carddomen')),
            ],
            options={
                'verbose_name': 'card_domen_tasks',
                'verbose_name_plural': 'card_domen_tasks',
                'db_table': 'card_domen_tasks',
            },
        ),
        migrations.AddField(
            model_name='carddomen',
            name='domen_id',
            field=models.ForeignKey(db_column='domen_id', on_delete=django.db.models.deletion.PROTECT, to='grow_map.domen'),
        ),
        migrations.AddField(
            model_name='card',
            name='person_id',
            field=models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='grow_map.person'),
        ),
    ]
