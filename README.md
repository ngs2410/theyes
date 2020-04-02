# Product Category Classification Challenge

## Introduction

This readme documents Neil Smith's response to the Product Category Classification Challenge from 'The Yes'.

The final predictions are contained in a file called 'product_data_predictions.json'.

The first section gives an overview of the whole solution.

The second section documents the scripts, inputs and outputs.

The third section goes into more details on each of the steps in developing the model and predictions:

1. establishing the environment,
2. understanding the data,
3. generating features,
4. labeling an inital 50 examples,
5. active learning an additional 100 examples,
6. grid search over hyperparameters,
7. final predictions.

The final section responds to the questions posed.

**Caveat**: The current solution was written quickly, doesn't include any tests and is only appropriate for small scale experimentation.

## Solution Overview

This solution uses pre-trained encoders (from Tensorflow Hub) for text and images to generate features for the product descriptions and images. 50 examples were labeled by hand. A scikit learn Gradient Boosted Classifier was used to provide predictions across the unlabeled data in a form of manual active learning. Having labeled an additional 100 of the hardest examples, using this active learning, the performance of the model appeared sufficient to inform a small hyperparameter grid search. This grid search illustrated that an Extra Trees Classifier with n_estimators=300 and max_features='sqrt' performed best given the data. Such a model was then trained across all 150 labeled examples and used to output predicted categories.

Initilly a word frequency count was used to determine whether there were any cheap signals in the descriptions. There were not.

## Contents Overview

### Inputs/Outputs

- *product_data_predictions.json* - The output products with predicted categories.
- *product_data.json* - Local copy of the original product data.
- *product_data_features.json* - Product data augmented with text and image features.
- *product_categories.txt* - Local copy of the product categories.
- *grid_search_output.txt* - Results from the small grid search.
- *label.html* - HTML output of the products for initial manual labeling.
- *predict.html* - HTML of the ranked predicted categories for active learning.
- *word_counts.txt* - Results of the initial word count experiment.

### Scripts

- *active_learning.py* - Takes labeled input and outputs ranked predictions to HTML for manual inspection.
- *add_features.py* - Encodes product descriptions and images using TF Hub models, adding them to a JSON file.
- *copy_images.py* - Makes a local copy of the product images for faster treatment.
- *generate_html.py* - Generates HTML of product images and descriptions to initiate labeling.
- *grid_search.py* - Runs multiple trials across sets of hyperparameters to determine optimal performance.
- *predict.py* - Trains an ExtraTreesClassifier using labeled examples and writes out a JSON file with categories.
- *word_count.py* - Counts word frequencies in product descriptions.
- *yeslib/labels.py* - Labelled data in a convenient Python format.
- *yeslib/product_data.py* - Common helpers for treating the product data.

## Solution Details

### 1. Establishing the environment

This solution is coded in Python version 3 using Tensorflow Hub for the pre-trained encoders, Scikit Learn for the classifiers and Beautiful Soup for HTML stripping. These command lines worked for me, but your environment might need other prerequisites installed.

`$ python3 -m venv theyes/venv`

`$ pip install --upgrade requests tensorflow tensorflow_hub beautifulsoup4 scikit-learn`

### 2. Understanding the data

We need to establish a representative evaluation but in order to determine what is a representative evaluation we have to have some feeling for the characteristics of the data. The cheapest way to do that in this situation is to (i) read the JSON, (ii) look at the images, and (iii) do some cheap word frequency analysis. These cheap initial assessments might highlight peculiarities in the data that require special treatment further down the pipeline.

Looking at the JSON file we can already see that:
- Some of the descriptions are in plain text, and others are in HTML. We'll need to strip HTML.
- Many of the descriptions are insufficient to classify the product without the image data. Some descriptions are even empty leaving a large amount of ambiguity as to which article is in focus.
- There is diversity in the descriptions. Some are descriptive prose and others are just a list of adjectives.
- On first glance every product appears to have an image and they all appear to have a ".jpg" suffix. Given that these were scraped from the Web it seems implausible that they would all be JPEGs.

The quick and dirty script "count_words.py" is used to dump out some word frequency data from the product data JSON file:

`$ python3 word_count.py > word_counts.txt`

