# SageMaker Feature Store Workshop


Each notebook has been built to educate feature store capabilities

![Lineage](../Images/lineage.png?raw=true "Lineage")

This notebook shows you how to use Amazon SageMaker for ML Lineage Tracking. It creates and stores information about the steps of a machine learning (ML) workflow from data preparation to model deployment. With the tracking information you can reproduce the workflow steps, track model and dataset lineage, and establish model governance and audit standards. Read more at Amazon SageMaker ML Lineage Tracking 

Key Takeaways

ML Lineage tracking ties together a SageMaker Processing job, the raw data being processed, the processing code, the query you used against the Feature Store to fetch your training and test sets, data wranger flow used for feature engineering, the training and test data in S3, and the training code into a lineage represented as a DAG.

The created ML lineage can be queried to infer the following. 1/What feature groups were used to train this model? 2/What models were trained using this feature group? 3/What feature groups were populated with data from this datasource? 4/What datasources were used to populate a feature group?

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

