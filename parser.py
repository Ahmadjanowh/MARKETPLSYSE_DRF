import os
import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from django.conf import settings
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.posts.models import Post

def parse_and_save_images():
    base_url = 'https://www.sulpak.kz/f/noutbuki?page={}'  # Базовый URL
    total_pages = 8  # Общее количество страниц для парсинга

    for page in range(1, total_pages + 1):
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        products = soup.find_all('div', class_='product__item product__item-js tile-container')

        for product in products:
            image = product.find('img')
            image_url = image['src']
            name = product.find('div', class_='product__item-name')
            title_post = name.text

            img_response = requests.get(image_url)
            if img_response.status_code == 200:
                file_name = os.path.basename(image_url)
                
                img_data = img_response.content
                img_file = ContentFile(img_data)
                post = Post.objects.create(
                    title=title_post,
                    description=title_post,
                    user_id=1  # Подставьте свой ID пользователя
                )
                post.image.save(file_name, img_file)

if __name__ == "__main__":
    parse_and_save_images()
