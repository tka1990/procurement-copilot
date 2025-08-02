
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/scrape", methods=["POST"])
def scrape_product():
    data = request.get_json()
    link = data.get("link", "")

    # Simulated scraping logic (mock response)
    if "shopee" in link:
        return jsonify({
            "title": "Shopee Product – Keychron K6 Wireless Keyboard",
            "image": "https://cf.shopee.com.my/file/269dc9f57a7d2a2c7bfcf8145d9c4efc",
            "price": 289.00
        })
    elif "lazada" in link:
        return jsonify({
            "title": "Lazada Product – Ergonomic Office Chair",
            "image": "https://lzd-img-global.slatic.net/g/p/3f53c24d6e6205b05a4a882f8d06275d.jpg_720x720q80.jpg",
            "price": 199.00
        })
    elif "ikea" in link:
        return jsonify({
            "title": "IKEA Product – ADDE Chair White",
            "image": "https://www.ikea.com/my/en/images/products/adde-chair-white__0727405_pe735985_s5.jpg",
            "price": 55.00
        })
    else:
        return jsonify({ "error": "Unsupported or unknown link" }), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
