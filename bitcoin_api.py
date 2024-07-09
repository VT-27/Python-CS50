import sys
import requests
import json

def main():
    if len(sys.argv) !=2:
        print("Missing command-line argument")
        sys.exit()
    
    if isinstance(sys.argv[1], float):
        print("Command-line argument is not a number")
        sys.exit()

    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        #print(json.dumps(response.json(), indent=2))

        # Parse the JSON data into a Python dictionary
        #formated_data = json.loads(data)

        # Extract and print the rate for USD
        usd_rate = data['bpi']['USD']['rate']

        # Convert the string rate to float
        rate_float = float(usd_rate.replace(',', ''))

        arg = float(sys.argv[1].replace(',', ''))
        final_rate = rate_float * arg

        print(f"${final_rate:,.4f}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

main()