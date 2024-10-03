import os
import sys
import requests
from unittest.mock import patch, mock_open
from src.main import save_media
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import save_media, fetch_media_from_tweets

@patch('requests.get')
@patch('builtins.open', new_callable=mock_open)
def test_save_media(mock_file, mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.iter_content = lambda chunk_size: [b'data']

    save_media('https://x.com/elonmusk/status/1841742540774768916', 'media', 'media1.jpg')

    mock_file.assert_called_once_with(os.path.join('media', 'media1.jpg'), 'wb')
    mock_file().write.assert_called()

    mock_get.assert_called_once_with('https://x.com/elonmusk/status/1841742540774768916', stream=True)
