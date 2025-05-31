import os
import sys

# Add your project directory to the sys.path
path = '/home/DaEtoJostka/blog_609-31_KarlovIA'  # IMPORTANT: Change this to your actual project path on PythonAnywhere
if path not in sys.path:
    sys.path.insert(0, path)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'app_config.settings'

# Import the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 