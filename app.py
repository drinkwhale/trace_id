from flask import Flask, request
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# 트레이서 설정
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# 콘솔에 스팬 출력 설정 (디버깅용)
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route("/")
def hello():
    # 현재 active span에서 trace_id 가져오기
    span = trace.get_current_span()
    trace_id = format(span.get_span_context().trace_id, '032x')  # 16진수 32자리 포맷

    return f"Hello, World! Your trace ID is: {trace_id}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)