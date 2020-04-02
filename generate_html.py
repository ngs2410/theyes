# A quick and simple script to output an HTML file of all products
#

from yeslib.product_data import ProductDataReader

PRODUCT_DATA_FILENAME = "product_data.json"
for product in ProductDataReader(PRODUCT_DATA_FILENAME).all():
	print(f'<p><img src="{product.local_image_file}" height="200"><br>{product.key}<br>{product.description}</p><hr>')
