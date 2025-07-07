from src.extractor import extract_table_data
from bs4 import BeautifulSoup

def test_extract_table_data():
    html = """
    <html>
        <body>
            <table>
                <tbody>
                    <tr><td>Produto</td><td>Preço</td></tr>
                    <tr><td>Caneta</td><td>2,50</td></tr>
                </tbody>
            </table>
        </body>
    </html>
    """
    soup = BeautifulSoup(html, "html.parser")
    data = extract_table_data(soup)
    assert data[0]["rows"][1][0] == "Caneta"
