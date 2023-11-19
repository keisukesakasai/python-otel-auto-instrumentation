from flask import Flask, request, jsonify, send_from_directory
from opentelemetry import trace

tracer = trace.get_tracer("pidata.tracer")

app = Flask(__name__)

@app.route('/attributesprocessor/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    with tracer.start_as_current_span("submit") as submit_span:
        submit_span.set_attribute("username", data["username"])
        submit_span.set_attribute("email", data["email"])
        submit_span.set_attribute("password", data["password"])
        submit_span.set_attribute("credit_card", data["credit_card"])

    return jsonify(status=1)

if __name__ == '__main__':
    app.run(host='127.0.0.1')