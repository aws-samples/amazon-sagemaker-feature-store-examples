# SageMaker Feature Store Workshop

Each notebook has been built to educate feature store capabilities

Hello World, Amazon SageMaker Feature Store
This notebook provides a demo of how easy it is to use SageMaker Feature Store. It does this by leveraging a simple  set of utility functions that wrap the feature store API to keep it simple for a data scientist using Python.

The main steps in this notebook are 

1) fs = FeatureStore()
Create a FeatureStore object by using the helper library 'feature_store_helper'
This helper class offers a number of convenient methods on top of the Feature Store
    API to simplify interacting with both the online store and the offline store.

2) Load example claims features as a feature group, example payment features and customer features, feature groups
We create a pandas dataframe with the claims and other features and create a feature group from the pandas dataframe using the wrapper funtion 
fs.create_fg_from_df
This method creates a new feature group using feature definitions derived from 
the column names and column data types of an existing Pandas dataframe. This is a convenience method to avoid having to know the details of FeatureDefinition syntax and data types. 

3) After the feature group is create, we need to ingest data into that freature group. This is done using the wrapper function 
fs.ingest_from_df() function
Ingests all the rows of a Pandas dataframe as new feature records into the given featur group

4) We can get the selected features or all the features of the feature group using the wrapper function 
fs.get_latest_feature_values 
etrieves a set of features of identified records from the online store.
Convenience wrapper on top of GetRecord API to allow record identifiers to be passed as either strings or integers, and to get native Python return types for feature values instead of only strings.

5) similar to the function above, we can get all the latest features from the offline feature store using the wrapper function 
fs.get_latest_offline_feature_values
Returns a dataframe with the most recent rows from a given feature group offline store.
Often, an offline store will contain multiple records for any given record identifier.
The offline store is append-only. This method will return only the most recent record
for any given identifier, based on the record event time.
For large offline stores, specify a list of record identifiers, or consider a direct Athena SQL query with custom filters instead.
       
6) To get the full history for a few ids of the feature group use the mapper function
fs.get_historical_offline_feature_values()
Returns a dataframe with all historical rows from a given feature group offline store.
For large offline stores, specify a list of record identifiers, or consider a direct Athena SQL query with custom filters instead. 

7) We can get the details of a feature group using the wrapper function 
fs.describe_feature_group()
or the tags of a feature group using 
fs.get_tags() 

8) The program then trains a simple model based on the latest features extracted from the the offline feature store. It uses the Sagemaker algorithm RandomForest Classifier to train the model using the latest features in the offline feature store. It uses the algorithms 
fit()
predict()
methods to train and make predictions respectively

 

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

