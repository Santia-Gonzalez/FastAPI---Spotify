from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from spotipy.oauth2 import SpotifyClientCredentials
from fastapi.responses import JSONResponse

from dotenv import load_dotenv
import os
import spotipy

load_dotenv()

# Traemos las variables del .env a nuestro módulo
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
# Configuración de las credenciales de Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def homepage():
    html_content = """ <!DOCTYPE html> 
        <html lang="en"> 
            <head> 
                <meta charset="UTF-8"> 
                <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
                <title>Homepage</title> 
                <style> 
                    body { 
                        font-family: Arial, 
                        sans-serif; 
                        background-color: #f0f0f0; 
                        color: #333; 
                        margin: 0; 
                        padding: 0; 
                        display: flex; 
                        justify-content: center; 
                        align-items: center; 
                        height: 100vh; 
                        text-align: center; 
                    } 
                    .container { 
                        background-color: #ffffff; 
                        padding: 20px; 
                        border-radius: 10px; 
                        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
                    } 
                    h1 { 
                        color: #007BFF; 
                    } 
                    p { font-size: 1.2em; } 
                </style> 
            </head> 
            <body> 
                <div class="container"> 
                    <h1> WELCOME TO THE PRINCIPAL PAGE!</h1> 
                    <p>Try with the next endpoints: </p> 
                    <p style="display: center"> 1 ./ (Homepage) </p> 
                    <p style="display: center"> 2 ./top-tracks/{artist} (Top tracks of one artist) </p> 
                    <p style="display: center"> 3 ./songs-by-genre/{genre} (Top songs by genre) </p>
                    <p style="display: center"> 4 ./albums/{artist} (Top 5 albums) </p>
                </div> 
            </body> 

        </html> 
    """ 
    return html_content

@app.get("/top-tracks/{nombre}")
async def top_tracks(nombre: str):
    result = sp.search(q=nombre, type='artist', limit=1)
    artist_id = result['artists']['items'][0]['id']
    results = sp.artist_top_tracks(artist_id, country='CO')
    tracks = [track['name'] for track in results['tracks']]
    return JSONResponse({'top-tracks': tracks})

@app.get("/related-artists/{name}")
async def related_artists(name: str):
    result = sp.search(q= name, type='artist', limit=1)
    artist_id = result['artists']['items'][0]['id']
    results = sp.artist_related_artists(artist_id)
    artists = [artist['name'] for artist in results['tracks']]
    return JSONResponse({'related-artists': artists})

@app.get("/songs-by-genre/{genre}")
async def songs_by_genre(genre: str):
    result = sp.search(q=f"genero:{genre}", type='track', market='CO', limit=10)
    tracks = [{'name': track['name'], 'artist': track['artists'][0]['name']} for track in result['tracks']['items']]
    return JSONResponse({'tracks': tracks})

@app.get("/albums/{name}")
async def artist_albums(name: str):
    result = sp.search(q=name, type='artist', limit=1)
    artist_id = result['artists']['items'][0]['id']
    results = sp.artist_albums(artist_id=artist_id, limit=5, country='CO')
    albums = [{'name': album['name'], 'release_date': album['release_date'], 'total_tracks': album['total_tracks']} for album in results['items']]
    return JSONResponse({'Albumes': albums})    
