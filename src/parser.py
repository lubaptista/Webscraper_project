from bs4 import BeautifulSoup

def parse_html(html_content):
    soup = BeautifulSoup(html_content, "lxml")
    return soup
