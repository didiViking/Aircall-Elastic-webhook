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
