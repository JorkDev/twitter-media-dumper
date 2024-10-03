from config import validate_credentials

if __name__ == '__main__':
    try:
        validate_credentials()
        print("Twitter API credentials loaded successfully!")
    except ValueError as e:
        print(f"Error: {e}")
