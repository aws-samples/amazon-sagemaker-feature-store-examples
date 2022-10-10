# SageMaker Feature Store Workshop


Each notebook has been built to educate feature store capabilities

# Using Python feature pipelines with Amazon SageMaker Feature Store
This notebook provides a demo of setting up a scheduled feature pipeline for 
transformation of raw data and ingestion into SageMaker Feature Store. Customers have
many ways to get this done, and this example takes the following approach:

- Uses a single Python function provided by the data scientist for feature transformation
- Uses Amazon Event Bridge for scheduling
- Uses Amazon SageMaker Pipelines for execution of the feature pipeline
- Uses an Amazon SageMaker Processing job to do the core feature transformation and ingestion work within the pipeline

Overview

Different ways to perform ingestion of features into feature store are available. Amazon SageMaker Processing with PySpark processor, Amazon SageMaker Processing with scikit-learn processor and Data Wrangler to transform our order data and ingest into feature store.
Amazon SageMaker Processing

Amazon SageMaker Processing gives us a simplified managed experience on SageMaker to run data processing workloads for data and feature engineering. Amazon SageMaker Processing spins up a processing container that takes a script we provide for data & feature engineering. The script can be scikit-learn or pyspark script. The container can be SageMaker built-in docker image or a custom image. SageMaker does the heavylifting of compute resources provisioning to run the job and also cleans up the resources once the job completes.
Data Wrangler

Amazon SageMaker Data Wrangler is a feature of SageMaker Studio that allows us to import, prepare, transform and analyze data. We can integrate Data Wrangler data flow into our Machine learning workflows to perform data pre processing and feature engineering with little to no code.

However in this example we just use data directly without doing any processing

The notebook assumes that the feature group already exists.

1) Create and schedule a new feature pipeline using the method
schedule_feature_pipeline()
Creates a brand new feature pipeline for an existing feature group. 
        
        Creates a SageMaker Pipeline containing a single step representing a SageMaker Processing job. 
        Uses SKLearn processor or PySpark processor depending on the script type. Creates a new IAM policy 
        to allow Amazon EventBridge to start the SageMaker Pipeline. Creates an EventBridge rule based 
        on the schedule provided. Associates the schedule rule with the Pipeline. Pipeline will be started 
        each time the schedule is triggered. Pipeline triggering can be enabled or disabled.
        
        For script_type='python', the user_defined_script must contain an apply_transforms function that
        takes in a Pandas dataframe and returns a transformed Pandas dataframe containing the exact set of
        columns needed for ingesting to the target feature group.
        
        For script_type='pyspark_sql', the user_defined_script must contain an transform_query function that
        takes in a feature group name, and returns a SQL query that uses that feature group name in its FROM
        clause to return the exact set of columns needed for ingesting to the target feature group. 
        The processing script will prepare a Spark dataframe with data from the data source, and will run
        the SQL query that is returned by transform_query. The resulting Spark dataframe will be ingested.
        
        If no user_defined_script is provided, the feature pipeline will simply ingest the features provided
        from the data source (s3 in this case). Otherwise, the transformations will be performed on the input
        data, and the resulting features will be ingested.
        
        Args:
            s3_uri_prefix (str): Raw data source, can be prefix for multiple files, currently only CSV supported.
            fg_name (str): Name of the feature group this pipeline is associated with.
            user_defined_script (str): Optional, filename for processing script.
            schedule (str): Optional, cron scheduling expression compatible with Amazon EventBridge.
            script_type (str): Optional, 'python' or 'pyspark_sql' indicating type of script to be created.
            enable (bool): Optional, whether or not to immediately enable the pipeline.
            instance_type (str): Optional, instance type for the processing job.
            instance_count (int): Optional, number of instances to use for the processing job.
            max_processes (int): Optional, max number of processes to use for feature ingestion.
            max_workers (int): Optional, max number of workers to use in each process.
            max_runtime_in_seconds (int): Optional, max seconds job is allowed to run, defaults to one hour.
        """
2) To disable the feature pipeline use the method
disable_feature_pipeline()
"""Disables a feature pipeline. 
        
        The feature pipeline must already exist. Once a feature pipeline is disabled,
        it will no longer be triggered on a schedule until it is once again enabled.
        
        Args:
            fg_name (str): Name of the feature group associated with the pipeline to disable.
        """

3) To update a feature pipeline use the method
update_feature_pipeline()
"""Disables a feature pipeline. 
        
        The feature pipeline must already exist. Once a feature pipeline is disabled,
        it will no longer be triggered on a schedule until it is once again enabled.
        
        Args:
            fg_name (str): Name of the feature group associated with the pipeline to disable.
        """
4) To remove a feature pipeline use the method
remove_feature_pipeline()
"""Removes an existing feature pipeline.
        
        Also removes the underlying EventBridge rule that was used for scheduling / triggering,
        as well as the underlying SageMaker Pipeline.
        
        Args:
            fg_name (str): Name of the feature group this pipeline is associated with.
        """
## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

