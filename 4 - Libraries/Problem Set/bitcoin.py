import sys
import requests

def main():
    bitcoin_input = cli_validation_and_input()
    bitcoin_price = api_bitcoin_price_request()
    total_cost_in_dollars = bitcoin_input * bitcoin_price
    print(f"${total_cost_in_dollars:,.4f}")

def cli_validation_and_input():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        try:
            return float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

def api_bitcoin_price_request():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.ConnectionError:
        print("Connection Error")
    except requests.RequestException:
        print("Other Request Error")
    else:
        return response["bpi"]["USD"]["rate_float"]

if __name__ == "__main__":
    main()