# SageMaker Feature Store Workshop


Each notebook has been built to educate feature store capabilities



This notebook demonstrates that Feasture store functions such as ingestion into feature store can be scaled and latency reduced by using multiple CPUs to perform the ingestion in parallel. Example shows how you can expeirment with differnt configurations for instance type and the number of processes while creating the pipeline. You can observe that as the number of instances increase, the paralellism increases and the latency decreases proportionally.
In the figure below we can see that the ingest time duration has been proportionately decreased depending on the number of instances used for ingestion.

![Ingest](../Images/ingest.png?raw=true "Ingest")

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

