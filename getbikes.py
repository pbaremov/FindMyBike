# this file provides functions that will scrap through the html
# of the pinkbikes.com website and will find all the images of bicycles
#

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
bikes_list = []
front_tags = []

def get_bikes(page):
    """
    The function bellow deals with pagination in the web scrapping part.
    it returns a list that holds the urls of every individual bike posted on the website
    and the fron tags of the ad. Front tags are intended to be used for future visualization of the results
    """
    url = f"https://www.pinkbike.com/buysell/list/?region=5&page={page}&category=75"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    bikes = soup.find_all(
        "tr", {"class": "bsitem-table"}
    )  # 'bsitem-title' is common class for all the bikes on the page

    for item in bikes:
        bike = item.find("a")["href"]
        front_tag = item.find("img")["src"]
        bikes_list.append(bike)
        front_tags.append(front_tag)

    return (
        bikes_list,
        front_tags,
    )  # bikes_list holds a list with all the urls of each individual bike - 324 seconds


def get_images_titles(i):
    """
        This function returs the urls of every image that is contained in the bikie ad, as well as the bike title
    image urls will be used for the later predictions and the titles for the visualization

    """
    bike_images = []
    r = requests.get(i, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    bike_title = soup.find("h1", {"class", "buysell-title"}).text
    thumbnail_images = soup.find_all("div", class_="buysell-thumbnailimage")
    if thumbnail_images is None:
        pass
    # Extract the background-image URLs
    image_urls = [img["style"].split("'")[1] for img in thumbnail_images]
    bike_images.append(image_urls)
    return image_urls, bike_title


