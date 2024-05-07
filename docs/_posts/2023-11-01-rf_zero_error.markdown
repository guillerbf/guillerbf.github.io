---
layout: single
title:  "Random Forest with zero error and no overfitting"
date:   2023-11-01 00:00:00 +0100
categories: data_science
---

You've trained a Random Forest, and your training error is close to zero, while your validation/test error is much higher. Are you overfitting your training set?

No, you likely are not. 

![RF errors](/assets/images/rf_errors.jpeg) 

Although this may seem counterintuitive, the Random Forest is designed to have zero training error. We know that the error of a model can be decomposed into bias and variance. Bagging theory tells us that, given an ensemble of independent classifiers, the bias of the ensemble will be the same as the bias of the independent model, while the variance will be divided by the number of models in the ensemble.

That's great. We can make each individual tree have zero bias by letting it grow completely until it perfectly predicts every training sample. This tree will have a high variance, but we can ensemble hundreds of trees to reduce the total variance by the same factor. Therefore, we can achieve low bias and low variance at the same time!

Okay, but what does it mean for training error? Every training instance will be seen by approximately 66% of the trees and each tree will perfectly classify its training instances (bias=0). Since the ensemble prediction is made through voting, the majority of trees will always provide the correct class for every training instance, thus making the training error (theoretically) equal to zero.

So, no, you are likely not overfitting, and you don't necessarily need to prune your trees or make any hyperparameter tuning adjustments to counteract it. Your Random Forest is behaving as it was designed to.

