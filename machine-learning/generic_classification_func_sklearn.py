### Generic function for making a classification model in sklearn ###

from sklearn import metrics

# Function for fitting data to a model
def classification_model(model, data, features, labels):

    # Fit the model
    model.fit(data[features], data[labels])

    # Make predictions on training set
    predictions = model.predict(data[features])

    # Print accuracy scores
    accuracy = metrics.accuracy_score(predictions, data[labels])
    print "Accuracy : %s" % "{0:.3%}".format(accuracy)
