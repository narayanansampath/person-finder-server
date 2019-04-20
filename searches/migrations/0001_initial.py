# Generated by Django 2.1.7 on 2019-03-31 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('doi', models.DateField(verbose_name='date of incident')),
                ('poi', models.CharField(max_length=255, verbose_name='place of incident')),
                ('fir_url', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('INITIALIZED', 'Initializd'), ('WAIT_FOR_APP', 'Waiting For Approval'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('UNKNOWN', 'Unknown')], default='INITIALIZED', max_length=20)),
                ('status_msg', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='complaints', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video_url', models.TextField(verbose_name='video source url')),
                ('location', models.CharField(max_length=255, null=True, verbose_name='name of the location')),
                ('lat', models.CharField(max_length=255, null=True)),
                ('long', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(choices=[('INITIALIZED', 'Initialized'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('ERROR', 'Error')], default='INITIALIZED', max_length=20)),
                ('progress', models.IntegerField(default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Searchee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('dob', models.DateField(verbose_name='date of birth')),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('NON_BINARY', 'Non Binary')], max_length=20, null=True)),
                ('height_cm', models.DecimalField(decimal_places=2, max_digits=3, null=True, verbose_name='height in cm')),
                ('weight_kg', models.IntegerField(null=True, verbose_name='weight in kg')),
                ('skin_tone', models.CharField(choices=[('ST_LIGHT', 'Light'), ('ST_MEDIUM', 'Medium'), ('ST_DARK', 'Dark')], max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='searchees', to='searches.Complaint')),
            ],
        ),
        migrations.CreateModel(
            name='SearcheeSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField()),
                ('userability', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('searchee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='searches.Searchee')),
            ],
        ),
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_sec', models.IntegerField(verbose_name='timestamp where appeared')),
                ('x1', models.IntegerField(default=0, verbose_name='x1 coordinate')),
                ('y1', models.IntegerField(default=0, verbose_name='y1 coordinate')),
                ('x2', models.IntegerField(default=0, verbose_name='x2 coordinate')),
                ('y2', models.IntegerField(default=0, verbose_name='y2 coordinate')),
                ('image_url', models.TextField(null=True)),
                ('confidence', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('search', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='searches.Search')),
            ],
        ),
        migrations.AddField(
            model_name='search',
            name='searchee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='searches', to='searches.Searchee'),
        ),
    ]