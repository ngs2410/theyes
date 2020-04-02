# A quick and dirty script that:
# 1. Loads the labeled training set.
# 2. Trains a classifier on the labeled data.
# 3. Predicts class probabilities for the entire set.
# 4. Writes predictions to a JSON product_data_predictions.json file.
#
import json

from yeslib.labels import KEY_TO_CATEGORY_IDX, CATEGORIES
from yeslib.product_data import ProductDataReader, TEXT_ENCODER, IMAGE_ENCODER

from sklearn.ensemble import GradientBoostingClassifier, ExtraTreesClassifier

INPUT_PRODUCT_DATA_FILENAME = "product_data_features.json"
OUTPUT_PRODUCT_JSON_FILENAME = "product_data_predictions.json"
SEED = 137

# 1. Load the training dataset
train_X = []
train_y = []
predict_X = []
products = list(ProductDataReader(INPUT_PRODUCT_DATA_FILENAME).all())
for product in products:
	features = product.features((TEXT_ENCODER, IMAGE_ENCODER))

	if product.key in KEY_TO_CATEGORY_IDX:
		# Keep labeled examples in the training set
		category = KEY_TO_CATEGORY_IDX[product.key]
		train_X.append(features)
		train_y.append(category)

	# All products go into the prediction set
	predict_X.append(features)

print(f'Loaded {len(train_X)} training examples.')
print(f'Loaded {len(predict_X)} total examples.')

# 2. Train the classifier
clf = ExtraTreesClassifier(n_estimators=300, max_features="sqrt",
		n_jobs=-1, random_state=SEED, verbose=True).fit(train_X, train_y)

# 3. Predict classes for all examples
probs = clf.predict_proba(predict_X)
output = []
for product, class_probs in zip(products, probs):
	class_prob_labels = sorted(zip(class_probs, CATEGORIES), reverse=True)
	category = class_prob_labels[0][1]
	output.append(product.as_property_dict(category))

# 4. Output to a JSON file
with open(OUTPUT_PRODUCT_JSON_FILENAME, 'w') as fp:
	fp.write(json.dumps(output, indent=2))
