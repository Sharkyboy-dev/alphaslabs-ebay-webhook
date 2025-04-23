from flask import Flask, request

app = Flask(__name__)

# Must be 32–80 chars
VERIFICATION_TOKEN = "alphaslabs_notify_token_v1_2025_abcd1234efgh5678ijkl9012mnop3456qrst"

@app.route("/", methods=["GET"])
def index():
    return "✅ AlphaSlabs Webhook Online", 200

@app.route("/alphaslabs-notify", methods=["POST"])
def notify():
    token = request.headers.get("x-ebay-signature", "")
    if token.strip() == VERIFICATION_TOKEN:
        print("✅ Verified eBay Notification")
        return "OK", 200
    print("❌ Verification Failed: ", token)
    return "Forbidden", 403