A manual examination of this output shows that the category labels themselves hardly appear in the product descriptions and that there are approximately 2,300 distinct tokens. Using category labels as a cheap baseline is unlikely to work well. The small number of tokens might make a bag of words approach plausible.

Given the dataset is relatively small, and to facilitate examination and rapid treatment of the images the script "copy_images.py" makes a local copy of the image files.

`$ python3 copy_images.py`

A manual examination of the images shows that they are some consistencies and some outliers.
- Many images are full length portraits of women, which, absent the textual description, represent significant ambiguity with respect to the applicable category.
- Most are on a white background, but some have natural backgrounds. Many have distracting objects in the frame.
- Those that are not portraits show the specific item (e.g. jewelery, shoes) alone, but also often have distractions.
- Many of the articles are ambiguous even to a non-expert human.
- In some situations the items in focus are virtually invisible or there are striking overlaps in the description which could plausibly apply to more than one item in the picture.
- There appear to be items that are singletons, for example, I only saw one pair of gloves in the dataset. I only saw a couple of examples of LINGERIE but several of swimwear which would go into the OTHERS category.

We also take a local copy of the product_data.json

`$ wget https://raw.githubusercontent.com/chenlh0/product-classification-challenge/master/product_data.json`

### 3. Generating features

The Python script "add_features.py" takes a product data JSON file and outputs the same file including features corresponding to image and text embeddings using the specified Tensorflow Hub models.

For this experiement I used these pretrained models:

