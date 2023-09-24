import requests 

# url for GraphQL API
GRAPHQL_URL = "http://localhost:4000/graphql/"


# Define your GraphQL query for artists
albumsQuery = """
{
  artists(where: { name: "Red Hot Chili Peppers" }) {
    albums {
        title
    }
  }
}
"""

# Send the GraphQL query
response = requests.get(GRAPHQL_URL, json={"query": albumsQuery})

# Parse the JSON response
RHCP = response.json()
albums = RHCP["data"]["artists"][0]["albums"]

# Print the albums by RHCP
print("Albums by the artist Red Hot Chili Peppers:")
for album in albums:
    print(album["title"])

# beginning of second GraphQL API call
genresQuery = """
{
  artist (where: {name: "U2"}) {
    albums {
      tracks {
        genre {
          genreId
          name
        }
      }
    }
  }
}
"""

# Send the GraphQL query
response = requests.get(GRAPHQL_URL, json={"query": genresQuery})

# create set to store genres
genres = set()

# Parse the JSON response
U2 = response.json()
for album in U2["data"]["artist"]["albums"]:
    for track in album["tracks"]:
        genres.add(track["genre"]["name"])

# print genres associated with U2
print("\nGenres associated with the artist U2:")
for genre in genres:
    print(genre)

# beginning of last GraphQL API call
grungeQuery = """
{
  playlists (where: {Name: "Grunge"}) {
   	tracks {
      name
     	album {
        title
        artist {
          name
        }
      } 
    }
  }
}
"""

# Send the GraphQL query
response = requests.get(GRAPHQL_URL, json={"query": grungeQuery})

# Parse the JSON response
Grunge = response.json()
# print track name, album title, artist name
print("\nNames of tracks on the playlist Grunge and their associated artist and album:")
for track in Grunge["data"]["playlists"][0]["tracks"]:
    print(track["name"] + " by " + track["album"]["artist"]["name"] + " is part of the album " + track["album"]["title"])

# end of GraphQL API calls