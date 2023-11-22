## python-otel-auto-instrumentation
Python 製アプリケーションを OpenTelemetry を使って自動計装するためのプロジェクト

## Environment
- Flask の `< 3` Version
- opentelemetry-distro の `0.41b0` Version

## Usage

### Server
- 環境構築
```sh
# --- OTEL SDK 設定
export OTEL_SERVICE_NAME=ServerApp

# --- OTEL Exporter 設定
export OTEL_TRACES_EXPORTER=console,otlp
export OTEL_METRICS_EXPORTER=console,otlp
export OTEL_LOGS_EXPORTER=console,otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

### Client
- 環境構築
```sh
# --- OTEL SDK 設定
export OTEL_SERVICE_NAME=ClientApp

# --- OTEL Exporter 設定
export OTEL_TRACES_EXPORTER=console,otlp
export OTEL_METRICS_EXPORTER=console,otlp
export OTEL_LOGS_EXPORTER=console,otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

### Jaeger
```sh
docker run -d \
  -e COLLECTOR_OTLP_ENABLED=true \
  -p 4317:4317 \
  -p 4318:4318 \
  -p 14268:14268 \
  -p 16686:16686 \
  jaegertracing/all-in-one:latest
```

### 起動
```sh
$ opentelemetry-instrument python app.py
```