from flask import Flask, request, jsonify
from elasticapm.contrib.flask import ElasticAPM
import logging
import json
from datetime import datetime
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Elastic APM configuration
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'aircall-webhook-receiver',
    'SERVER_URL': '[ELASTICAPMendpoint]',
    'API_KEY': '[]'  # Your APM Server API key here
}

# Initialize APM
apm = ElasticAPM(app)

# Elasticsearch configuration
ES_HOST = "[ESS-endpoint]"
ES_API_KEY = "[]" # Your Elasticsearch API key here

# Initialize Elasticsearch client with API key auth
es = Elasticsearch(
    ES_HOST,
    api_key=ES_API_KEY,
)

# Setup logger
logger = logging.getLogger('aircall')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

@app.route('/')
def index():
    logger.info("Health check passed")
    return "Aircall Webhook Receiver with APM is running!"

@app.route('/aircall/call', methods=['POST'])
def handle_call():
    data = request.get_json(force=True)
    logger.info(f"Received CALL event: {json.dumps(data)}")
    index_document(data, "call")
    return jsonify({'status': 'received'}), 200

@app.route('/aircall/sms', methods=['POST'])
def handle_sms():
    data = request.get_json(force=True)
    logger.info(f"Received SMS event: {json.dumps(data)}")
    index_document(data, "sms")
    return jsonify({'status': 'received'}), 200

@app.route('/crash')
def crash():
    1 / 0  # This will crash and be auto-captured by Elastic APM
    return "This won't be returned"

@app.route("/aircall-webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)

    event_type = detect_event_type(data)

    logger.info(
        "Received Aircall webhook",
        extra={
            "event_type": event_type,
            "source": "aircall",
            "webhook_data": data,
        },
    )

    index_document(data, event_type)

    payload_str = json.dumps(data)
    if "[phone-number]" in payload_str or "[email-address]" in payload_str:
        logger.info("✅ Event is from your test number or user.")
    else:
        logger.info("ℹ️ Event received, but not from your test number or user.")

    return jsonify({"status": "received"}), 200

def detect_event_type(data):
    if "call" in data:
        return "call"
    elif "sms" in data:
        return "sms"
    elif "resource" in data:
        if "call" in data["resource"]:
            return "call"
        elif "sms" in data["resource"]:
            return "sms"
    return "unknown"

def index_document(data, event_type):
    # Prepare a new dict to avoid mutating the original data
    doc = dict(data)  # shallow copy

    # Add @timestamp field if missing
    if "@timestamp" not in doc:
        doc["@timestamp"] = datetime.utcnow().isoformat() + "Z"

    # Add/overwrite event_type
    doc["event_type"] = event_type

    try:
        response = es.index(index="aircall-logs", document=doc)
        logger.info(f"Indexed document to Elasticsearch: {response['result']}")
    except Exception as e:
        logger.error(f"Failed to index document: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
