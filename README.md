## python-otel-auto-instrumentation
Python アプリを Otel で自動計装するためのプロジェクトです。

## 手順
- Jaeger 起動
```sh
docker run -d \
  -e COLLECTOR_OTLP_ENABLED=true \
  -p 4317:4317 \
  -p 4318:4318 \
  -p 14268:14268 \
  -p 16686:16686 \
  jaegertracing/all-in-one:latest
```

- app 実行
```sh
opentelemetry-instrument \
    --traces_exporter console,otlp \
    --metrics_exporter otlp \
    --service_name SampleApp \
    --exporter_otlp_protocol grpc \
    --exporter_otlp_endpoint localhost:4317 \
    python app.py
```