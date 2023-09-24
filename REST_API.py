import requests 

# url for REST API
REST_URL = "http://localhost:8000/api/"

artistTable = "tables/artists/rows"
albumsTable = "tables/albums/rows"
tracksTable = "tables/tracks/rows"
genresTable = "tables/genres/rows"
playlistTable = "tables/playlists/rows"
playlist_trackTable = "tables/playlist_track/rows"
retrieveID = {"_filters": "Name:Red Hot Chili Peppers"}

# use get to retrieve information
response = requests.get(REST_URL + artistTable, params={"_filters": "Name:Red Hot Chili Peppers"})

# convert response to json
rhcp = response.json()

# get artist ID
artist_info = rhcp.get('data')
artistID = artist_info[0].get('ArtistId')

# now find albums by RHCP
response = requests.get(REST_URL + albumsTable, params={"_filters": "ArtistId:" + str(artistID)})

# convert response to json
rhcp = response.json()

# print albums
print("Albums by the artist Red Hot Chili Peppers:")
albums_info = rhcp.get('data')
for album in albums_info:
    print(album.get('Title'))

# beginning of second REST API call 
response = requests.get(REST_URL + artistTable, params={"_filters": "Name:U2"})

# convert response to json
u2 = response.json()

# get artist ID
artist_info = u2.get('data')
artistID = artist_info[0].get('ArtistId')

# now we find all the albums by U2
response = requests.get(REST_URL + albumsTable, params={"_filters": "ArtistId:" + str(artistID)})

# convert response to json
u2 = response.json()

# retrieve albums ids
albums_info = u2.get('data')
albumIDs = []
for album in albums_info:
    albumIDs.append(album.get('AlbumId'))

# convert albumIDs to string
albumIDs = ','.join(map(str, albumIDs))

# now we find all the genres associated with the albums
response = requests.get(REST_URL + tracksTable, params={"_filters": "AlbumId:[" + albumIDs + "]", "_limit":"135", "_extend": "GenreId"})
u2 = response.json()

# now we store the genres in a list
genres = set()
tracks_info = u2.get('data')
for track in tracks_info:
    genres.add(track.get('GenreId'))

# lastly, find the name of the genres 
response = requests.get(REST_URL + genresTable, params={"_filters": "GenreId:[" + ','.join(map(str, genres)) + "]"})
u2 = response.json()

# print the results to the screen 
print("\nGenres associated with the artist U2:")
genres_info = u2.get('data')
for genre in genres_info:
    print(genre.get('Name'))

# beginning of final REST API call 
response = requests.get(REST_URL + playlistTable, params={"_filters": "Name:Grunge"})
Grunge = response.json()

# get playlist ID
playlist_info = Grunge.get('data')
playlistID = playlist_info[0].get('PlaylistId')

# now we retrieve all the tracks on the playlist
response = requests.get(REST_URL + playlist_trackTable, params={"_filters": "PlaylistId:" + str(playlistID), "_extend": "TrackId", "_limit": "15"})
Grunge = response.json()

# store track ids 
tracks_info = Grunge.get('data')
trackIDs = []
for track in tracks_info:
    trackIDs.append(track.get('TrackId'))

# retrieve track names and albums id 
response = requests.get(REST_URL + tracksTable, params={"_filters": "TrackId:[" + ','.join(map(str, trackIDs)) + "]", "_extend": "AlbumId", "_limit": "15"})
Grunge = response.json()

# store track names and albums id
tracks_info = Grunge.get('data')
trackNames = []
albumIDs = []
for track in tracks_info:
    trackNames.append(track.get('Name'))
    albumIDs.append(track.get('AlbumId'))

# print the results to the screen
print("\nNames of tracks on the playlist Grunge and their associated artist and album:")
for track in trackNames:
    response = requests.get(REST_URL + tracksTable, params={"_filters": "Name:" + track, "_extend": "AlbumId", "_limit": "15"})
    Grunge = response.json()
    tracks_info = Grunge.get('data')
    album_ID = tracks_info[0]['AlbumId']
    album_name = tracks_info[0]['AlbumId_data']['Title']
    response = requests.get(REST_URL + albumsTable, params={"_filters": "AlbumId:" + str(album_ID), "_extend": "ArtistId", "_limit": "15"})
    Grunge = response.json()
    albums_info = Grunge.get('data')
    artist_ID = albums_info[0]['ArtistId_data']['Name']
    print(track + " by " + artist_ID + " is part of the album: " + album_name)

# end of REST API calls