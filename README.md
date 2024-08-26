Deploy to Google Cloud Run
Authenticate with Google Cloud:

gcloud auth login
gcloud init
Set Your Google Cloud Project:

gcloud config set project YOUR_PROJECT_ID
Enable Required APIs:

gcloud services enable run.googleapis.com
Deploy the Application to Cloud Run:

gcloud run deploy
Follow the prompts to deploy your application.

gcloud projects create my-awesome-project-123 --name="My Awesome Project"
gcloud beta billing accounts list
gcloud beta billing projects describe [PROJECT_ID]
gcloud beta billing projects link [PROJECT_ID] --billing-account=[BILLING_ACCOUNT_ID]
gcloud config set project [PROJECT_ID]
