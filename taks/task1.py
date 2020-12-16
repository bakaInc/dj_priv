import django
print(django.get_version())

import os
print(os.environ)

# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings' # mod_wsgi
# django-admin runserver --settings=mysite.settings
from django.conf import settings
settings.configure()
# print(settings)  # DJANGO_SETTINGS_MODULE / settings.configure()
print(dir(settings))
print(settings.PASSWORD_HASHERS)
# https://docs.djangoproject.com/en/3.1/ref/settings/



