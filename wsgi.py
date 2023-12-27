import sys

# Add your project directory to the sys.path
project_home = '/home/nigelmashozhera1/Cv'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import your Flask app and rename it to "application" for WSGI
from main import app as application
  