from urllib.request import urlretrieve
import os
import bs4
import requests
import regex as re
from io import StringIO  
import argparse

parser = argparse.ArgumentParser(description='Download NOAA data')
parser.add_argument('-a', type=bool, default=False, help='download all data')
parser.add_argument('-y', '--year', type=str, default=2024, help='year to download')
args = parser.parse_args()


def download_noaa(year):
    url = f"https://www.ncei.noaa.gov/pub/data/noaa/{year}/"
    r = requests.get(url)
    data = bs4.BeautifulSoup(r.text, "html.parser")
    print(r.status_code)

    # place above url text into file
    noaa_doc = data.get_text()
    noaa_file = StringIO(noaa_doc)
    noaa_links = re.findall(r"\d{6}-\d{5}-\d{4}.gz|A\d{5}-\d{5}-\d{4}.gz", noaa_file.read())

    # year = noaa_links[0][13:17]
    os.mkdir(f"../data/{year}")
    for i, j in zip(noaa_links, range(5)):
        urlretrieve(url + i, f"../data/{year}/" + i)


if __name__ == "__main__":
    if args.a == True:
        url = "https://www.ncei.noaa.gov/pub/data/noaa/"
        years = [i for i in range(1901, 2024)]
        for year in years:
            download_noaa(year)
    elif len(args.year) == 4:
        download_noaa(args.year)

    else:
        years = re.findall(r'\d{4}', args.year)
        for year in years:
            download_noaa(year)
