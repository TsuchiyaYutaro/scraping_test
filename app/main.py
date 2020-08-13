from urllib import request
from bs4 import BeautifulSoup

def _parse_url(x):
    x = x.split('channel/')[1]
    x = x.split('?sub_confirmation')[0]
    return x

if __name__ == '__main__':
    top_url = "https://nijisanji.ichikara.co.jp/member/"
    top_html = request.urlopen(top_url)
    top_soup = BeautifulSoup(top_html, "html.parser")
    top_links = top_soup.body.find_all('a')

    liver_link_list = []
    for link in top_links:
        if 'href' in link.attrs:
            liver_link_list.append(link.attrs['href'])
        
    liver_link_list = [i for i in liver_link_list if 'https://nijisanji.ichikara.co.jp/member/' in i][1:]

    liver_list = []
    for i in liver_link_list:
        liver_html = request.urlopen(i)
        liver_soup = BeautifulSoup(liver_html, "html.parser")
        liver_name = liver_soup.body.find_all(class_='elementor-heading-title elementor-size-default')[0].text
        liver_link = liver_soup.body.find_all('a')

        channel_id = []

        for link in liver_link:
            if 'href' in link.attrs:
                channel_id.append(link.attrs['href'])

        channel_id = [i for i in channel_id if 'https://www.youtube.com/channel/' in i][0]
        channel_id = _parse_url(channel_id)

        liver_list.append([liver_name, channel_id])

    print(liver_list)