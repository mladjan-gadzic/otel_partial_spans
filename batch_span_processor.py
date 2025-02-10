from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Set the global trace provider
trace.set_tracer_provider(TracerProvider())

# Create the OTLP exporter to send spans
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317")

# Create a BatchSpanProcessor and add the exporter
span_processor = BatchSpanProcessor(otlp_exporter)

# Register the span processor with the tracer provider
trace.get_tracer_provider().add_span_processor(span_processor)

# Example usage: create and start a span
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("partial_span_processor") as span:
    span.set_attribute("http.method", "GET")
    span.set_attribute("http.url", "https://example.com/api")
    span.set_attribute("user.id", 12345)
    print("This is an example span.")

# Flush spans before exiting
span_processor.shutdown()