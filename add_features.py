# A quick and simple script to:
# 1. Load pretrained encoders for text and images.
# 2. Augment the product data with text and image features.
# 3. Write out the augmented products to a new file.
#
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

from yeslib.product_data import ProductDataReader, write_product_data
from yeslib.product_data import Product, TEXT_ENCODER, IMAGE_ENCODER


INPUT_PRODUCT_DATA_FILENAME = "product_data.json"
OUTPUT_PRODUCT_DATA_FILENAME = "product_data_features.json"

# 1. Load the pre-trained text encoder
text_embed = hub.load(TEXT_ENCODER)

# Load the pre-trained image encoder
image_embed = tf.keras.Sequential([
	hub.KerasLayer(IMAGE_ENCODER, trainable=False),  # Can be True, see below.
])
image_embed.build((None,)+Product.IMAGE_SHAPE+(3,))

# 2. Augment the product data with the encoded features
products = list(ProductDataReader(INPUT_PRODUCT_DATA_FILENAME).all())
for product in products:
	product[TEXT_ENCODER] = text_embed([product.description])[0].numpy().tolist()
	product[IMAGE_ENCODER] = image_embed(product.image()[np.newaxis, ...])[0].numpy().tolist()

# 3. Write the augmented products to a file
write_product_data(OUTPUT_PRODUCT_DATA_FILENAME, products)