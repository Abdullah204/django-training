# Imports:
>>> from artists.models import Artist  <br />
>>> from albums.models import Album  <br />
 note  : other imports are written directly before it is used
# Inserts:
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

# list down all artists:<br />
>>> Artist.objects.all()<br />
<QuerySet [<Artist: artist0 https://www.instagram.com/artist0/>, <br />
<Artist: artist1 https://www.instagram.com/artist1/>,<br />
<Artist: artist2 https://www.instagram.com/artist2/>,<br />
<Artist: artist3 https://www.instagram.com/artist3/>,<br />
<Artist: artist4 https://www.instagram.com/artist4/>,<br />
<Artist: artist5 https://www.instagram.com/artist5/>]><br />

>>> Artist.objects.all().values()<br />
<QuerySet [{'id': 6, 'stage_name': 'artist0', 'social_link_field': 'https://www.instagram.com/artist0/'},<br />
{'id': 1, 'stage_name': 'artist1', 'social_link_field': 'https://www.instagram.com/artist1/'},<br />
{'id': 2, 'stage_name': 'artist2', 'social_link_field': 'https://www.instagram.com/artist2/'},<br />
{'id': 3, 'stage_name': 'artist3', 'social_link_field': 'https://www.instagram.com/artist3/'},<br />
{'id': 4, 'stage_name': 'artist4', 'social_link_field': 'https://www.instagram.com/artist4/'},<br />
{'id': 5, 'stage_name': 'artist5', 'social_link_field': 'https://www.instagram.com/artist5/'}]><br />

# list down all artists sorted by name:<br />
>>> Artist.objects.all().order_by('stage_name').values()<br />
<QuerySet [{'id': 6, 'stage_name': 'artist0',<br />
 'social_link_field': 'https://www.instagram.com/artist0/'},<br />
{'id': 1, 'stage_name': 'artist1', 'social_link_field': 'https://www.instagram.com/artist1/'},<br />
{'id': 2, 'stage_name': 'artist2', 'social_link_field': 'https://www.instagram.com/artist2/'},<br />
{'id': 3, 'stage_name': 'artist3', 'social_link_field': 'https://www.instagram.com/artist3/'},<br />
{'id': 4, 'stage_name': 'artist4', 'social_link_field': 'https://www.instagram.com/artist4/'},<br />
{'id': 5, 'stage_name': 'artist5', 'social_link_field': 'https://www.instagram.com/artist5/'}]><br />


# list down all artists whose name starts with `a`:<br />
>>> Artist.objects.filter(stage_name__startswith='A')<br />
<QuerySet [<Artist: artist0 https://www.instagram.com/artist0/>,<br />
 <Artist: artist1 https://www.instagram.com/artist1/>,<br />
  <Artist: artist2 https://www.instagram.com/artist2/>,<br />
   <Artist: artist3 https://www.instagram.com/artist3/>,<br />
    <Artist: artist4 https://www.instagram.com/artist4/>, <br />
    <Artist: artist5 https://www.instagram.com/artist5/>]><br />
>>> Artist.objects.filter(stage_name__startswith='a')<br />
<QuerySet [<Artist: artist0 https://www.instagram.com/artist0/>, <br/> <Artist: artist1 https://www.instagram.com/artist1/>,<br />
<Artist: artist2 https://www.instagram.com/artist2/>,<br />
<Artist: artist3 https://www.instagram.com/artist3/>,<br />
<Artist: artist4 https://www.instagram.com/artist4/>, <br />
<Artist: artist5 https://www.instagram.com/artist5/>]><br />

>>> Artist.objects.filter(stage_name__startswith='b')<br />
<QuerySet []>
 notice : its not case sensitive <br/>
 note the second query (starts with 'b') wasnt required but I wrote it to make sure the filter is working correctly

# in 2 different ways, create some albums and assign them to any artists <br />
(hint: use `objects` manager and use the related object reference):<br />

# first way:<br />
>>>import pytz , datetime (also had to add pytz in poetry)<br />


>>> album1 = Album(name="album1" , release_datetime =datetime.datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),cost=12.5)<br />
>>> album2 = Album(name="album2" , release_datetime =datetime.datetime(2014, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),cost=15.5)<br />
>>> album1.save()<br />
>>> album2.save()<br />

>>> artist1 = Artist.objects.get(id=1)<br />
>>> artist1.album_set.add(album1)<br />
>>> artist1.album_set.add(album2)<br />


# second way:<br />
<br />
>>> artist2 = Artist.objects.get(id=2)<br />
>>> album3 = Album(name="album3" , release_datetime =datetime.datetime(2011, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),cost=10.5,artist =artist2)<br />
>>> album4 = Album(name="album4" , release_datetime =datetime.datetime(2012, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),cost=5.5,artist =artist2)<br />
>>> album3.save()<br />
>>> album4.save()
<br />

# get the latest released album:<br /><br />


>>> from django.db.models import Max<br />
>>> Album.objects.aggregate(Max('release_datetime'))<br />
{'release_datetime__max': datetime.datetime(2014, 11, 20, 20, 8, 7, 127325, tzinfo=datetime.timezone.utc)}<br />

# get all albums released before today:<br />

>>> from django.utils import timezone<br />
>>> Album.objects.filter(release_datetime__lt= timezone.now())<br />
<QuerySet [<Album: 2 album2>, <Album: 5 album1>, <Album: 6 album3>, <Album: 7 album4>]><br />



# get all albums released today or before but not after today:<br /><br />
>>> Album.objects.filter(release_datetime__lte= timezone.now())<br />
<QuerySet [<Album: 2 album2>, <Album: 5 album1>, <Album: 6 album3>, <Album: 7 album4>]><br />



# count the total number of albums (hint: count in an optimized manner)<br /><br />
#note use count instead of len as len internally makes select * from table == O(N) , <br />
whereas count makes select count(*) which complexity is O(1)<br /><br />

>>> Album.objects.count()
4
<br /><br />


# in 2 different ways, for each artist, list down all of his/her albums 
(hint: use `objects` manager and use the related object reference)<br /><br />

# first way:<br />
>>> for obj in Artist.objects.all():<br />
...     print(obj.album_set.all())<br />
...<br />


<QuerySet []><br />
<QuerySet [<Album: 2 album2>, <Album: 5 album1>]><br />
<QuerySet [<Album: 6 album3>, <Album: 7 album4>]><br />
<QuerySet []><br />
<QuerySet []><br />
<QuerySet []><br />

note : album id isnt equal to number in name because I deleted some albums
<br /><br />


# second way:<br /><br />

>>> for alb in Album.objects.all():<br />
...     print(alb.name , alb.artist.stage_name)<br />
... <br />
album2 artist1<br />
album1 artist1<br />
album3 artist2<br />
album4 artist2<br />
<br />


# list down all albums ordered by cost then by name (cost has the higher priority):<br /><br />


>>> Album.objects.all().order_by('cost','name')<br />
<QuerySet [<Album: 7 album4>, <Album: 6 album3>, <Album: 5 album1>, <Album: 2 album2>]><br />

<br />
