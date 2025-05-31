import os

from django.core.wsgi import get_wsgi_application

# Add these lines for PythonAnywhere deployment
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler
# End of lines for PythonAnywhere deployment

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_config.settings')

# Modify this line for PythonAnywhere deployment
if settings.DEBUG:
    application = get_wsgi_application()
else:
    application = StaticFilesHandler(get_wsgi_application())
# End of modification for PythonAnywhere deployment 