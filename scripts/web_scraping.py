from urllib.request import urlopen
from bs4 import BeautifulSoup
import os, requests

def download_image(url, folder_path):
    try:
        img_data = requests.get(url).content
        file_name = os.path.join(folder_path, url.split("/")[-1]) + '.jpg'
        with open(file_name, 'wb') as handler:
            handler.write(img_data)
        print(f"Downloaded: {file_name}")
    except Exception as e:
        print(f"Could not download {url}: {e}")

lpg = ['https://www.freepik.com/free-photos-vectors/lpg-gas',
        'https://www.istockphoto.com/search/2/image-film?phrase=lpg%20cylinder&mediatype=photography',
        'https://www.gettyimages.in/photos/lpg-cylinder',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=2',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=3',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=4',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=5',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=6',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=7',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=8',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=9',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=10',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=11',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=12',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=13',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=14',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=15',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=16',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=17',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=18',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=19',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=20',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=21',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=22',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=23',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=24',
        'https://www.gettyimages.in/photos/lpg-cylinder?page=25',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&phrase=lpg%20cylinder&page=2',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=3&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=4&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=5&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=6&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=7&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=8&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=9&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=10&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=11&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=12&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=13&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=14&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=15&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=16&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=17&phrase=lpg%20cylinder',
        'https://www.istockphoto.com/search/2/image-film?mediatype=photography&page=18&phrase=lpg%20cylinder',]

elderly_urls = ["https://www.gettyimages.in/search/2/image-film?phrase=indian%20elderly&sort=mostpopular&page=2",
        'https://www.gettyimages.in/search/2/image-film?page=3&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=4&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=5&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=6&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=7&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=8&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=9&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=10&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=11&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=12&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=13&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=14&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=15&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=16&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=17&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=18&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=19&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=20&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=21&phrase=indian%20elderly&sort=mostpopular',
        'https://www.gettyimages.in/search/2/image-film?page=22&phrase=indian%20elderly&sort=mostpopular',
        "https://unsplash.com/s/photos/elderly",
        "https://www.gettyimages.in/search/2/image-film?phrase=indian+elderly"]

child_urls = ['https://www.istockphoto.com/search/2/image-film?msockid=3877a4bd6ef66b9b38dcb5286af66546&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?phrase=children&page=2',
              'https://www.istockphoto.com/search/2/image-film?page=3&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=4&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=5&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=6&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=7&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=8&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=9&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=10&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=11&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=12&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=13&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=14&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=15&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=16&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=17&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=18&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=19&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=20&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=21&phrase=children',
              'https://www.istockphoto.com/search/2/image-film?page=22&phrase=children',
              ]


def web_scrap(urls, folder_path):
  os.makedirs(folder_path, exist_ok=True)

  for i in urls:
    print(f'URL : {i}')
    htmldata = urlopen(i)
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')

    for item in images:
      print(item['src'])
      img_url = item['src']
      download_image(img_url, folder_path)

  files = os.listdir(folder_path)
  object_crop_files = [file for file in files if file.endswith('.jpg')]
  return 'Scraped images count : '+ str(len(object_crop_files))
