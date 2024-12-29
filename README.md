# **Building a Cricket Statistics Pipeline with Google Cloud Services**

## **Purpose**
**In the world of data engineering, the journey from data retrieval to insightful visualization is an adventure filled with challenges and rewards. In this guide, we’ll walk through the intricate steps of constructing a comprehensive cricket statistics pipeline using Google Cloud services. From retrieving data via the Cricbuzz API to crafting a dynamic Looker Studio dashboard, each phase contributes to the seamless flow of data for analysis and visualization.**

## **Questions this project seek to answer**
- **How much Runs scored in BGT 2024 ?**
- **How much runs are Scored by each bastman with total number of innings played and average in this BGT ?**
- **Suitable charts comparing the Batsman on basis of Runs and Average**

## **Technical Stack**
![Tech Stack](https://github.com/user-attachments/assets/00aad608-a801-414a-a3c6-4c2ba5d175e5)

## **Pipeline Architecture**
![Untitled design](https://github.com/user-attachments/assets/f2e53712-2b92-47ad-9cfe-b6de9f9e3256)

- **Data Retrieval with Python and Cricbuzz API**
The foundation of our project begins with Python’s prowess in interfacing with APIs. We’ll delve into the methods of fetching cricket statistics from the Cricbuzz API, harnessing the power of Python to gather the required data efficiently.

- **Storing Data in Google Cloud Storage (GCS)**
Once the data is obtained, our next step involves preserving it securely in the cloud. We’ll explore how to store this data in a CSV format within Google Cloud Storage (GCS), ensuring accessibility and scalability for future processing.

- **Creating a Cloud Function Trigger**
With our data safely stored, we proceed to set up a Cloud Function that acts as the catalyst for our pipeline. This function triggers upon file upload to the GCS bucket, serving as the initiator for our subsequent data processing steps.

- **Execution of the Cloud Function**
Within the Cloud Function, intricate code is crafted to precisely trigger a Dataflow job. We’ll meticulously handle triggers and pass the requisite parameters to seamlessly initiate the Dataflow job, ensuring a smooth flow of data processing.

- **Dataflow Job for BigQuery**
The core of our pipeline lies in the Dataflow job. Triggered by the Cloud Function, this job orchestrates the transfer of data from the CSV file in GCS to BigQuery. We’ll meticulously configure the job settings to ensure optimal performance and accurate data ingestion into BigQuery.

- **Looker Dashboard Creation**
Finally, we’ll explore the potential of BigQuery as a data source for Looker Studio. Configuring Looker to connect with BigQuery, we’ll create a visually compelling dashboard. This dashboard will serve as the visualization hub, enabling insightful analysis based on the data loaded from our cricket statistics pipeline.

## **Dashboard Preview**
![image](https://github.com/user-attachments/assets/5e9a7411-afea-402d-96de-8bc90c718ac0)

## **Next Steps**
- **Add CI/CD tooling to automate the workflow and make it more production ready**
- **Take advantage of systemd to run the agent when the VM starts up**
- **Add Piperider to allow for data profiling and monitoring**
- **Add docker containers to aid with reproducibility of the presented pipeline.**
