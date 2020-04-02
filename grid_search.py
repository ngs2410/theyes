import functools
import itertools
import random
import sys

from yeslib.labels import KEY_TO_CATEGORY_IDX, CATEGORIES
from yeslib.product_data import ProductDataReader, TEXT_ENCODER, IMAGE_ENCODER

from sklearn.ensemble import GradientBoostingClassifier, ExtraTreesClassifier, RandomForestClassifier

INPUT_PRODUCT_DATA_FILENAME = "product_data_features.json"
RUNS_PER_TRIAL = 10


def partialclass(partial_name, cls, *args, **kwds):
	class NewCls(cls):
		__init__ = functools.partialmethod(cls.__init__, *args, **kwds)
		cls.partial_name = partial_name
	return NewCls


reader = ProductDataReader(INPUT_PRODUCT_DATA_FILENAME)
orig_Xy = []
for product in reader.all():
	if product.key in KEY_TO_CATEGORY_IDX:
		features = product.features((TEXT_ENCODER, IMAGE_ENCODER))
		category = KEY_TO_CATEGORY_IDX[product.key]
		orig_Xy.append((features, category))

num_examples = len(orig_Xy)
split = int(0.85 *  num_examples)
print(f'Using {split} training examples.')
print(f'Using {num_examples - split} evaluation examples.')

ParallelExtraTreesClassifier = partialclass('ParallelExtraTreesClassifier', ExtraTreesClassifier, n_jobs=-1)
ParallelRandomForestClassifier = partialclass('ParallelRandomForestClassifier', RandomForestClassifier, n_jobs=-1)

h_models = [ParallelExtraTreesClassifier, ParallelRandomForestClassifier] #, GradientBoostingClassifier]
h_max_features = [None, "sqrt", "log2"]
h_n_estimators = [300, 500] #25, 50, 100, 200, 300]

hparam_list = [
	h_models,
	h_max_features,
	h_n_estimators
]
trials = list(itertools.product(*hparam_list)) 

for model, max_features, n_estimators in trials:
	total = 0.
	for random_state in range(RUNS_PER_TRIAL):
		# Shuffle the original data reproducibly
		Xy = list(orig_Xy)
		random.seed(random_state)
		random.shuffle(Xy)
		X, y = zip(*Xy)
		X_train, X_test = X[:split], X[split:]
		y_train, y_test = y[:split], y[split:]

		clf = model(
			max_features=max_features,
			n_estimators=n_estimators,
			random_state=random_state).fit(X_train, y_train)
		total += clf.score(X_test, y_test)
	accuracy = total / RUNS_PER_TRIAL * 100.
	print(f"{accuracy:.2f} {model.partial_name} {n_estimators} {max_features}")
	sys.stdout.flush()