from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Your existing parking_data dictionary

parking_data = {
    #Cowell, Stevenson, Crown, Merrill, Porter, Kresge, Oakes, Rachel Carson College, College Nine, and College Ten
    "Cowell": {"spots_available": 10},
    "Stevenson": {"spots_available": 10},
    "Crown": {"spots_available": 10},
    "Merrill": {"spots_available": 10},
    "Porter": {"spots_available": 10},
    "Kresge": {"spots_available": 10},
    "Oakes": {"spots_available": 10},
    "Rcarson": {"spots_available": 10},
    "Nine": {"spots_available": 10},
    "Ten": {"spots_available": 10},
    "West": {"spots_available": 10},
    "East": {"spots_available": 10}
    # Add more parking lots here
}




@app.route("/")
def index():
    return "UCSC Parking Website"

@app.route("/get_parking_data/<parking_lot>")
def get_parking_data(parking_lot):
    return jsonify(parking_data.get(parking_lot, "Parking lot not found"))

@app.route("/report", methods=['POST'])
def report_parking():
    data = request.json
    parking_lot = data.get('parking_lot')
    spots = data.get('spots')

    if parking_lot in parking_data and isinstance(spots, int):
        parking_data[parking_lot]['spots_available'] = spots
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(debug=True)
