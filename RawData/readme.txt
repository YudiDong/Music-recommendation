1. Information type.
As you all noticed, all the Yahoo music data are in numerical form.
There are 4 different type total, user_id, item_id, item_rating, item_count.
Item means it can be track, album, artist, or genre.
"None" in the data means cannot find the item. Similar to the "NULL" in the database.

2. albumData2.txt
item_id(album)|item_id(artist)|item_id(genre)|...|item_id(genre)

3. artistData2.txt
item_id(artist)

4. genreData2.txt
item_id(genre)

5. testIdx2.txt
user_id | item_count
item_id
item_id
item_id
item_id
item_id
item_id
user_id | item_count
......

6. testTrack_hierarchy.txt
user_id | item_id(track) | item_id(album) | item_id(artist) | item_id(genre) | item_id(genre) | .....

7. trackData.2txt
item_id(track) | item_id(album) | item_id(artist) | item_id(genre) | item_id(genre) | ......

8. trainIdx2.txt
Be careful in this file, you cannot tell if a item_id is track, album, artist or genre.
user_id | item_count
item_id item_rating
item_id item_rating
.....
user_id | item_count
.......
