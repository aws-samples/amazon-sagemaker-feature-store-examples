# SageMaker Feature Store Workshop


Each notebook has been built to educate feature store capabilities

In this notebook, we will illustrate how to implement feature monitoring using AWS Glue DataBrew to create feature statistics.

![Monitoring](../Images/monitoring.png?raw=true "Monitoring")

AWS Glue DataBrew is a visual data preparation tool that helps you clean and normalize data without writing code. DataBrew also allows customers to specify which data quality statistics to auto-generate for datasets when running a profile job. This allows users to customize data profile statistics such as determining duplicate values, correlations, and outliers based on the nature and size of their datasets, and create a custom data profile overview with only the statistics that meet their needs.

Key Takeaways

    1) A utility file feature_monitoring_utils.py has been provided with rich helper functions to prepare and run databrew profile jobs.

    2) We first create a DataBrew dataset from the offline feature store and then run a DataBrew profile job on that dataset.

    3) We extract statistics from the profile job execution and persist to S3

    4) We perform some additional visualizations of the feature group statistics

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

