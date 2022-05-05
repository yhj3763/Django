# Generated by Django 4.0.4 on 2022-04-26 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('auid', models.IntegerField(db_column='auID', primary_key=True, serialize=False)),
                ('aname', models.CharField(blank=True, db_column='aNAME', max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('custid', models.AutoField(db_column='custID', primary_key=True, serialize=False)),
                ('custname', models.CharField(blank=True, db_column='custName', max_length=20, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('pubid', models.IntegerField(db_column='pubID', primary_key=True, serialize=False)),
                ('pname', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'publishers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('subid', models.CharField(db_column='subID', max_length=5, primary_key=True, serialize=False)),
                ('sname', models.CharField(blank=True, db_column='sName', max_length=30, null=True)),
            ],
            options={
                'db_table': 'subjects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('titleid', models.IntegerField(db_column='titleID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('pubdate', models.DateField(blank=True, db_column='pubDate', null=True)),
                ('cover', models.CharField(blank=True, max_length=1, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'titles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Titleauthors',
            fields=[
                ('titleid', models.OneToOneField(db_column='titleID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.titles')),
                ('importance', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'titleauthors',
                'managed': False,
            },
        ),
    ]
