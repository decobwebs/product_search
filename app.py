from flask import Flask, request, render_template, send_from_directory
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

#Full Code
def scrape_jiji(search_term):
    url = f'https://jiji.ng/search?q={search_term}'
    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    products = []

    for item in soup.find_all('div', class_='item'):
        name_tag = item.find('h3')
        price_tag = item.find('span', class_='price')
        link_tag = item.find('a', href=True)

        if name_tag and price_tag and link_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            link = link_tag['href']

            products.append({
                'name': name,
                'price': price,
                'url': f'https://jiji.ng{link}'
            })

    return products


def scrape_jumia(search_term):
    url = f'https://www.jumia.com.ng/catalog/?q={search_term}'
    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    products = []

    for item in soup.find_all('article', class_='prd'):
        name_tag = item.find('h3', class_='name')
        price_tag = item.find('div', class_='prc')
        link_tag = item.find('a', href=True)

        if name_tag and price_tag and link_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            link = link_tag['href']

            products.append({
                'name': name,
                'price': price,
                'url': f'https://www.jumia.com.ng{link}'
            })

    return products


def scrape_konga(search_term):
    url = f'https://www.konga.com/search?search={search_term}'
    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    products = []

    for item in soup.find_all('div', class_='product-card'):
        name_tag = item.find('h3', class_='product-title')
        price_tag = item.find('span', class_='price')
        link_tag = item.find('a', href=True)

        if name_tag and price_tag and link_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            link = link_tag['href']

            products.append({
                'name': name,
                'price': price,
                'url': f'https://www.konga.com{link}'
            })

    return products


def scrape_payporte(search_term):
    url = f'https://www.payporte.com/search?search={search_term}'
    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    products = []

    for item in soup.find_all('div', class_='product-item'):
        name_tag = item.find('h2', class_='product-title')
        price_tag = item.find('span', class_='price')
        link_tag = item.find('a', href=True)

        if name_tag and price_tag and link_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            link = link_tag['href']

            products.append({
                'name': name,
                'price': price,
                'url': f'https://www.payporte.com{link}'
            })

    return products


def scrape_printivo(search_term):
    url = f'https://printivo.com/?s={search_term}'
    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    products = []

    for item in soup.find_all('div', class_='product-item'):
        name_tag = item.find('h2', class_='product-title')
        price_tag = item.find('span', class_='price')
        link_tag = item.find('a', href=True)

        if name_tag and price_tag and link_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            link = link_tag['href']

            products.append({
                'name': name,
                'price': price,
                'url': f'https://printivo.com{link}'
            })

    return products


def scrape_kara(search_term):
    url = f'https://www.kara.com.ng/search?search={search_term}'
    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    products = []

    for item in soup.find_all('div', class_='product-item'):
        name_tag = item.find('h2', class_='product-title')
        price_tag = item.find('span', class_='price')
        link_tag = item.find('a', href=True)

        if name_tag and price_tag and link_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            link = link_tag['href']

            products.append({
                'name': name,
                'price': price,
                'url': f'https://www.kara.com.ng{link}'
            })

    return products


def scrape_ajebomarket(search_term):
    url = f'https://www.ajebomarket.com/?s={search_term}'
    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    products = []

    for item in soup.find_all('div', class_='product-item'):
        name_tag = item.find('h2', class_='product-title')
        price_tag = item.find('span', class_='price')
        link_tag = item.find('a', href=True)

        if name_tag and price_tag and link_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            link = link_tag['href']

            products.append({
                'name': name,
                'price': price,
                'url': f'https://www.ajebomarket.com{link}'
            })

    return products


def convert_price(price_str):
    cleaned_price_str = price_str.replace('₦', '').replace(' ', '').replace(',', '')
    try:
        return int(cleaned_price_str)
    except ValueError:
        return None


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_name = request.form['product_name']
        price_filter = request.form.get('price_filter')
        price_value = request.form.get('price_value')

        sites = {
            'Jiji': scrape_jiji,
            'Jumia': scrape_jumia,
            'Konga': scrape_konga,
            'PayPorte': scrape_payporte,
            'Printivo': scrape_printivo,
            'Kara': scrape_kara,
            'Ajebomarket': scrape_ajebomarket
        }

        all_products = []

        for site_name, scraper_function in sites.items():
            print(f"Scraping {site_name}...")
            try:
                products = scraper_function(product_name)
                for product in products:
                    product['site'] = site_name
                    all_products.append(product)
            except Exception as e:
                print(f"Failed to scrape {site_name}: {e}")

        for product in all_products:
            product['price_int'] = convert_price(product['price'])

        all_products = [p for p in all_products if p['price_int'] is not None]

        if price_filter and price_value:
            price_value = int(price_value)
            if price_filter == 'above':
                filtered_products = [p for p in all_products if p['price_int'] >= price_value]
            elif price_filter == 'below':
                filtered_products = [p for p in all_products if p['price_int'] <= price_value]
        else:
            filtered_products = all_products

        sorted_products = sorted(filtered_products, key=lambda x: x['price_int'])[:10]

        return render_template('results.html', products=sorted_products)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