[https://tfhub.dev/google/universal-sentence-encoder/4](https://tfhub.dev/google/universal-sentence-encoder/4)
[https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/4](https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/4)

These were arbitrary choices based on what appeared to be quickest to implement. There are many other pre-trained encoders that, given time, could be tested and may generate better results.

### 4. Labeling an initial 50 examples

Given none of the data is labeled, we start by labeling a subset of the data. A key challenge is ensuring that the training set represents all of the categories with at least a minimum number of examples to allow for effective training and accurate testing. I elected to start by labeling 5 examples of each category if I could find them. There are some categories that do not have 5 examples in the data. 5 examples per category might be enough to allow for some initial discrimiation that we can then use to then augment those labelled sets. My plan was to use a form of active learning and add additional examples based on the "most incorrect" classifications of the model.

There are some caveats:
- Our evaluation set would ideally be proportionally representative of each category based on their occurence in the data. 
- Ideally, the practitioner developing the model/algorithm to solve this problem would be blind to the examples in the evaluation set.

To ease labeling, the Python script "generate_html.py" takes the product data JSON file and outputs an HTML file that can be manually inspected to find candidates for labeling each category.

Examining the HTML output where we have the image and description together, we can immediately see that some of the descriptions refer not only to the photo but also to an independent item for pairing.

### 5. Active learning an additional 100 examples,

Given a 50 initial labeled examples, the script "active_learning.py" trains a model on that data and then outputs an HTML file that ranks the unlabeled examples by the highest probability class predicted. With human examination it is easy to see where a class has been predicted with high probability but it actually incorrect. These examples can then be added as labeled examples to adjust the model's behavior. 

I found that after adding an extra 100 of these "hard" examples the model was able to get large numbers of predictions across the rest of the data correct.

### 6. Grid search over hyperparameters,

With 150 labeled examples, we have sufficient to run a simple grid search across hyperparameters. The script *grid_search.py* carries this out, running multiple trials with different random seeds for each set of hyperparameters. The output is a simple mean of the accuracy scores. The full results can be seen in grid_search_output.txt.

In practice, the ExtraTreesClassifier with 300 estimators and "sqrt" max features was found to be most effective.

This model gives us a mean accuracy of 57.39%. While this is not particularly high, it should be noted that this is using a small number of labeled examples, and the examples in the labeled set (that we are splitting for train/eval) are some of the "hardest" ones in the overall set. I would expect accuracy across a separate, labeled set to be at least 57.39% providing it matches the same distribution of data.

### 7. Final Predictions.

The 150 labeled examples along with the optimal hyperparameters found in our small grid search were then used by the "predict.py" script to output a copy of the original "product_data.json" file with the predicted categories included. This output is in the file "product_data_predictions.json"

## Responses to Questions

## Why are you designing the solution in this way?

I am designing the solution as a sequence of standalone Python scripts. This represents a "lowest common denominator"; ensuring that the scripts can be re-run and verified with the fewest dependencies. Such scripts are inexpensive to set up and iterate on when the dataset is small (as in this case).

I am most familiar with the Tensorflow platform and have seen effective results from the kinds of pre-trained models available through the Tensorflow Hub.

I have seen these pre-trained embeddings do well when fed through simple classifiers. I am using the Scikit Learn classifiers as they have standardized interfaces for many different model types and are known to be among the fastest available for certain algorithms (RandomForest, ExtraTrees). This makes iterative experimentation and grid searches rapid.

In the past I have seen these techniques build good classifiers with as few as 10 examples per category and so I started by labeling 50 examples. Active learning allows us to see which examples the model is finding hard and to add those as labeled examples.

For each example I took the text and image embedding and simply concatenated them as features for the classifier. These embeddings tend to discriminate topicality very well and should suffice in this test.

## What are the aspects that you considered when designing?

Counting words can be a low cost and effective. A simple Python script to break the descriptions into words and use high frequency words that correspond to the categories could act as an initial baseline. Based on a quick visual inspection of word frequencies this proved not to be effective.

In determining a representative evaluation set, it should be noted that we don't know whether the categories are balanced or biased in the data. I started with a balanced set of labeled examples and then the active learning highlighted classes that needed more examples.

Examining the data it is clear that both text and images will be required to disambiguate some examples. Using pre-trained image and sentence embeddings could provide a quick baseline. These kinds of embeddings tend to represent well general themes in the examples and seeing as we're only looking for broad categorizations I expect them to do well.

Given we start with no labeled data, I did consider using a DBSCAN clustering approach over cosine distances to build clusters that might, by chance, correspond to the categories required. The risk is that pre-trained embeddings contain a lot of higher-dimensional information and it's unlikely that the clusters that an automated algorithm will discover correspond to those that have been specified.

Similarly, LDA could be used over the text corpus to try to learn, in an unsupervised fashion, words that correspond to the categories we are interested in. In my experience, LDA is also liable to discover topics that don't necessarily correspond to those that you desire and would take a good amount of time to set up.

## What are the cases your solution covers, how are they covered and why are they important?

The solution covers cases where:
- The product data is well-formed JSON.
- Every product has an image.
- Images are JPEG or PNG (RGBA or Palette) - some image formats might be silently succeeding even though they are not of a format that we can embed.
- Every product has a description although that description may be empty.
- Product descriptions are in English.
- The image accompanying the product is a fair and reasonable representation of the object under consideration.
- Cross references from descriptions to pairing items appear to be tolerated to a degree.
- Given appropriate descriptions items that are partially occluded appear to be tolerated.

## What are the cases your solution does not cover and what are the ways you can extend your current solution for them?

In the interests of expediency I have only prepared a small amount of the data for train/test sets. Ideally, we would be able to make use of human raters to label a meaningful proportion of the data and then be able to split it into training, development and evaluation sets.

The current solution assumes that images that pass through the pipeline are correct by default, i.e. we rely on exceptions to catch bad images, but there might be some image formats that don't trigger exceptions but are still not treated correctly by the loaded model. A more robust approach would be a whitelist of image formats that we know work.

The dataset provided is not balanced. SHORTS, LINGERIE and JUMPSUIT are categories that are not well represented in the data and this is likely to make it difficult/impossible to learn those categories effectively. This could be mitigated by specifically searching out additional examples in those categories.

The category OTHERS is an open ended category meaning that there are likely to be many novel items that should be in the OTHERS category but which the trained model has seen no examples of. Depending upon how precise categorisation needs to be we could make a design decision to either (i) require a certain threshold be exceeded to put a particular item into a category or else it will be placed into OTHERS, or (ii) back off from items that we don't have confidence in categorizing and simply not include them in the catalogue.

The current solution is not multilingual but it would be trivial to substitute the English language text encoder with a multilingual one.

The current solution does not reject products where there is no desccription and the image is inherently ambiguous. We could treat those examples differently, spoting the lack of a description and indeterminate categorization and creating a new class of UNCLASSIFIABLE items.

The current solution doesn't include any tests and is only appropriate for small scale experimentation.