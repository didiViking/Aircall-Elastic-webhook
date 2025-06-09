Aircall → Elasticsearch Webhook Receiver
A lightweight Python + Flask app to capture call and SMS events from Aircall webhooks and push them into your Elastic stack using Elastic APM.

Built for quick testing, local dev, or self-hosted observability workflows.
Features:

Receives real-time call and SMS webhook events from Aircall

Sends data to your Elasticsearch instance via Elastic APM

Simple Flask app, easy to extend or integrate

No cloud dependencies — works locally or anywhere Flask can run

Stack
Python 3

Flask

Elastic APM

Elasticsearch (self-hosted or remote)
Usage
Clone this repo

git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO

Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set your environment variables
Create a .env file or export these in your terminal:

env
Copy
Edit
ELASTIC_APM_SERVER_URL=http://localhost:8200
ELASTIC_APM_SERVICE_NAME=aircall-webhook
Run the app

bash
Copy
Edit
python app.py
Expose your app (e.g., with ngrok) so Aircall can reach it:

bash
Copy
Edit
ngrok http 3000
Set your Aircall webhook to point to your public URL from ngrok.

✅ Output
Data will appear in your Elasticsearch index.

Use Kibana or a custom dashboard to view and analyze call/SMS events.

Customize event_type fields or indexing logic in app.py.

📎 Related Links
Aircall Webhooks Documentation

Elastic APM

Original Blog Post

