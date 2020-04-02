# A quick and simple script to copy the product images to a local directory
#
import requests
from yeslib.product_data import ProductDataReader

INPUT_PRODUCT_DATA_FILENAME = "product_data.json"

for product in ProductDataReader(INPUT_PRODUCT_DATA_FILENAME, image_dir='foo').all():
	r = requests.get(product.remote_image_url)
	with open(product.local_image_file, 'wb') as fp:
		fp.write(r.content)
