# Generated by Django 5.0.2 on 2024-02-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engage_Partners_Table',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('province', models.TextField()),
                ('category', models.TextField()),
                ('name_of_partner_or_office', models.TextField()),
                ('address', models.TextField()),
                ('contact_person', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.TextField()),
                ('date_engaged', models.DateField()),
                ('engagement_mode', models.TextField()),
                ('loi', models.TextField()),
                ('remarks', models.TextField()),
            ],
            options={
                'db_table': 'Engage_Partners_Table',
            },
        ),
        migrations.CreateModel(
            name='Intern_Table',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('province', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=200)),
                ('ojt_duration', models.IntegerField()),
                ('school_address', models.CharField(max_length=200)),
                ('contact_person', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('mode', models.CharField(max_length=20)),
                ('recommendation_letter', models.BooleanField(default=False)),
                ('application_form', models.BooleanField(default=False)),
                ('cv_resume', models.BooleanField(default=False)),
                ('medical_certificate', models.BooleanField(default=False)),
                ('workplan_form', models.BooleanField(default=False)),
                ('interview_form', models.BooleanField(default=False)),
                ('acceptance_letter', models.BooleanField(default=False)),
                ('wfh_arrangement', models.BooleanField(default=False)),
                ('nda', models.BooleanField(default=False)),
                ('work_assignment_form', models.BooleanField(default=False)),
                ('war', models.BooleanField(default=False)),
                ('timesheet', models.BooleanField(default=False)),
                ('coc', models.BooleanField(default=False)),
                ('remarks', models.TextField()),
            ],
            options={
                'db_table': 'Intern_Table',
            },
        ),
        migrations.CreateModel(
            name='Training_Webinars_Table',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('province', models.CharField(max_length=255)),
                ('course_name', models.CharField(max_length=255)),
                ('training_track', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('time', models.TimeField()),
                ('total_num_hours', models.IntegerField()),
                ('nga_m', models.IntegerField()),
                ('nga_f', models.IntegerField()),
                ('suc_m', models.IntegerField()),
                ('suc_f', models.IntegerField()),
                ('lgu_m', models.IntegerField()),
                ('lgu_f', models.IntegerField()),
                ('others_m', models.IntegerField()),
                ('others_f', models.IntegerField()),
                ('total_m', models.IntegerField()),
                ('total_f', models.IntegerField()),
                ('total_participants', models.IntegerField()),
                ('participants_list', models.TextField()),
                ('attendance_sheet', models.TextField()),
                ('group_photo', models.TextField()),
                ('implementation_mode', models.CharField(max_length=255)),
                ('certificates_issued', models.IntegerField()),
                ('resource_persons', models.TextField()),
                ('resource_persons_cv', models.TextField()),
                ('course_officers', models.TextField()),
                ('course_officers_email', models.TextField()),
                ('remarks', models.TextField()),
            ],
            options={
                'db_table': 'Training_Webinars_Table',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=240)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=250)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]