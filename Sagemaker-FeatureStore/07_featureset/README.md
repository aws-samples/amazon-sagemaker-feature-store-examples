# SageMaker Feature Store Workshop


Each notebook has been built to educate feature store capabilities

This notebook provides a demo of how to pull together a feature vector from across multiple feature groups at runtime for online inference. It does this by leveraging a simple set of utility functions that wrap the feature store API to keep it simple for a data scientist using Python.

![Featureset](../Images/featureset_pattern.png?raw=true "Featureset")

The main method used in this notebook is the 
get_latest_featureset_values()
It retrieves a set of features of identified records from one or more online feature groups.
        
        This convenience method lets the caller specify a "feature set" to be retrieved. A feature set is an
        ordered list of fully-qualified feature names with a feature group name as well as a feature name. 
        The feature name can be a wildcard to indicate that all features from that feature
        group should be returned. Since multiple feature groups are involved, an identifier dictionary must
        also be specified. For each unique identifier name across the feature set, a single record identifier
        value is specified for the lookup. That same identifier value will be used for each feature group with
        a matching record identifier feature name. For example, 'customer_id' may be the identifier used for 
        a 'customer' feature group and a 'customer-demographics' feature group. The 'customer_id' lookup identifier
        would be specified once in the 'id_dict' input argument.
        
        Args:
            fg_name (str): Name of the feature group from which to retrieve the records.
            id_dict (Dict[str,Union[str,int]]): Dictionary of record identifiers of records to be retrieved, key is the identifier feature
              name (can be different for each feature group), and value is the actual record identifier.
            features (List[str]): List of named features to retrieve. Features are fully-qualified as 'fg-name:feature-name',
              or 'fg-name:*' for all features.
        Returns:
            Dict[str, Union[str, int, float]]: Dictionary of named feature values with native Python types
## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

