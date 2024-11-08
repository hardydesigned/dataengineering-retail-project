# Local

```
pip install -r requirements.txt

# Create the transformed data csv if necessary
cd data
python get_data.py

# Start Mage and Postgres with Docker
# Rename the dev.env to .env and define your credentials for postgres
# In docker-compose.yaml replace "/your-path-to-your-gcp-credentials.json" with the actual one
# Tutorial: https://www.youtube.com/watch?v=rWcLDax-VmM

cd ../data-pipeline
docker compose up -d

python ingest_data.py

# in pgAdmin (http://localhost:15433): Register Server
# Hostname: database
# Port: 5432
# Username: postgres
# Password: postgres

# Open Mage to view the Pipeline (http://localhost:6789)
# Run the whole Pipeline (You have to use BigQuery in the US to make it work)

# Now you can view the results in Google Studio and create a dashboard in Looker, like the one in the link
```

# Cloud

```
cd install
# Edit your configuration in main.tf
terraform init
terraform apply


# SSH into your VM
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3
sudo apt install python3-pip

pip install -r requirements.txt

# Create the transformed data csv if necessary

cd data
python get_data.py

# Start Mage and Postgres with Docker
# Rename the dev.env to .env and define your credentials for postgres
# In docker-compose.yaml replace "/your-path-to-your-gcp-credentials.json" with the actual one
# Tutorial: https://www.youtube.com/watch?v=rWcLDax-VmM

cd ../data-pipeline
docker compose up -d

python ingest_data.py

# in pgAdmin (http://localhost:15433): Register Server
# Hostname: database
# Port: 5432
# Username: postgres
# Password: postgres

# Open Mage to view the Pipeline (http://localhost:6789)
# Run the whole Pipeline (You have to use BigQuery in the US to make it work)

# Now you can view the results in Google Studio and create a dashboard in Looker, like the one in the link
```
