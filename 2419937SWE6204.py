import os
import sys
from django.core.management import execute_from_command_line

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personalised_news.settings')
    execute_from_command_line(['manage.py', 'runserver'])

if __name__ == '__main__':
    main()
