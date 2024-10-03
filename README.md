
# Twitter Media Dumper

A Python-based tool for downloading media (images, videos) from Twitter profiles, hashtags, and timelines. Due to limitations on the free Twitter API, this project originally aimed to fetch media from tweets but now focuses on available API endpoints or alternate methods like web scraping.

## Features

- Fetch media (images and videos) from user profiles or hashtags using Twitter's API or web scraping (future implementation).
- Filter media by type (images or videos) and date range.
- Save media locally in a structured directory.
- Dockerized for easy deployment.
- Unit tests for key functionality.

## Installation

### Prerequisites
- Python 3.10+
- Twitter Developer Account with API access (v2)
- pip (Python package installer)
- Docker (optional for containerized usage)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/JorkDev/twitter-media-dumper.git
   cd twitter-media-dumper
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Twitter API credentials:
   ```
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   TWITTER_ACCESS_TOKEN=your_bearer_token  # Use the Bearer Token for v2
   ```

## Usage

Run the script to fetch media from a specific user or timeline:
```bash
python src/main.py
```

In `main.py`, adjust the parameters such as the Twitter username, media type, and date range.

Example:
```python
fetch_media_from_tweets_v2(
    client, 
    query='from:elonmusk', 
    media_type='images', 
    start_time='2023-01-01T00:00:00Z', 
    end_time='2024-01-01T00:00:00Z'
)
```

## Docker Usage

1. Build the Docker image:
   ```bash
   docker build -t twitter-media-dumper .
   ```

2. Run the Docker container with your `.env` file:
   ```bash
   docker run --env-file=.env twitter-media-dumper
   ```

## Running Tests

Unit tests are included for core functionalities. To run tests:
```bash
pytest
```

## Future Plans

- Implement web scraping functionality to fetch tweets and media without API limitations.
- Add more advanced filtering options.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
