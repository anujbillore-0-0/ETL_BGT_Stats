import requests
import csv
from google.cloud import storage

#Extract Data from Cricbuzz API

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/series/7745"
querystring = {"statsType": "mostRuns"}

headers = {
    "x-rapidapi-key": "e6b3e0185bmsh03561ca61154cf7p18c183jsn9ac988312f9f",
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json().get("testStatsList", {}).get("values", [])
    csv_filename = "batsmen_rankings.csv"

    if data:
        # Headers for the CSV file
 

        # Open the CSV file for writing
        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            

            # Write each row of data
            for item in data:
                values = item.get("values", [])
                writer.writerow(values)  # Write values directly as a row

        print(f"Data fetched successfully and written to '{csv_filename}'")

         # Upload the CSV file to GCS
        bucket_name = 'bkt-ranking-dataaaaa'
        storage_client = storage.Client(project="luminous-wharf-445218-t0")
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f'{csv_filename}'  # The path to store in GCS

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)

        print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")
    else:
        print("No data available from the API.")
else:
    print("Failed to fetch data:", response.status_code)
