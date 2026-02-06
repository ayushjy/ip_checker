from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"status": "IP Checker Running"})


@app.route("/check-ip")
def check_ip():

    ip = request.args.get("ip")

    if not ip:
        return jsonify({"error": "IP required"}), 400

    try:
        url = f"http://ipwho.is/{ip}"
        data = requests.get(url, timeout=5).json()

        if not data.get("success"):
            return jsonify({"error": "Invalid IP"}), 400

        result = {
            "ip": data.get("ip"),
            "success": data.get("success"),
            "type": data.get("type"),
            "continent": data.get("continent"),
            "continent_code": data.get("continent_code"),
            "country": data.get("country"),
            "country_code": data.get("country_code"),
            "region": data.get("region"),
            "region_code": data.get("region_code"),
            "city": data.get("city"),
            "org": data.get("connection", {}).get("org"),
            "timezone": data.get("timezone", {}).get("id"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "is_eu": data.get("is_eu"),
            "postal": data.get("postal"),
            "calling_code": data.get("calling_code"),
            "capital": data.get("capital"),
            "borders": data.get("borders")
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
