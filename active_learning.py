# A quick and dirty script that:
# 1. splits the data into a labeled training set and an unlabeled predict set.
# 2. Trains a classifier on the labeled data.
# 3. Predicts class probabilities for the unlabeled data.
# 4. Writes predictions to an HTML file for active learning.
#
from yeslib.labels import KEY_TO_CATEGORY_IDX, CATEGORIES
from yeslib.product_data import ProductDataReader, TEXT_ENCODER, IMAGE_ENCODER

from sklearn.ensemble import GradientBoostingClassifier, ExtraTreesClassifier

INPUT_PRODUCT_DATA_FILENAME = "product_data_features.json"
OUTPUT_HTML_FILE = "predict.html"
SEED = 137

# 1. Load and split the data into training and predict
train_X = []
train_y = []
predict_X = []
predict_y = []
reader = ProductDataReader(INPUT_PRODUCT_DATA_FILENAME)
for product in reader.all():
	features = product.features((TEXT_ENCODER, IMAGE_ENCODER))

	if product.key in KEY_TO_CATEGORY_IDX:
		# Keep labeled examples in the training set
		category = KEY_TO_CATEGORY_IDX[product.key]
		train_X.append(features)
		train_y.append(category)
	else:
		# Unlabeled examples are put into the predict set
		predict_X.append(features)
		predict_y.append((product.key, product.description))

print(f'Loaded {len(train_X)} training examples.')

# 2. Train the classifier
clf = ExtraTreesClassifier(n_estimators=300, max_features="sqrt",
		n_jobs=-1, random_state=SEED, verbose=True).fit(train_X, train_y)

# 3. Predict classes for all unlabeled examples and sort from strongest
# predictions to weakest to highlight the "most wrong" examples.
probs = clf.predict_proba(predict_X)
batch = []
for (key, description), class_probs in zip(predict_y, probs):
	batch.append((max(class_probs), key, description, tuple(class_probs)))
batch = sorted(batch, reverse=True)

# 4. Output to an HTML file so we can visually inspect predictions
# and add to the labeled data.
with open(OUTPUT_HTML_FILE, 'w') as fp:
	for idx, (_, key, description, class_probs) in enumerate(batch):
		class_prob_labels = sorted(zip(class_probs, CATEGORIES), reverse=True)
		fp.write(f'<p>{idx}<br><img src="images/{key}" height="200"><br>{key}<br>{description}<br>{class_prob_labels}</p><hr>')


