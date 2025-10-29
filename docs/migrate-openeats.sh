#!/bin/sh

/usr/local/bin/python /code/manage.py migrate admin 0003_logentry_add_action_flag_choices
/usr/local/bin/python /code/manage.py migrate auth 0012_alter_user_first_name_max_length
/usr/local/bin/python /code/manage.py migrate authtoken 0003_tokenproxy
/usr/local/bin/python /code/manage.py migrate contenttypes 0002_remove_content_type_name
/usr/local/bin/python /code/manage.py migrate sessions 0001_initial
/usr/local/bin/python /code/manage.py migrate sites 0002_alter_domain_unique

/usr/local/bin/python /code/manage.py migrate recipe 0021_photo_auto_resize
/usr/local/bin/python /code/manage.py migrate recipe_groups 0004_auto_20220514_1110
/usr/local/bin/python /code/manage.py migrate ingredient 0013_auto_20220514_1110
/usr/local/bin/python /code/manage.py migrate rating 0005_rating_timestamp_remove_defaults
/usr/local/bin/python /code/manage.py migrate menu 0011_auto_20220514_1110
/usr/local/bin/python /code/manage.py migrate list 0011_auto_20220514_1110
/usr/local/bin/python /code/manage.py migrate news 0004_auto_20220514_1110
