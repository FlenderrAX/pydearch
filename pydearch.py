from colorama import init, Fore, Style
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests
import re
import sys

init(autoreset=True)

def scrap_emails(url: str):
    EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    webLink = url
    parsed_url = urlparse(webLink)

    if not parsed_url.scheme:
        webLink = f"http://{webLink}"
    
    try:
        webRequest = requests.get(webLink)
    except requests.exceptions.RequestException as e:
        print(f"An error has occurred: {e}")
        sys.exit()

    soup = BeautifulSoup(webRequest.content, 'html.parser')
    emails = re.findall(EMAIL_REGEX, soup.get_text())
    result = emails if emails else "No Email found."

    return result

def scrap_link(url: str):
    webLink = url
    parsed_url = urlparse(webLink)

    if not parsed_url.scheme:
        webLink = f"http://{webLink}"
    
    try:
        webRequest = requests.get(webLink)
    except requests.exceptions.RequestException as e:
        print(f"An error has occurred: {e}")
        sys.exit()

    soup = BeautifulSoup(webRequest.content, 'html.parser')
    links = [urljoin(webLink, a['href']) for a in soup.find_all('a', href=True)]
    result = links if links else "No URL found."

    return result

def scrap_email_url(url: str):
    EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    webLink = url
    parsed_url = urlparse(webLink)

    if not parsed_url.scheme:
        webLink = f"http://{webLink}"

    try:
        webRequest = requests.get(webLink)
    except requests.exceptions.RequestException as e:
        print(f"An error has occurred: {e}")
        sys.exit()

    soup = BeautifulSoup(webRequest.content, 'html.parser')

    links = [urljoin(webLink, a['href']) for a in soup.find_all('a', href=True)]
    emails = re.findall(EMAIL_REGEX, soup.get_text())

    urlResult = links if links else "No URL found."
    emailResult = emails if emails else "No Email found."

    return (urlResult, emailResult)

logo = r"""
 /$$$$$$$  /$$     /$$ /$$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$
| $$__  $$|  $$   /$$/| $$__  $$| $$_____/ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$
| $$  \ $$ \  $$ /$$/ | $$  \ $$| $$      | $$  \ $$| $$  \ $$| $$  \__/| $$  | $$
| $$$$$$$/  \  $$$$/  | $$  | $$| $$$$$   | $$$$$$$$| $$$$$$$/| $$      | $$$$$$$$
| $$____/    \  $$/   | $$  | $$| $$__/   | $$__  $$| $$__  $$| $$      | $$__  $$
| $$          | $$    | $$  | $$| $$      | $$  | $$| $$  \ $$| $$    $$| $$  | $$
| $$          | $$    | $$$$$$$/| $$$$$$$$| $$  | $$| $$  | $$|  $$$$$$/| $$  | $$
|__/          |__/    |_______/ |________/|__/  |__/|__/  |__/ \______/ |__/  |__/                                                                                                          
"""

print(Fore.CYAN + logo)

menu = f"""
{Fore.YELLOW}[+] {Fore.GREEN}Scrap Emails {Fore.YELLOW}[0]
{Fore.YELLOW}[+] {Fore.GREEN}Scrap URLs {Fore.YELLOW}[1]
{Fore.YELLOW}[+] {Fore.GREEN}Scrap Emails & URLs {Fore.YELLOW}[2]
{Fore.YELLOW}[+] {Fore.GREEN}Exit {Fore.YELLOW}[3]
"""

print(menu)

try:
    choice = int(input(Fore.CYAN + "=> "))

    match choice:

        case 0:
            print("Please enter your " + Fore.RED + "link " + Fore.RESET + ": ")
            userLink = input("")
            print(
                scrap_emails(userLink)
                )
            
        case 1:
            print("Please enter your " + Fore.RED + "link " + Fore.RESET + ": ")
            userLink = input("")
            links = scrap_link(userLink)
            
            print(
                "========================"
            )
            for link in links:
                print(
                    f"[+] {link}"
                )

        case 2:
            print("Please enter your " + Fore.RED + "link " + Fore.RESET + ": ")
            userLink = input("")

            URLs = scrap_email_url(userLink)[0]
            Emails = scrap_email_url(userLink)[1]

            print(
                "========================"
                )
            if type(URLs) == list:
                for link in URLs:
                    print(
                        f"[+] {link}"
                    )
            else:
                print(URLs)

            print(
                "========================"
                )
            if type(Emails) == list:
                for email in Emails:
                    print(
                        f"[+] {email}"
                    )
            else:
                print(Emails)

        case 3:
            print(Fore.RED + "Successfully exited.")
            sys.exit()
        case _:
            print(Fore.RED + "Invalid choice. Please enter a number between 0 and 3.")
except ValueError:
    print(Fore.RED + "Invalid input. Please enter a number.")