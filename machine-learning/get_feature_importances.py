### GET FEATURE IMPORTANCES ###

# This is to be applied on a FITTED algorithm/model
feat_imp = pf.Series(model.feature_importances_, index=features).sort_values(ascending=False)
# Note: 'features' is the list of input features/variables

print feat_imp
