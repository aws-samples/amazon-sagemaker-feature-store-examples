# SageMaker Feature Store Workshop


Each notebook has been built to educate feature store capabilities

# Using SQL feature pipelines with Amazon SageMaker Feature Store
This notebook provides a demo of setting up a SQL-based scheduled feature pipeline for 
transformation of raw data and ingestion into SageMaker Feature Store. Customers have
many ways to get this done, and this example takes the following approach:

- Uses a single SQL function provided by the data scientist for feature transformation
- Uses Amazon Event Bridge for scheduling
- Uses Amazon SageMaker Pipelines for execution of the feature pipeline
- Uses an Amazon SageMaker Processing job to do the core feature transformation and ingestion work within the pipeline

The notebook assumes that the feature group already exists.



## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

