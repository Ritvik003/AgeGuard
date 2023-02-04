from bs4 import BeautifulSoup
from urllib.request import urlopen

#enter in dummy url for now, this will be modified in chrome extension to accept any url

#url = "https://www.azfamily.com/2023/01/27/arizona-dps-troopers-bust-over-160-pounds-drugs-3-traffic-stops/"

url = "https://www.pornhub.com/view_video.php?viewkey=ph63b4cd6330ad1"

#this is a very simple content restriction program

def flag_text(host) :
    buzz = ["fuck", "shit", "bitch", "cunt", "pussy", "asshole", "pornographic", "whore", "death", "dead", "drugs", "cocaine", "meth",
            "methamphetamine", "marijuana", "rape", "trafficking", "heroin", "gunned", "sex"]
    page = urlopen(host)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text()
    print(text)
    
    for word in buzz:
        if text.find(word) != -1:
            print("hi")
            return True
    
    return False
        
flag_text(url)


