from dotenv import load_dotenv
from typing import Optional
import os
import requests

load_dotenv()
BEARER = os.getenv("BEARER_TOKEN")

def get_data(screen_name: str, count: int) -> Optional[dict]:
    """
    Get data from Twitter API
    
    Parameters
    ----------
    screen_name : str
        Twitter screen name
    count : int
        Number of tweets to get
    
    Returns
    -------
    dict : Optional[dict] (Union[None, dict])
        Dictionary containing the data from the API
    """
    url = f"https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {"screen_name": screen_name, "count": count}
    headers = {"Authorization": f"Bearer {BEARER}"}
    response = requests.get(url, params=params, headers=headers)
    return response.json()

def main() -> None:
    """
    Main function
    """
    screen_name = "LogarithmeNeper"
    count = 10
    data = get_data(screen_name, count)
    if data is not None:
        print(data)

if __name__ == "__main__":
    main()