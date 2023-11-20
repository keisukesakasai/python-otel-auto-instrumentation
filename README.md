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
OTel の設定
```sh:set_env_var.sh
export OTEL_SERVICE_NAME=FlaskApp
export OTEL_TRACES_EXPORTER=otlp
export OTEL_METRICS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```
環境変数設定
```
source ./set_env_var.sh
```
アプリ起動
```sh
opentelemetry-instrument flask run
```

```
opentelemetry-instrument \
    --traces_exporter console,otlp \
    --metrics_exporter console \
    --service_name server \
    --exporter_otlp_endpoint http://localhost:4317 \
    --distro opentelemetry-instrument \
    --configurator "/" \
    python3 app.py
```