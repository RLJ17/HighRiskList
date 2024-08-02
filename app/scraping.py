import requests
from bs4 import BeautifulSoup
import json
from flask import jsonify

def search_offshore_leaks(entity_name):
    entity_search = entity_name.strip().lower().replace(' ', '+')
    url = f'https://offshoreleaks.icij.org/search?q={entity_search}'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {
            'error': 'No se pudo acceder al contenido - Espere unos minutos',
            'status_code': response.status_code,
        }
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for row in soup.select('tbody tr'):
        entity_tag = row.select_one('a.font-weight-bold.text-dark')
        jurisdiction_tag = row.select_one('td.jurisdiction')
        country_tag = row.select_one('td.country')
        datafrom_tag = row.select_one('td.source a')
        
        if entity_tag and jurisdiction_tag and country_tag:
            results.append({
                'Entity': entity_tag.text.strip(),
                'Jurisdiction': jurisdiction_tag.text.strip(),
                'LinkedTo': country_tag.text.strip(),
                'Data From': datafrom_tag.text.strip()
            })
    if not results:
        return {'error': 'No se encontraron resultados para la entidad proporcionada',
                'status_code': response.status_code,}
    
    return {
        'source': 'Offshore Leaks',
        'hits': len(results),
        'best_match': results[0],
        'results': results
    }


if __name__ == '__main__':
    entity_name = ' british trade '
    result = search_offshore_leaks(entity_name)
    print(json.dumps(result, indent=4))