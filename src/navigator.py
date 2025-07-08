from bs4 import BeautifulSoup

def get_pagination_urls(html, base_url):
    """
    Busca todas as páginas para navegar.
    """
    soup = BeautifulSoup(html, "lxml")
    pages = set()

    page_links = soup.select("ul.pagination li a")
    for link in page_links:
        href = link.get("href")
        if href:
            full_url = base_url.rstrip("/") + href
            pages.add(full_url)

    return list(pages)