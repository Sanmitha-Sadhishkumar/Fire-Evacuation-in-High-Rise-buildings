import os
import requests
from urllib.parse import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup

def download_image(img_url, folder_path, base_url):
    try:
        # Ensure the URL is properly formed
        if not img_url.startswith(('http://', 'https://')):
            img_url = urljoin(base_url, img_url)

        # Download the image
        img_data = requests.get(img_url).content
        file_name = os.path.join(folder_path, img_url.split("/")[-1].split("?")[0])

        # Save the image
        with open(file_name, 'wb') as handler:
            handler.write(img_data)
        print(f"Downloaded: {file_name}")

    except Exception as e:
        print(f"Could not download {img_url}: {e}")

# List of URLs to scrape
pictogram_urls = [
    'https://stock.adobe.com/in/search/images?k=chemical%20labelling',
    'https://www.complianceandrisks.com/topics/globally-harmonized-system/',
    'https://www.shutterstock.com/search/chemical-label',
    'https://www.istockphoto.com/search/2/image-film?phrase=chemical+label',
    'https://depositphotos.com/photos/chemical-label.html',
    'https://www.bradyindia.co.in/applications/ghs-labeling-requirements',
    'https://www.safetyhub.com/safety-training/introduction-to-ghs/',
    'https://stock.adobe.com/search/images?k=chemical+label',
    'https://teamdls.com/Label-Markets/Industrial-Labels/GHS-Chemical-Labels.htm',
    'https://www.kaggle.com/datasets/sagieppel/labpics-chemistry-labpics-medical/data',
    'https://www.coleparmer.in/p/ghs-flame-pictogram-labels/64906',
    'https://www.coleparmer.in/p/ghs-flame-over-circle-pictogram-labels/64907',
    'https://www.jjstech.com/ghs1054.html',
    'https://ehsdailyadvisor.blr.com/2018/04/ghs-pictogram-training-cheat-sheet/',
    'https://lawfilesext.leg.wa.gov/Law/WAC/WAC%20296%20%20TITLE/WAC%20296%20-901%20%20CHAPTER/WAC%20296%20-901%20-14026.htm',
    'https://www.shutterstock.com/search/flammalbe-image',
    'https://www.shutterstock.com/search/labelled-chemicals',
    'https://www.shutterstock.com/search/chermicals-in-bottles',
    'https://www.shutterstock.com/search/flame-over-circle',
    'https://www.shutterstock.com/search/flame-over-circle-symbol',
    'https://www.shutterstock.com/search/flame-over-circle-chemicals-symbol',
    'https://www.shutterstock.com/search/hazardous-substances-label',
    'https://www.shutterstock.com/search/labelled-hazardous',
    'https://www.chemicalindustryjournal.co.uk/back-to-the-basics-of-chemical-labelling',
    'https://in.vwr.com/store/product/3216634/vwr-labels-hazardous-substance-ghs-labels',
    'https://ohsonline.com/articles/2023/01/18/properly-store-and-label-hazardous-substances.aspx',
    'https://www.shutterstock.com/search/chemical-substance',
    'https://www.istockphoto.com/illustrations/chemical-label',
    'https://www.istockphoto.com/search/2/image-film?mediatype=illustration&phrase=hazardous%20chemicals',
    'https://www.istockphoto.com/search/2/image-film?mediatype=illustration&phrase=hazardous%20chemicals%20label&servicecontext=srp-related'
    'https://www.istockphoto.com/search/2/image-film?mediatype=illustration&phrase=hazardous%20chemicals%20',
    'https://www.istockphoto.com/search/2/image-film?mediatype=illustration&phrase=hazardous%20chemicals%20construction&servicecontext=srp-related',
    'https://www.istockphoto.com/search/2/image-film?mediatype=illustration&phrase=hazardous%20chemicals%20storage&servicecontext=srp-related',
    'https://www.hague-group.com/chemical-hazard-labelling-our-comprehensive-guide/',
    'https://www.herma.com/label/products/labels-for-hazardous-substances-and-dangerous-goods/hazardous-substance-labels/',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=hazardous%20substance%20label&sort=mostpopular',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=chemical%20labels&sort=mostpopular',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=hazardous%20chemical%20labels&sort=mostpopular',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=hazardous%20chemical%20labels&suppressfamilycorrection=true&sort=mostpopular&page=2',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=hazardous%20chemical%20labels&suppressfamilycorrection=true&sort=mostpopular&page=3',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=hazardous%20chemical%20labels&suppressfamilycorrection=true&sort=mostpopular&page=4',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=hazardous%20chemical%20labels&suppressfamilycorrection=true&sort=mostpopular&page=5',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=hazardous%20chemical%20labels&suppressfamilycorrection=true&sort=mostpopular&page=6',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=hazardous%20chemical%20labels&suppressfamilycorrection=true&sort=mostpopular&page=7',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=hazardous%20chemical%20labels&suppressfamilycorrection=true&sort=mostpopular&page=8',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=hazardous%20chemical%20labels&suppressfamilycorrection=true&sort=mostpopular&page=9',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=hazardous%20labels&sort=mostpopular',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=chemical%20labels&sort=mostpopular',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=2',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=3',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=4',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=5',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=6',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=7',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=8',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=2',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=3',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=4',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=5',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=6',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=7',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=8',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=9',
    'https://www.gettyimages.in/search/2/image-film?family=creative&phrase=flammable%20labels&sort=mostpopular&page=10'
]


folder_path = "symbol_dataset"
os.makedirs(folder_path, exist_ok=True)

for base_url in pictogram_urls:
    try:
        print(f'URL : {base_url}')
        htmldata = urlopen(base_url)
        soup = BeautifulSoup(htmldata, 'html.parser')

        # Find all image tags
        images = soup.find_all('img')

        # Loop through each image and try to download it
        for item in images:
            img_url = item.get('src')
            if img_url:
                download_image(img_url, folder_path, base_url)

    except Exception as e:
        print(f"Could not download {base_url}: {e}")


