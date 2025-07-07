from config.settings import SETTINGS

def extract_table_data(soup):
    """
    Extrai dados das tabelas do HTML.
    Retorna lista de linhas, onde cada linha é dict.
    """
    all_tables_data = []
    tables = soup.select(SETTINGS["CSS_SELECTORS"]["TABLE"])
    
    for idx, table in enumerate(tables, start=1):
        table_data = []
        rows = table.select(SETTINGS["CSS_SELECTORS"]["ROWS"])

        for row in rows:
            columns = row.select(SETTINGS["CSS_SELECTORS"]["COLUMNS"])
            values = [col.text.strip() for col in columns]
            table_data.append(values)

        all_tables_data.append({
            "table_index": idx,
            "rows": table_data
        })
    
    return all_tables_data
