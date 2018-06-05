# Generated by Django 2.0.1 on 2018-03-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dayv2Pub',
            fields=[
                ('houseid', models.CharField(max_length=20)),
                ('personid', models.CharField(max_length=10)),
                ('frsthm', models.CharField(max_length=10)),
                ('outoftwn', models.CharField(max_length=10)),
                ('ontd_p1', models.CharField(max_length=10)),
                ('ontd_p2', models.CharField(max_length=10)),
                ('ontd_p3', models.CharField(max_length=10)),
                ('ontd_p4', models.CharField(max_length=10)),
                ('ontd_p5', models.CharField(max_length=10)),
                ('ontd_p6', models.CharField(max_length=10)),
                ('ontd_p7', models.CharField(max_length=10)),
                ('ontd_p8', models.CharField(max_length=10)),
                ('ontd_p9', models.CharField(max_length=10)),
                ('ontd_p10', models.CharField(max_length=10)),
                ('ontd_p11', models.CharField(max_length=10)),
                ('ontd_p12', models.CharField(max_length=10)),
                ('ontd_p13', models.CharField(max_length=10)),
                ('ontd_p14', models.CharField(max_length=10)),
                ('ontd_p15', models.CharField(max_length=10)),
                ('tdcaseid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('hh_hisp', models.CharField(max_length=10)),
                ('hh_race', models.CharField(max_length=10)),
                ('driver', models.CharField(max_length=10)),
                ('r_sex', models.CharField(max_length=10)),
                ('worker', models.CharField(max_length=10)),
                ('drvrcnt', models.CharField(max_length=10)),
                ('hhfaminc', models.CharField(max_length=10)),
                ('hhsize', models.CharField(max_length=10)),
                ('hhvehcnt', models.CharField(max_length=10)),
                ('numadlt', models.CharField(max_length=10)),
                ('flag100', models.CharField(max_length=10)),
                ('lif_cyc', models.CharField(max_length=10)),
                ('trippurp', models.CharField(max_length=10)),
                ('awayhome', models.CharField(max_length=10)),
                ('cdivmsar', models.CharField(max_length=10)),
                ('census_d', models.CharField(max_length=10)),
                ('census_r', models.CharField(max_length=10)),
                ('drop_prk', models.CharField(max_length=10)),
                ('drvr_flg', models.CharField(max_length=10)),
                ('educ', models.CharField(max_length=10)),
                ('endtime', models.CharField(max_length=10)),
                ('hh_ontd', models.CharField(max_length=10)),
                ('hhmemdrv', models.CharField(max_length=10)),
                ('hhresp', models.CharField(max_length=10)),
                ('hhstate', models.CharField(max_length=10)),
                ('hhstfips', models.CharField(max_length=10)),
                ('intstate', models.CharField(max_length=10)),
                ('msacat', models.CharField(max_length=10)),
                ('msasize', models.CharField(max_length=10)),
                ('nonhhcnt', models.CharField(max_length=10)),
                ('numontrp', models.CharField(max_length=10)),
                ('paytoll', models.CharField(max_length=10)),
                ('prmact', models.CharField(max_length=10)),
                ('proxy', models.CharField(max_length=10)),
                ('psgr_flg', models.CharField(max_length=10)),
                ('r_age', models.CharField(max_length=10)),
                ('rail', models.CharField(max_length=10)),
                ('strttime', models.CharField(max_length=10)),
                ('tracc1', models.CharField(max_length=10)),
                ('tracc2', models.CharField(max_length=10)),
                ('tracc3', models.CharField(max_length=10)),
                ('tracc4', models.CharField(max_length=10)),
                ('tracc5', models.CharField(max_length=10)),
                ('tracctm', models.CharField(max_length=10)),
                ('travday', models.CharField(max_length=10)),
                ('tregr1', models.CharField(max_length=10)),
                ('tregr2', models.CharField(max_length=10)),
                ('tregr3', models.CharField(max_length=10)),
                ('tregr4', models.CharField(max_length=10)),
                ('tregr5', models.CharField(max_length=10)),
                ('tregrtm', models.CharField(max_length=10)),
                ('trpaccmp', models.CharField(max_length=10)),
                ('trphhacc', models.CharField(max_length=10)),
                ('trphhveh', models.CharField(max_length=10)),
                ('trptrans', models.CharField(max_length=10)),
                ('trvl_min', models.CharField(max_length=10)),
                ('trvlcmin', models.CharField(max_length=10)),
                ('trwaittm', models.CharField(max_length=10)),
                ('urban', models.CharField(max_length=10)),
                ('urbansize', models.CharField(max_length=10)),
                ('urbrur', models.CharField(max_length=10)),
                ('useintst', models.CharField(max_length=10)),
                ('usepubtr', models.CharField(max_length=10)),
                ('vehid', models.CharField(max_length=10)),
                ('whodrove', models.CharField(max_length=10)),
                ('whyfrom', models.CharField(max_length=10)),
                ('whyto', models.CharField(max_length=10)),
                ('whytrp1s', models.CharField(max_length=10)),
                ('wrkcount', models.CharField(max_length=10)),
                ('dweltime', models.CharField(max_length=10)),
                ('whytrp90', models.CharField(max_length=10)),
                ('tdtrpnum', models.CharField(max_length=10)),
                ('tdwknd', models.CharField(max_length=10)),
                ('tdaydate', models.CharField(max_length=10)),
                ('trpmiles', models.CharField(max_length=50)),
                ('wttrdfin', models.CharField(max_length=50)),
                ('vmt_mile', models.CharField(max_length=50)),
                ('pubtrans', models.CharField(max_length=10)),
                ('homeown', models.CharField(max_length=10)),
                ('hometype', models.CharField(max_length=10)),
                ('hbhur', models.CharField(max_length=10)),
                ('htresdn', models.CharField(max_length=10)),
                ('hthtnrnt', models.CharField(max_length=10)),
                ('htppopdn', models.CharField(max_length=10)),
                ('hteempdn', models.CharField(max_length=10)),
                ('hbresdn', models.CharField(max_length=10)),
                ('hbhtnrnt', models.CharField(max_length=10)),
                ('hbppopdn', models.CharField(max_length=10)),
                ('gasprice', models.CharField(max_length=10)),
                ('vehtype', models.CharField(max_length=10)),
                ('hh_cbsa', models.CharField(max_length=10)),
                ('hhc_msa', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'dayv2pub',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            name='Hhv2Pub',
            fields=[
                ('houseid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('varstrat', models.CharField(max_length=10)),
                ('wthhfin', models.CharField(max_length=50)),
                ('drvrcnt', models.CharField(max_length=10)),
                ('cdivmsar', models.CharField(max_length=10)),
                ('census_d', models.CharField(max_length=10)),
                ('census_r', models.CharField(max_length=10)),
                ('hh_hisp', models.CharField(max_length=10)),
                ('hh_race', models.CharField(max_length=10)),
                ('hhfaminc', models.CharField(max_length=10)),
                ('hhrelatd', models.CharField(max_length=10)),
                ('hhresp', models.CharField(max_length=10)),
                ('hhsize', models.CharField(max_length=10)),
                ('hhstate', models.CharField(max_length=10)),
                ('hhstfips', models.CharField(max_length=10)),
                ('hhvehcnt', models.CharField(max_length=10)),
                ('homeown', models.CharField(max_length=10)),
                ('hometype', models.CharField(max_length=10)),
                ('msacat', models.CharField(max_length=10)),
                ('msasize', models.CharField(max_length=10)),
                ('numadlt', models.CharField(max_length=10)),
                ('rail', models.CharField(max_length=10)),
                ('resp_cnt', models.CharField(max_length=10)),
                ('scresp', models.CharField(max_length=10)),
                ('travday', models.CharField(max_length=10)),
                ('urban', models.CharField(max_length=10)),
                ('urbansize', models.CharField(max_length=10)),
                ('urbrur', models.CharField(max_length=10)),
                ('wrkcount', models.CharField(max_length=10)),
                ('tdaydate', models.CharField(max_length=10)),
                ('flag100', models.CharField(max_length=10)),
                ('lif_cyc', models.CharField(max_length=10)),
                ('cnttdhh', models.CharField(max_length=10)),
                ('hbhur', models.CharField(max_length=10)),
                ('htresdn', models.CharField(max_length=10)),
                ('hthtnrnt', models.CharField(max_length=10)),
                ('htppopdn', models.CharField(max_length=10)),
                ('hteempdn', models.CharField(max_length=10)),
                ('hbresdn', models.CharField(max_length=10)),
                ('hbhtnrnt', models.CharField(max_length=10)),
                ('hbppopdn', models.CharField(max_length=10)),
                ('hh_cbsa', models.CharField(max_length=10)),
                ('hhc_msa', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'hhv2pub',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perv2Pub',
            fields=[
                ('houseid', models.CharField(max_length=20)),
                ('personid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('varstrat', models.CharField(max_length=10)),
                ('wtperfin', models.CharField(max_length=50)),
                ('sfwgt', models.CharField(max_length=50)),
                ('hh_hisp', models.CharField(max_length=10)),
                ('hh_race', models.CharField(max_length=10)),
                ('drvrcnt', models.CharField(max_length=10)),
                ('hhfaminc', models.CharField(max_length=10)),
                ('hhsize', models.CharField(max_length=10)),
                ('hhvehcnt', models.CharField(max_length=10)),
                ('numadlt', models.CharField(max_length=10)),
                ('wrkcount', models.CharField(max_length=10)),
                ('flag100', models.CharField(max_length=10)),
                ('lif_cyc', models.CharField(max_length=10)),
                ('cnttdtr', models.CharField(max_length=10)),
                ('borninus', models.CharField(max_length=10)),
                ('carrode', models.CharField(max_length=10)),
                ('cdivmsar', models.CharField(max_length=10)),
                ('census_d', models.CharField(max_length=10)),
                ('census_r', models.CharField(max_length=10)),
                ('condnigh', models.CharField(max_length=10)),
                ('condpub', models.CharField(max_length=10)),
                ('condride', models.CharField(max_length=10)),
                ('condrive', models.CharField(max_length=10)),
                ('condspec', models.CharField(max_length=10)),
                ('condtax', models.CharField(max_length=10)),
                ('condtrav', models.CharField(max_length=10)),
                ('deliver', models.CharField(max_length=10)),
                ('diary', models.CharField(max_length=10)),
                ('disttosc', models.CharField(max_length=10)),
                ('driver', models.CharField(max_length=10)),
                ('dtacdt', models.CharField(max_length=10)),
                ('dtconj', models.CharField(max_length=10)),
                ('dtcost', models.CharField(max_length=10)),
                ('dtrage', models.CharField(max_length=10)),
                ('dtran', models.CharField(max_length=10)),
                ('dtwalk', models.CharField(max_length=10)),
                ('educ', models.CharField(max_length=10)),
                ('everdrov', models.CharField(max_length=10)),
                ('flextime', models.CharField(max_length=10)),
                ('fmscsize', models.CharField(max_length=10)),
                ('frsthm', models.CharField(max_length=10)),
                ('fxdwkpl', models.CharField(max_length=10)),
                ('gcdwork', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=10)),
                ('gt1jblwk', models.CharField(max_length=10)),
                ('hhresp', models.CharField(max_length=10)),
                ('hhstate', models.CharField(max_length=10)),
                ('hhstfips', models.CharField(max_length=10)),
                ('issue', models.CharField(max_length=10)),
                ('occat', models.CharField(max_length=10)),
                ('lsttrday', models.CharField(max_length=10)),
                ('mcused', models.CharField(max_length=10)),
                ('medcond', models.CharField(max_length=10)),
                ('medcond6', models.CharField(max_length=10)),
                ('moroften', models.CharField(max_length=10)),
                ('msacat', models.CharField(max_length=10)),
                ('msasize', models.CharField(max_length=10)),
                ('nbiketrp', models.CharField(max_length=10)),
                ('nwalktrp', models.CharField(max_length=10)),
                ('outcntry', models.CharField(max_length=10)),
                ('outoftwn', models.CharField(max_length=10)),
                ('payprof', models.CharField(max_length=10)),
                ('prmact', models.CharField(max_length=10)),
                ('proxy', models.CharField(max_length=10)),
                ('ptused', models.CharField(max_length=10)),
                ('purchase', models.CharField(max_length=10)),
                ('r_age', models.CharField(max_length=10)),
                ('r_relat', models.CharField(max_length=10)),
                ('r_sex', models.CharField(max_length=10)),
                ('rail', models.CharField(max_length=10)),
                ('sameplc', models.CharField(max_length=10)),
                ('schcare', models.CharField(max_length=10)),
                ('schcrim', models.CharField(max_length=10)),
                ('schdist', models.CharField(max_length=10)),
                ('schspd', models.CharField(max_length=10)),
                ('schtraf', models.CharField(max_length=10)),
                ('schtrn1', models.CharField(max_length=10)),
                ('schtrn2', models.CharField(max_length=10)),
                ('schtyp', models.CharField(max_length=10)),
                ('schwthr', models.CharField(max_length=10)),
                ('self_emp', models.CharField(max_length=10)),
                ('timetosc', models.CharField(max_length=10)),
                ('timetowk', models.CharField(max_length=10)),
                ('toscsize', models.CharField(max_length=10)),
                ('travday', models.CharField(max_length=10)),
                ('urban', models.CharField(max_length=10)),
                ('urbansize', models.CharField(max_length=10)),
                ('urbrur', models.CharField(max_length=10)),
                ('useintst', models.CharField(max_length=10)),
                ('usepubtr', models.CharField(max_length=10)),
                ('webuse', models.CharField(max_length=10)),
                ('wkfmhmxx', models.CharField(max_length=10)),
                ('wkftpt', models.CharField(max_length=10)),
                ('wkrmhm', models.CharField(max_length=10)),
                ('wkstfips', models.CharField(max_length=10)),
                ('worker', models.CharField(max_length=10)),
                ('wrktime', models.CharField(max_length=10)),
                ('wrktrans', models.CharField(max_length=10)),
                ('yearmile', models.CharField(max_length=10)),
                ('yrmlcap', models.CharField(max_length=10)),
                ('yrtous', models.CharField(max_length=10)),
                ('disttowk', models.CharField(max_length=10)),
                ('tdaydate', models.CharField(max_length=15)),
                ('homeown', models.CharField(max_length=10)),
                ('hometype', models.CharField(max_length=10)),
                ('hbhur', models.CharField(max_length=5)),
                ('htresdn', models.CharField(max_length=10)),
                ('hthtnrnt', models.CharField(max_length=10)),
                ('htppopdn', models.CharField(max_length=10)),
                ('hteempdn', models.CharField(max_length=10)),
                ('hbresdn', models.CharField(max_length=10)),
                ('hbhtnrnt', models.CharField(max_length=10)),
                ('hbppopdn', models.CharField(max_length=10)),
                ('hh_cbsa', models.CharField(max_length=10)),
                ('hhc_msa', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'perv2pub',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehv2Pub',
            fields=[
                ('houseid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('wthhfin', models.CharField(max_length=50)),
                ('vehid', models.CharField(max_length=10)),
                ('drvrcnt', models.CharField(max_length=10)),
                ('hhfaminc', models.CharField(max_length=10)),
                ('hhsize', models.CharField(max_length=10)),
                ('hhvehcnt', models.CharField(max_length=10)),
                ('numadlt', models.CharField(max_length=10)),
                ('flag100', models.CharField(max_length=10)),
                ('cdivmsar', models.CharField(max_length=10)),
                ('census_d', models.CharField(max_length=10)),
                ('census_r', models.CharField(max_length=10)),
                ('hhstate', models.CharField(max_length=10)),
                ('hhstfips', models.CharField(max_length=10)),
                ('hybrid', models.CharField(max_length=10)),
                ('makecode', models.CharField(max_length=10)),
                ('modlcode', models.CharField(max_length=10)),
                ('msacat', models.CharField(max_length=10)),
                ('msasize', models.CharField(max_length=10)),
                ('od_read', models.CharField(max_length=10)),
                ('rail', models.CharField(max_length=10)),
                ('travday', models.CharField(max_length=10)),
                ('urban', models.CharField(max_length=10)),
                ('urbansize', models.CharField(max_length=10)),
                ('urbrur', models.CharField(max_length=10)),
                ('vehcomm', models.CharField(max_length=10)),
                ('vehownmo', models.CharField(max_length=50)),
                ('vehyear', models.CharField(max_length=10)),
                ('whomain', models.CharField(max_length=10)),
                ('wrkcount', models.CharField(max_length=10)),
                ('tdaydate', models.CharField(max_length=15)),
                ('vehage', models.CharField(max_length=10)),
                ('personid', models.CharField(max_length=10)),
                ('hh_hisp', models.CharField(max_length=10)),
                ('hh_race', models.CharField(max_length=10)),
                ('homeown', models.CharField(max_length=10)),
                ('hometype', models.CharField(max_length=10)),
                ('lif_cyc', models.CharField(max_length=10)),
                ('annmiles', models.CharField(max_length=50)),
                ('hbhur', models.CharField(max_length=10)),
                ('htresdn', models.CharField(max_length=10)),
                ('hthtnrnt', models.CharField(max_length=10)),
                ('htppopdn', models.CharField(max_length=10)),
                ('hteempdn', models.CharField(max_length=10)),
                ('hbresdn', models.CharField(max_length=10)),
                ('hbhtnrnt', models.CharField(max_length=10)),
                ('hbppopdn', models.CharField(max_length=10)),
                ('best_flg', models.CharField(max_length=10)),
                ('bestmile', models.CharField(max_length=20)),
                ('best_edt', models.CharField(max_length=10)),
                ('best_out', models.CharField(max_length=10)),
                ('fueltype', models.CharField(max_length=10)),
                ('gsyrgal', models.CharField(max_length=10)),
                ('gscost', models.CharField(max_length=10)),
                ('gstotcst', models.CharField(max_length=10)),
                ('epatmpg', models.CharField(max_length=50)),
                ('epatmpgf', models.CharField(max_length=10)),
                ('eiadmpg', models.CharField(max_length=10)),
                ('vehtype', models.CharField(max_length=10)),
                ('hh_cbsa', models.CharField(max_length=10)),
                ('hhc_msa', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'vehv2pub',
                'managed': False,
            },
        ),
    ]