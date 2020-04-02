import os
import json
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import PIL.Image as Image
import numpy as np


TEXT_ENCODER = "https://tfhub.dev/google/universal-sentence-encoder/4"
IMAGE_ENCODER = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/4"

class Product(object):
	IMAGE_URL = 'image_url'
	DESCRIPTION = 'description'
	CATEGORY = 'category'
	FEATURES = 'features'
	IMAGE_SHAPE = (224, 224)

	def __init__(self, properties, image_dir):
		self._properties = properties
		self._image_dir = image_dir
		if 'features' not in self._properties:
			self._properties[Product.FEATURES] = {}

	@property
	def properties(self):
		return self._properties

	@property
	def remote_image_url(self):
		return self._properties[Product.IMAGE_URL]

	@property
	def key(self):
		return os.path.basename(urlparse(self.remote_image_url).path)

	@property
	def description(self):
		raw_desc = self._properties.get(Product.DESCRIPTION, '')
		return raw_desc or BeautifulSoup(raw_desc).get_text()

	def features(self, args):
		features_list = [self._properties['features'][arg] for arg in args]
		return [item for sublist in features_list for item in sublist]

	def __setitem__(self, key, value):
		self._properties[Product.FEATURES][key] = value

	@property
	def local_image_file(self):
		return os.path.join(self._image_dir, self.key)

	def image(self):
		raw_image = Image.open(self.local_image_file)
		if raw_image.format == 'PNG'and raw_image.mode == 'P':
			processed_image = raw_image.convert("RGBA")
		else:
			processed_image = raw_image

		image = processed_image.resize(Product.IMAGE_SHAPE)
		image = np.array(image, dtype=np.float32)/255.0

		if raw_image.format == 'PNG':
			image = image[..., :3]

		return image

	def as_property_dict(self, category):
		return {
			Product.IMAGE_URL: self._properties[Product.IMAGE_URL],
			Product.DESCRIPTION: self._properties[Product.DESCRIPTION],
			Product.CATEGORY: category,
		}


class ProductDataReader(object):

	def __init__(self, filename, image_dir='images'):
		self._filename = filename
		self._image_dir = image_dir

	def _raw_product_dicts(self):
		return json.loads(open(self._filename, 'r').read())

	def all(self):
		for product_dict in self._raw_product_dicts():
			yield Product(product_dict, self._image_dir)


def write_product_data(filename, products):
	objects = [product.properties for product in products]
	with open(filename, 'w') as fp:
		fp.write(json.dumps(objects, indent=2))