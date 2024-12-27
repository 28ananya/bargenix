from flask import Flask, request, jsonify
import uuid
from datetime import datetime, timedelta
app = Flask(__name__)
mock_db = {
    "coupons": [],
    "requests_log": []
}

@app.route('/generate_coupon', methods=['POST'])
def generate_coupon():
    data = request.json
    product_id = data.get('product_id')
    
    if not product_id:
        return jsonify({"error": "Product ID is required"}), 400
    
    # Generate coupon details
    coupon_code = str(uuid.uuid4())[:8]  # Shortened UUID
    expiration_date = datetime.now() + timedelta(days=7)
    coupon = {
        "product_id": product_id,
        "coupon_code": coupon_code,
        "expiration_date": expiration_date.isoformat()
    }
    mock_db['coupons'].append(coupon)
    
    return jsonify({"message": "Coupon generated", "coupon": coupon}), 201


@app.route('/validate_coupon', methods=['POST'])
def validate_coupon():
    data = request.json
    product_id = data.get('product_id')
    coupon_code = data.get('coupon_code')
    
    if not product_id or not coupon_code:
        return jsonify({"error": "Product ID and Coupon Code are required"}), 400
    
    for coupon in mock_db['coupons']:
        if coupon['product_id'] == product_id and coupon['coupon_code'] == coupon_code:
            if datetime.fromisoformat(coupon['expiration_date']) > datetime.now():
                return jsonify({"message": "Coupon is valid"}), 200
            else:
                return jsonify({"error": "Coupon has expired"}), 400
    
    return jsonify({"error": "Invalid coupon"}), 400


@app.before_request
def log_request():
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "path": request.path,
        "method": request.method,
        "data": request.json
    }
    mock_db['requests_log'].append(log_entry)


@app.route('/mock_db', methods=['GET'])
def get_mock_db():
    return jsonify(mock_db)

if __name__ == '__main__':
    app.run(debug=True)
