import time

from opentelemetry import _logs
from opentelemetry._logs.severity import SeverityNumber
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LogRecord
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs._internal.export import SimpleLogRecordProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.trace import SpanKind, TraceFlags

# Set up the OpenTelemetry Log Exporter
log_exporter = OTLPLogExporter(endpoint="http://localhost:4318/v1/logs")

# Create a SimpleLogRecordProcessor to send logs synchronously
log_processor = SimpleLogRecordProcessor(log_exporter)

# Set up the Logger Provider
logger_provider = LoggerProvider(
  resource=Resource.create({"service.name": "python-log-service"}))
logger_provider.add_log_record_processor(log_processor)

# Set the global logger provider
_logs.set_logger_provider(logger_provider)

# Create a tracer
tracer_provider = TracerProvider()
tracer = tracer_provider.get_tracer(__name__)

# Start a span manually and associate it with the log
with tracer.start_span("example-span", kind=SpanKind.INTERNAL) as span:
  # Create a logger instance using OpenTelemetry's LoggerProvider
  logger = logger_provider.get_logger("python-log-logger")

  # Create a LogRecord manually with timestamp in nanoseconds
  log_record = LogRecord(trace_id=1, trace_flags=TraceFlags(1), span_id=1,
                         severity_number=SeverityNumber(24))

  # Emit the log record
  logger.emit(log_record)

# Allow some time for the log to be exported before the program exits
time.sleep(2)
