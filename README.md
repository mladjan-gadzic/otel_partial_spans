## Prerequisites
* python 3.13.1 (`brew install python`)
* pip 25.0 (it should be installed with previous command)
* virtualenv 20.29.1 (`pip install virtualenv`)

## Setup
* create virtualenv (`virtualenv myenv` current dir is default target)
* activate virtualenv (`source myenv/bin/activate`)
* clone opentelemetry-python (https://github.com/mladjan-gadzic/opentelemetry-python/tree/partial-spans)
* add requirements.txt to opentelemetry-python
```
-e exporter/opentelemetry-exporter-otlp
-e exporter/opentelemetry-exporter-otlp-proto-common
-e exporter/opentelemetry-exporter-otlp-proto-grpc
-e exporter/opentelemetry-exporter-otlp-proto-http
-e opentelemetry-api
-e opentelemetry-proto
-e opentelemetry-sdk
-e opentelemetry-semantic-conventions
```
* build opentelemetry-python (`pip install --no-cache-dir -r requirements.txt`)
* run python program (`python partial_span_processor.py`)
