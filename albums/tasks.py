from celery import shared_task
from django.core.mail import send_mail
from musicplatform.settings import EMAIL_HOST_USER
from artists.models import Artist
@shared_task
def congratulate_artist(id,album_name ,release_datetime , cost):
    print("congrats")
    artist = Artist.objects.get(user_id = id)
    msg = 'We would like to congratulate you for your new album: '
    msg += album_name +" released: " + release_datetime  
    msg +=  " " + "with cost: " + str(cost)
    send_mail('Congrats',msg,EMAIL_HOST_USER,[artist.user.email],    fail_silently=False,
)

