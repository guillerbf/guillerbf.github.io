---
layout: single
title:  "Data splits in the world of small data"
date:   2023-11-01 00:00:00 +0100
categories: data_science
---

Is the division into training, validation, and test data non-negotiable?

The other day, I was asked this question in class at Zrive. And although it may seem trivial, it isn't. To answer it, we must first understand why we initially divide our data. We train models on historical data to apply them to future data, and therefore, we want to evaluate the prediction quality of our model in an unbiased way when generalizing to new data. That's why we divide the data in the first instance.

The training data is used to train the model. The validation data is used to evaluate the error of different models (or with different hyperparameters) on data that the model hasn't seen during training. Finally, the test data allows us to have a final, unbiased estimate of the error we can expect from our best model on data that has been kept separate from the entire training and model selection process.

But what do we do when we work with problems that have very little data? Dividing a small dataset inevitably leads to three even smaller data groups, with the potential for increased variance when training and validating on small sets that may not be representative of the real distribution we are trying to model. In this cases, there is no right answer as we will likely need to cut some corners.

One option is to sacrifice the test data and use cross-validation with 100% of the dataset. With cross-validation, we obtain a measure of the error and its dispersion across folds for both training and validation. If both errors are of similar magnitude and do not have significant dispersion, we can have some confidence that they represent a good estimate of the error we could expect on the test data, while still using as much of the data as we can to train our models.

When we move into the world of small data, problems become truly interesting with no clear right/wrong solutions.