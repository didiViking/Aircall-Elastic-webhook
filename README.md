# Aircall → Elasticsearch Webhook Receiver

A lightweight Python + Flask app to capture **call** and **SMS** events from [Aircall](https://aircall.io/) webhooks and push them into your **Elastic stack** using **Elastic APM**.

Built for quick testing, local dev, or self-hosted observability workflows.

---

## Features

- Real-time webhook listener for Aircall call and SMS events  
- Sends data to Elasticsearch using Elastic APM  
- Simple and extendable Flask codebase  
- No cloud dependency — works locally or anywhere Flask runs

---

## Stack

- Python 3  
- Flask  
- Elastic APM  
- Elasticsearch (self-hosted or remote)

---

## Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
   cd YOUR-REPO

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt

3. **Configure environment variables**

   Create a `.env` file or export these variables directly in your shell:

   ```env
   ELASTIC_APM_SERVER_URL=http://localhost:8200
   ELASTIC_APM_SERVICE_NAME=aircall-webhook

4. **Run the app**

   ```bash
   python app.py


5. **Test the webhook**

   To test your Aircall webhook:

   Go to your [Aircall dashboard](https://dashboard.aircall.io).
   Navigate to **Integrations** → **Webhook**.
   Add your Glitch (or deployed) app URL, for example: `https://your-glitch-app.glitch.me/webhook`.
   Make a test call or send an SMS to your Aircall number.
   Check your terminal or logs — your app should print incoming webhook data.

   If everything is set correctly, data will be logged and sent to your Elastic instance.

6. **Check your data in Elastic**

   Once your app receives events from Aircall, and the data is sent to Elastic APM:

   Go to your [Kibana](https://www.elastic.co/kibana/) instance.
   Navigate to **Index Management** to make sure your index is created (e.g., `aircall-*`).
   Use **Discover** to view incoming events.
   Filter or search by `event_type` to easily find `call` or `sms` entries.
   If you’ve set a custom index name or fields, check that your mapping reflects that.

   This helps verify that your webhook is successfully posting data and Elastic is storing it properly.


   
