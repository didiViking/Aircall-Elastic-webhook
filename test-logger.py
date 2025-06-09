import logging
import datetime
import json
import traceback
from elasticsearch import Elasticsearch
import elasticsearch as es_lib

print("Elasticsearch client version:", es_lib.__version__)

# Setup Elasticsearch client
es = Elasticsearch(
    "[ESS-endpoint]",
    api_key="[]]"
)

# Direct indexing test to check if ES connection works
doc = {
    "@timestamp": datetime.datetime.utcnow().isoformat(),
    "level": "INFO",
    "message": "Direct test document",
    "logger_name": "direct_test"
}

try:
    resp = es.index(index="aircall-logs", document=doc)
    print("[INFO] Direct indexing response:", resp)
except Exception as e:
    print("[ERROR] Direct indexing failed:", e)
    traceback.print_exc()

class ElasticLogHandler(logging.Handler):
    def __init__(self, es_client, index):
        super().__init__()
        self.es_client = es_client
        self.index = index

    def emit(self, record):
        log_entry = {
            "@timestamp": datetime.datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": self.format(record),
            "logger_name": record.name,
        }
        try:
            print(f"[DEBUG] Sending log to Elasticsearch: {json.dumps(log_entry)}")
            self.es_client.index(index=self.index, document=log_entry)
        except Exception as e:
            print(f"[ERROR] Failed to send log to Elasticsearch: {e}")
            traceback.print_exc()

# Setup logger
logger = logging.getLogger("test_aircall_logger")
logger.setLevel(logging.DEBUG)

elastic_handler = ElasticLogHandler(es, index="aircall-logs")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
elastic_handler.setFormatter(formatter)
logger.addHandler(elastic_handler)

# Send test log
logger.info("🔧 Test log from standalone script!")