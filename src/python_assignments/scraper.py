import requests
from bs4 import BeautifulSoup as bs

print("This scraper will return the profile image link of the GitHub user.")

github_user_name = input("Enter the GitHub username: ")
url = f"https://github.com/{github_user_name}"  # Fixed URL

# Send request with user-agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
r = requests.get(url, headers=headers)

# Check if the page exists
if r.status_code == 200:
    soup = bs(r.content, 'html.parser')

    # Updated method to find profile image
    image_tag = soup.find('img', class_="avatar avatar-user width-full border color-bg-default")
    
    if image_tag:
        profile_image = image_tag['src']
        print("Profile Image URL:", profile_image)
    else:
        print("No profile image found! (Maybe username is incorrect or profile has no picture.)")
else:
    print("GitHub profile not found! Check the username.")
