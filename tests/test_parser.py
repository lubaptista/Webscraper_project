from src.parser import parse_html

def test_parse_html():
    html = "<html><body><h1>Teste</h1></body></html>"
    soup = parse_html(html)
    assert soup.find("h1").text == "Teste"
