Imports:
>>> from artists.models import Artist  
>>> from albums.models import Album  
 # note  : other imports are written directly before it is used
Inserts:
>>> b = Artist(stage_name='artist1', social_link_field='https://www.instagram.com/artist1/')<br />
>>> b.save()<br />
>>> b = Artist(stage_name='artist2', social_link_field='https://www.instagram.com/artist2/')<br />
>>> b.save()<br />
>>> b = Artist(stage_name='artist3', social_link_field='https://www.instagram.com/artist3/')<br />
>>> b.save()<br />
>>> b = Artist(stage_name='artist4', social_link_field='https://www.instagram.com/artist4/')<br />
>>> b.save()<br />
>>> b = Artist(stage_name='artist5', social_link_field='https://www.instagram.com/artist5/')<br />
>>> b.save()<br />
>>> b = Artist(stage_name='artist0', social_link_field='https://www.instagram.com/artist0/')<br />
>>> b.save()<br />

list down all artists:
>>> Artist.objects.all()
<QuerySet [<Artist: artist0 https://www.instagram.com/artist0/>,
<Artist: artist1 https://www.instagram.com/artist1/>,
<Artist: artist2 https://www.instagram.com/artist2/>,
<Artist: artist3 https://www.instagram.com/artist3/>,
<Artist: artist4 https://www.instagram.com/artist4/>,
<Artist: artist5 https://www.instagram.com/artist5/>]>

>>> Artist.objects.all().values()
<QuerySet [{'id': 6, 'stage_name': 'artist0', 'social_link_field': 'https://www.instagram.com/artist0/'},
{'id': 1, 'stage_name': 'artist1', 'social_link_field': 'https://www.instagram.com/artist1/'},
{'id': 2, 'stage_name': 'artist2', 'social_link_field': 'https://www.instagram.com/artist2/'},
{'id': 3, 'stage_name': 'artist3', 'social_link_field': 'https://www.instagram.com/artist3/'},
{'id': 4, 'stage_name': 'artist4', 'social_link_field': 'https://www.instagram.com/artist4/'},
{'id': 5, 'stage_name': 'artist5', 'social_link_field': 'https://www.instagram.com/artist5/'}]>

list down all artists sorted by name:
>>> Artist.objects.all().order_by('stage_name').values()
<QuerySet [{'id': 6, 'stage_name': 'artist0',
 'social_link_field': 'https://www.instagram.com/artist0/'},
{'id': 1, 'stage_name': 'artist1', 'social_link_field': 'https://www.instagram.com/artist1/'},
{'id': 2, 'stage_name': 'artist2', 'social_link_field': 'https://www.instagram.com/artist2/'},
{'id': 3, 'stage_name': 'artist3', 'social_link_field': 'https://www.instagram.com/artist3/'},
{'id': 4, 'stage_name': 'artist4', 'social_link_field': 'https://www.instagram.com/artist4/'},
{'id': 5, 'stage_name': 'artist5', 'social_link_field': 'https://www.instagram.com/artist5/'}]>


list down all artists whose name starts with `a`:
>>> Artist.objects.filter(stage_name__startswith='A')
<QuerySet [<Artist: artist0 https://www.instagram.com/artist0/>,
 <Artist: artist1 https://www.instagram.com/artist1/>,
  <Artist: artist2 https://www.instagram.com/artist2/>,
   <Artist: artist3 https://www.instagram.com/artist3/>,
    <Artist: artist4 https://www.instagram.com/artist4/>, 
    <Artist: artist5 https://www.instagram.com/artist5/>]>
>>> Artist.objects.filter(stage_name__startswith='a')
<QuerySet [<Artist: artist0 https://www.instagram.com/artist0/>, <Artist: artist1 https://www.instagram.com/artist1/>, <Artist: artist2 https://www.instagram.com/artist2/>, <Artist: artist3 https://www.instagram.com/artist3/>, <Artist: artist4 https://www.instagram.com/artist4/>, <Artist: artist5 https://www.instagram.com/artist5/>]>
>>> Artist.objects.filter(stage_name__startswith='b')
<QuerySet []>
# notice : its not case sensitive
# note the second query (starts with 'b') wasnt required but I wrote it to make sure the filter is working correctly

in 2 different ways, create some albums and assign them to any artists 
(hint: use `objects` manager and use the related object reference):

first way:
>>>import pytz , datetime (also had to add pytz in poetry)


>>> album1 = Album(name="album1" , release_datetime =datetime.datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),cost=12.5)
>>> album2 = Album(name="album2" , release_datetime =datetime.datetime(2014, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),cost=15.5)
>>> album1.save()
>>> album2.save()

>>> artist1 = Artist.objects.get(id=1)
>>> artist1.album_set.add(album1)
>>> artist1.album_set.add(album2)


second way:

>>> artist2 = Artist.objects.get(id=2)
>>> album3 = Album(name="album3" , release_datetime =datetime.datetime(2011, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),cost=10.5,artist =artist2)
>>> album4 = Album(name="album4" , release_datetime =datetime.datetime(2012, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),cost=5.5,artist =artist2)
>>> album3.save()
>>> album4.save()


get the latest released album:


>>> from django.db.models import Max
>>> Album.objects.aggregate(Max('release_datetime'))
{'release_datetime__max': datetime.datetime(2014, 11, 20, 20, 8, 7, 127325, tzinfo=datetime.timezone.utc)}

get all albums released before today:

>>> from django.utils import timezone
>>> Album.objects.filter(release_datetime__lt= timezone.now())
<QuerySet [<Album: 2 album2>, <Album: 5 album1>, <Album: 6 album3>, <Album: 7 album4>]>



get all albums released today or before but not after today:
>>> Album.objects.filter(release_datetime__lte= timezone.now())
<QuerySet [<Album: 2 album2>, <Album: 5 album1>, <Album: 6 album3>, <Album: 7 album4>]>



count the total number of albums (hint: count in an optimized manner)
#note use count instead of len as len internally makes select * from table == O(N) , 
whereas count makes select count(*) which complexity is O(1)

>>> Album.objects.count()
4



in 2 different ways, for each artist, list down all of his/her albums 
(hint: use `objects` manager and use the related object reference)

first way:
>>> for obj in Artist.objects.all():
...     print(obj.album_set.all())
...


<QuerySet []>
<QuerySet [<Album: 2 album2>, <Album: 5 album1>]>
<QuerySet [<Album: 6 album3>, <Album: 7 album4>]>
<QuerySet []>
<QuerySet []>
<QuerySet []>

#note : album id isnt equal to number in name because I deleted some albums



second way:

>>> for alb in Album.objects.all():
...     print(alb.name , alb.artist.stage_name)
... 
album2 artist1
album1 artist1
album3 artist2
album4 artist2



list down all albums ordered by cost then by name (cost has the higher priority):


>>> Album.objects.all().order_by('cost','name')
<QuerySet [<Album: 7 album4>, <Album: 6 album3>, <Album: 5 album1>, <Album: 2 album2>]>

