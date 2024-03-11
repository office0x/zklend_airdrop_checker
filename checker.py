import requests

def airdrop_status(address):
    url = f"https://data.app.zklend.com/airdrop/{address}"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    # Load addresses from wallets.txt
    with open('wallets.txt', 'r') as file:
        addresses = file.read().splitlines()

    # Iterate over addresses and print results
    for address in addresses:
        result = airdrop_status(address)
        if result != None:
            print(f"{address} Eligible")
        else:
            print(f"{address} 0")


if __name__ == "__main__":
    main()
