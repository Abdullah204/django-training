#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# from artists.models import Artist
# from albums.models import Album
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# Artist.objects.all().delete()
# b = Artist(stage_name='artist1', social_link_field='https://www.instagram.com/artist1/')
# b.save()
# b = Artist(stage_name='artist0', social_link_field='https://www.instagram.com/artist0/')
# b.save()
# b = Artist(stage_name='artist3', social_link_field='https://www.instagram.com/artist3/')
# b.save()
# b = Artist(stage_name='artist4', social_link_field='https://www.instagram.com/artist4/')
# b.save()
# b = Artist(stage_name='artist5', social_link_field='https://www.instagram.com/artist5/')
# b.save()

# all_artists = Artist.objects.all()
# print(all_artists)
