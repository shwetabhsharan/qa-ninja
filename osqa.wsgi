import os
import sys
sys.path.append('/home/shwetabh/workspace/qa-ninja')
sys.path.append('/home/shwetabh/workspace/qa-ninja/qa-ninja/osqa-server')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

