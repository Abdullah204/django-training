from celery import app
from django.core.mail import send_mail
from musicplatform.settings import EMAIL_HOST_USER
from artists.models import Artist
from django.db.models import Max
from django.utils import timezone
from datetime import timedelta
from celery import shared_task

@shared_task
def album_creation_check():
    for artist in Artist.objects.prefetch_related('album').all():
        latest_album = artist.album_set.aggregate(Max('release_datetime'))
        if(timezone.now() - timedelta(days=30) > latest_album["release_datetime__max"]):
            msg = 'Artist:'
            msg += artist.stage_name +" "
            msg += + "your popularity is decreasing on our platform because you arent uploading new album for a while"
            send_mail(
            'Important Note',msg,'',[artist.user.email],
            fail_silently=False)