import requests 

# url for REST API
retrieveID = "http://localhost:8000/api/tables/artists/rows?_filters=Name:Red%20Hot%20Chili%20Peppers"
retrieveAlbums = ""

# use get to retrieve information
response = requests.get(retrieveID)

rhcp = response.json()
# artistID = rhcp.get("ArtistID")

if response.status_code == 200:
    print("Success!")
    print(rhcp)