import requests

def fetch_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            subdomains = set(entry["name_value"] for entry in data)
            return subdomains
        else:
            print("Error: Unable to fetch data from crt.sh")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    domain = input("Enter the target domain (e.g., example.com): ")
    subdomains = fetch_subdomains(domain)
    
    if subdomains:
        print("\n[+] Found Subdomains:")
        for sub in sorted(subdomains):
            print(sub)

        # Save results to a file
        with open("subdomains.txt", "w") as f:
            for sub in sorted(subdomains):
                f.write(sub + "\n")
        
        print("\n[+] Subdomains saved in 'subdomains.txt'")
    else:
        print("\n[-] No subdomains found.")

if __name__ == "__main__":
    main()
