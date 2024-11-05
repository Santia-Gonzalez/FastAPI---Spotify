# FastAPI Project with Spotipy

This project uses FastAPI to create an API that interacts with the Spotify API through the Spotipy library.

## Requirements

- Python 3.9
- Conda
- A Spotify account and Spotify API credentials (client ID and client secret)

## Environment Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/FastAPI---Spotify.git
    cd your-repository
    ```

2. Create the Conda environment:
    ```sh
    conda env create -f environment.yml
    ```

3. Activate the environment:
    ```sh
    conda activate FastAPI
    ```

## Spotify Credentials

1. Obtain your client ID and client secret from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

2. Create a `.env` file in the root directory of the project and add your credentials:
    ```plaintext
    SPOTIPY_CLIENT_ID='your_client_id'
    SPOTIPY_CLIENT_SECRET='your_client_secret'
    ```

## Running the Application

1. Start the server:
    ```sh
    fastapi dev main.py
    ```

2. Access the API:
    - [http://localhost:8000](http://localhost:8000)

## Available Endpoints ##

### Homepage

- **Path**: `/`
- **Method**: GET
- **Description**: Returns to the homepage
- **Example**:
    ```sh
    GET /songs-by-genre/rock
    ```

### Top Tracks

- **Path**: `/top-tracks/{artist}`
- **Method**: GET
- **Description**: Returns the top tracks of a specific artist in the Colombian market.
- **Example**:
    ```sh
    GET /top-tracks/Maluma
    ```

### Get Songs by Genre

- **Path**: `/songs-by-genre/{genre}`
- **Method**: GET
- **Description**: Returns the top 10 tracks of a specific genre in the Colombian market.
- **Example**:
    ```sh
    GET /songs-by-genre/rock
    ```

### Get Albums of an Artist

- **Path**: `/albums/{name}`
- **Method**: GET
- **Description**: Returns the top 5 albums of a specific artist in the Colombian market.
- **Example**:
    ```sh
    GET /albums/Coldplay
    ```

## Notes

- Ensure your Spotify credentials are correctly set up in the `.env` file.
- If you encounter any issues, check the server logs for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

---

I hope this helps you set up and run your project smoothly! If you have any other questions or need further assistance, feel free to ask. 😊
