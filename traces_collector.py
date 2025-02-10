import time
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configure the Tracer provider
trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({"service.name": "python-service"})
    )
)

# Create an OTLP exporter to send traces to the OpenTelemetry Collector over HTTP
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")

# Create a BatchSpanProcessor to send spans asynchronously
span_processor = BatchSpanProcessor(otlp_exporter)

# Add the span processor to the tracer provider
trace.get_tracer_provider().add_span_processor(span_processor)

# Get a tracer
tracer = trace.get_tracer(__name__)

# Create a simple trace
with tracer.start_as_current_span("foo"):
    print("This is a trace")
    time.sleep(1)

# Allow some time for the trace to be exported before the program exits
time.sleep(2)