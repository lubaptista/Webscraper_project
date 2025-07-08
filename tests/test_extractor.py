from src.extractor import extract_product_data

def test_extract_product_data():
    html = '''
    <div class="thumbnail">
        <a class="title" href="/test-sites/e-commerce/allinone/product/562">Asus VivoBook X4</a>
        <h4 class="price">$295.99</h4>
        <p class="description">Asus VivoBook description text…</p>
    </div>
    '''
    data = extract_product_data(html)
    assert data[0]["title"] == "Asus VivoBook X4"
    assert data[0]["url"].endswith("/product/562")
    assert data[0]["price"] == "$295.99"
    assert data[0]["description"] == "Asus VivoBook description text…"
