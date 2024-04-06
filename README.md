# CPSC-449-Exercise-1

This Python program is designed to demonstrate the interaction with REST and GraphQL APIs using the Python `requests` library. Developed for CPSC-449 Web Backend Engineering at California State University, Fullerton, this tool allows querying a music database, showcasing how to retrieve data about artists, albums, tracks, and genres.

## Music Database Query Exercise

## Features

- **REST API Interaction:**

  - Retrieves information about artists, albums, tracks, genres, and playlists from a music database.
  - Constructs and sends GET requests to retrieve data based on specific filters.
  - Parses JSON responses to extract and display relevant data.

- **GraphQL API Interaction:**
  - Sends GraphQL queries to a different endpoint to fetch data about artists, albums, and tracks.
  - Demonstrates how to construct and send queries to a GraphQL API and how to handle the returned data.
  - Specifically, it can find albums by "Red Hot Chili Peppers," genres associated with "U2," and details about the "Grunge" playlist.

## Operating System Compatibility

This program was tested on Ubuntu Linux.

## Prerequisites for Running Program

Before running the scripts, ensure the following prerequisites are met:

1. Download and extract the Chinook SQLite sample database:

   - `wget https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip`
   - `unzip chinook.zip`

2. Install SQLite:

   - `sudo apt update`
   - `sudo apt install --yes sqlite3`
   - Verify the database: `sqlite3 chinook.db .dump`

3. Set up the Python virtual environment:

   - Install pip and venv: `sudo apt install --yes python3-pip python3-venv`
   - Create and activate the virtual environment:
     - `python3.10 -m venv $HOME/.venv`
     - `echo 'source $HOME/.venv/bin/activate' | tee -a $HOME/.bashrc`
     - `. $HOME/.venv/bin/activate`

4. Install n version manager for Node.js and update npm:

   - `curl -s -L http://git.io/n-install | bash -s -- -y`
   - `. $HOME/.bashrc`
   - `npm update --global`

5. Install servers for the REST and GraphQL APIs:
   - `npm install --global soul-cli`
   - `npm install --global tuql`

## Running the APIs

1. Start the API servers in two separate terminals:

   - For REST API: `soul --database chinook.db --studio`
   - For GraphQL API: `tuql --db chinook.db --graphiql`

2. Access the following interfaces in your web browser when API servers are running:
   - [Soul Studio GUI](http://localhost:8000/studio) - A visual interface for the Soul API.
   - [Soul API Documentation](http://localhost:8000/api/docs) - Documentation and testing tool for the REST API.
   - [GraphQL IDE for tuql](http://localhost:4000/graphql) - An interactive editor for GraphQL queries.

## How to Use Python Files

1. Ensure that the APIs are running and accessible at the specified URLs (`http://localhost:8000/api/` for REST and `http://localhost:4000/graphql/` for GraphQL).
2. Execute the script. The program will automatically make requests to the APIs to fetch and display data based on predefined queries for both REST and GraphQL endpoints.

## Dependencies

- Python 3.x
- `requests` library: if not already installed, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Note

This tool is purely educational and demonstrates the use of the `requests` library in Python to interact with REST APIs. The code is structured for easy understanding and modification for further experimentation with API requests.
