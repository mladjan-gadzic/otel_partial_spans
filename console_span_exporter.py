from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

# Set up the tracer provider
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

provider = TracerProvider()
provider.mladjan()

# Add a span processor to output spans to the console
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

# Create a span
with tracer.start_as_current_span("example-span") as span:
    # Add attributes to the span
    span.set_attribute("http.method", "GET")
    span.set_attribute("http.url", "https://example.com/api")
    span.set_attribute("user.id", 12345)

    print("Doing some work...")