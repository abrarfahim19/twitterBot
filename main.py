from fetch_data import fetch_ethereum_price
from twitter_bot import tweet_ethereum_price

if __name__ == "__main__":
    # Fetch Ethereum price from the API
    ethereum_price = fetch_ethereum_price()
    print(ethereum_price)

    # Tweet the Ethereum price
    tweet_ethereum_price(ethereum_price)
