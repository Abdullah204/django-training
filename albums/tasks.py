from celery import shared_task
from django.core.mail import send_mail
from musicplatform.settings import EMAIL_HOST_USER
from artists.models import Artist
from django.utils import timezone
from datetime import timedelta
from django.db.models import Max

@shared_task
def congratulate_artist(id,album_name ,release_datetime , cost):
    artist = Artist.objects.get(user_id = id)
    msg = 'We would like to congratulate you for your new album: '
    msg += album_name +" released: " + release_datetime  
    msg +=  " " + "with cost: " + str(cost)
    send_mail('Congrats',msg,EMAIL_HOST_USER,[artist.user.email],    fail_silently=False,
)

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