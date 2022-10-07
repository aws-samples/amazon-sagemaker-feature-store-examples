# SageMaker Feature Store Workshop

Each notebook has been built to educate feature store capabilities

Demonstrate time travel with Amazon SageMaker Feature Store

This notebook provides a demo of performing both as-of time travel and row-level time travel using SageMaker Feature Store. It does this by using a simple set of utility functions that wrap the feature store API to keep it simple for a data scientist using Python.

![Time Travel](../Images/row_level_time_travel.png?raw=true)

The main steps in this notebook are 

1) fs = FeatureStore()
Create a FeatureStore object by using the helper library 'feature_store_helper'
This helper class offers a number of convenient methods on top of the Feature Store
    API to simplify interacting with both the online store and the offline store.
2) We can get all the latest features from the offline feature store for any poiint in time using the wrapper function 
fs.get_latest_offline_feature_values
The function takes as an argument the feature group name and also the time for which the feature values need to be returned and returns a dataframe with the most recent rows at any point in time from a given feature group offline store.
Often, an offline store will contain multiple records for any given record identifier.
The offline store is append-only. This method will return only the most recent record
for any given identifier, based on the record event time.
For large offline stores, specify a list of record identifiers, or consider a direct Athena SQL query with custom filters instead.
       
3) To perform row-level time travel and get features at specified time events use the method 
get_features() 
Performs row-level time travel, returning a point-in-time accurate dataset.
        
This convenience method lets the caller specify a "feature set" to be retrieved, with feature values that are free from feature leakage. The events_df specifies a set of event timestamps and corresponding record identifiers to drive the row-level time travel. The features parameter identifies the feature set to retrieve. It is an ordered list of fully-qualified feature names with a feature group name as well as a feature name. The feature name can be a wildcard to indicate that all features from that feature
group should be returned. Since multiple feature groups may be involved, the events dataframe must have a column for each unique identifier name across the feature set. That same identifier value will be used for each feature group with a matching record identifier feature name. For example, 'customer_id' may be the identifier used for a 'customer' feature group and a 'customer-demographics' feature group. 
The 'customer_id' lookup identifier would be a column in the events_df dataframe.
Depending on the requested timestamp and the event times of the feature avalues found, the row-level time travel will return null values for feature values that would not yet have been available. For feature values that are available, the time travel will return the most recent value, without allowing any values that are newer than the requested timestamp.
        

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

