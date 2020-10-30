# Generated by Django 3.0.10 on 2020-10-29 17:00

import apps.core.fields.aes_json_field
import apps.core.fields.aes_text_field
import apps.core.managers.user
import apps.core.models.api_key
import apps.core.models.service
import apps.core.models.user
from django.db import migrations, models
import django.db.models.deletion
import django_enum_choices.choice_builders
import django_enum_choices.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='username')),
                ('name', models.CharField(max_length=100, verbose_name='user_name')),
                ('surname', models.CharField(max_length=100, verbose_name='user_surname')),
                ('email', models.CharField(max_length=255, unique=True, verbose_name='user_email')),
                ('phone', apps.core.fields.aes_text_field.AesTextField(null=True, verbose_name='user_phone')),
                ('is_active', models.BooleanField(default=False, verbose_name='user_is_active')),
                ('is_vpn', models.BooleanField(default=False, verbose_name='user_is_vpn')),
                ('is_2fa', models.BooleanField(default=False, verbose_name='user_is_2fa')),
                ('is_temporary', models.BooleanField(default=False, verbose_name='user_is_temporary')),
                ('source', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('ldap', 'ldap'), ('db', 'db')], default=apps.core.models.user.User.Source['DB'], enum_class=apps.core.models.user.User.Source, max_length=4, verbose_name='user_source')),
                ('additional_data', apps.core.fields.aes_json_field.AesJSONField(null=True, verbose_name='user_additional_data')),
                ('active_to', models.DateTimeField(null=True, verbose_name='user_active_to')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
                'default_permissions': (),
            },
            managers=[
                ('objects', apps.core.managers.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('platform', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('ios', 'ios'), ('android', 'android'), ('web', 'web'), ('external', 'external')], default=apps.core.models.api_key.ApiKey.DevicePlatformEnum['WEB'], enum_class=apps.core.models.api_key.ApiKey.DevicePlatformEnum, max_length=8)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('secret', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'api_key',
                'verbose_name_plural': 'api_keys',
                'db_table': 'api_keys',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, verbose_name='device_name')),
                ('certificate', apps.core.fields.aes_text_field.AesTextField(max_length=50, verbose_name='device_certificate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_devices', to='core.User', verbose_name='device_user')),
            ],
            options={
                'verbose_name': 'device',
                'verbose_name_plural': 'devices',
                'db_table': 'devices',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='language_code')),
                ('name', models.CharField(max_length=50, verbose_name='language_name')),
                ('bundle', models.CharField(max_length=5, verbose_name='language_bundle')),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
                'db_table': 'languages',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(default='', max_length=50)),
                ('module', models.CharField(default='', max_length=50)),
                ('function', models.CharField(default='', max_length=50)),
                ('filename', models.CharField(default='', max_length=50)),
                ('message', models.TextField(default='', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('status_code', models.IntegerField(null=True, verbose_name='log_entry_status_code')),
                ('request_body', apps.core.fields.aes_json_field.AesJSONField(null=True, verbose_name='log_entry_request_body')),
                ('username', models.CharField(max_length=100, null=True, verbose_name='log_entry_username')),
            ],
            options={
                'db_table': 'log_entries',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, verbose_name='project_name')),
                ('is_vpn', models.BooleanField(default=False, verbose_name='project_is_vpn')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'db_table': 'projects',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, verbose_name='service_name')),
                ('type', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('db', 'db'), ('ssh', 'ssh')], default=apps.core.models.service.Service.ServiceType['DB'], enum_class=apps.core.models.service.Service.ServiceType, max_length=3, verbose_name='service_type')),
                ('variables', apps.core.fields.aes_json_field.AesJSONField(null=True, verbose_name='service_variables')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
                'db_table': 'services',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='UserProjectDevice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_projects', to='core.Device', verbose_name='devices')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_devices', to='core.Project', verbose_name='projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_devices', to='core.User', verbose_name='users')),
            ],
            options={
                'verbose_name': 'users_projects_devices',
                'verbose_name_plural': 'users_projects_devices',
                'db_table': 'users_projects_devices',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('active_2fa', models.BooleanField(default=False, verbose_name='token-active-2fa')),
                ('expires_at', models.DateTimeField(blank=True, null=True, verbose_name='token_expires_at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to='core.User', verbose_name='token_user')),
            ],
            options={
                'db_table': 'tokens',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Remote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, verbose_name='remote_name')),
                ('host', apps.core.fields.aes_text_field.AesTextField(verbose_name='remote_host')),
                ('port', apps.core.fields.aes_text_field.AesTextField(null=True, verbose_name='remote_port')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remotes', to='core.Service', verbose_name='remote_services')),
            ],
            options={
                'verbose_name': 'remote',
                'verbose_name_plural': 'remotes',
                'db_table': 'remotes',
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='project',
            name='remotes',
            field=models.ManyToManyField(related_name='projects', to='core.Remote', verbose_name='projects_remotes'),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Language', verbose_name='user_language'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]