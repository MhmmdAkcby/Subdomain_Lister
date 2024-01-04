# Subdomain Finder

This Python script utilizes a wordlist to find subdomains for a target domain. It makes HTTP requests to each combination of subdomain and target domain and prints the ones that return a response.

## Prerequisites
Make sure you have the following installed:

- Python (>=3.6)
- requests library

Install the required library using:

```bash
pip install requests


## Usage

--> Clone the repository:
git clone https://github.com/yourusername/subdomain-finder.git
cd subdomain-finder

--> Run the script:
python subdomain_finder.py

## Configuration
You can customize the script by modifying the target_input and subdomainlist.txt file.

target_input: The main domain for which you want to find subdomains.
subdomainlist.txt: A list of subdomains you want to check.
