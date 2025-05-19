#!/usr/bin/env python
"""Entry point for Django's command-line utilities."""
import os
import sys

def main():
    """Set up the environment and handle admin commands."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personalised_news.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "added to your PYTHONPATH environment. Also check if your "
            "virtual environment is properly activated."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
