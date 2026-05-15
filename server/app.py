from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

try:
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    print("ML model loaded successfully")
except Exception as e:
    print("Error loading ML model:", e)
    model = None
    vectorizer = None


try:
    MONGO_URI = os.getenv("MONGODB_URI")

    if not MONGO_URI:
        raise ValueError("MONGODB_URI not found in .env file")

    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

    
    client.admin.command('ping')

    db = client["spam_db"]
    collection = db["messages"]

    print("MongoDB connected successfully")

except Exception as e:
    print("MongoDB connection failed:", e)
    client = None
    db = None
    collection = None

@app.route("/",methods=['GET'])
def home():
    return "EMAIL SPAM PREDICTION API IS RUNNING"



@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None or vectorizer is None:
            return jsonify({"error": "Model not loaded"}), 500

        if collection is None:
            return jsonify({"error": "Database not connected"}), 500

        data = request.json
        message = data.get("message", "")

        if not message:
            return jsonify({"error": "Message is required"}), 400

        vec = vectorizer.transform([message])
        prediction = model.predict(vec)[0]

        result = "Spam" if prediction == 1 else "Not Spam"

        
        collection.insert_one({
            "message": message,
            "result": result
        })

        return jsonify({
            "message": message,
            "prediction": result
        })

    except Exception as e:
        return jsonify({
            "error": "Prediction failed",
            "details": str(e)
        }), 500


@app.route("/history", methods=["GET"])
def history():
    try:
        if collection is None:
            return jsonify({"error": "Database not connected"}), 500

        data = list(collection.find({}, {"_id": 0}))
        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": "Failed to fetch history",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
    
     
        
