from flask import Flask, render_template, jsonify, request
import random
import datetime

app = Flask(__name__)

# -----------------------------
# GLOBAL VARIABLES
# -----------------------------
water_level = 53
motor_status = "OFF"
mode = "AUTO"

system_health = 95
power_status = 88
efficiency = 92

history = []

# -----------------------------
# HOME PAGE
# -----------------------------
@app.route("/")
def home():

    return render_template(
        "index.html",
        water_level=water_level,
        motor_status=motor_status,
        mode=mode,
        health=system_health,
        power=power_status,
        efficiency=efficiency
    )


# -----------------------------
# GET SYSTEM STATUS
# -----------------------------
@app.route("/status")
def status():

    global water_level

    # Water simulation

    if motor_status == "ON":

        if water_level < 100:
            water_level += 1

    else:

        if water_level > 10:
            water_level -= 1

    return jsonify({

        "water_level": water_level,
        "motor_status": motor_status,
        "mode": mode,
        "health": system_health,
        "power": power_status,
        "efficiency": efficiency

    })


# -----------------------------
# START MOTOR
# -----------------------------
@app.route("/start", methods=["POST"])
def start_motor():

    global motor_status

    motor_status = "ON"

    history.append({

        "time": str(datetime.datetime.now()),
        "action": "Motor Started"

    })

    return jsonify({

        "message": "Motor Started",
        "motor": motor_status

    })


# -----------------------------
# STOP MOTOR
# -----------------------------
@app.route("/stop", methods=["POST"])
def stop_motor():

    global motor_status

    motor_status = "OFF"

    history.append({

        "time": str(datetime.datetime.now()),
        "action": "Motor Stopped"

    })

    return jsonify({

        "message": "Motor Stopped",
        "motor": motor_status

    })


# -----------------------------
# AUTO MODE
# -----------------------------
@app.route("/auto", methods=["POST"])
def auto_mode():

    global mode

    mode = "AUTO"

    return jsonify({

        "mode": mode

    })


# -----------------------------
# MANUAL MODE
# -----------------------------
@app.route("/manual", methods=["POST"])
def manual_mode():

    global mode

    mode = "MANUAL"

    return jsonify({

        "mode": mode

    })


# -----------------------------
# HISTORY
# -----------------------------
@app.route("/history")
def get_history():

    return jsonify(history)


# -----------------------------
# ALERTS
# -----------------------------
@app.route("/alerts")
def alerts():

    alert = "System Normal"

    if water_level <= 20:
        alert = "Low Water Level"

    elif water_level >= 95:
        alert = "Tank Full"

    return jsonify({

        "alert": alert

    })


# -----------------------------
# MACHINE LEARNING PREDICTION
# -----------------------------
@app.route("/predict")
def predict():

    predicted_level = water_level + random.randint(-5, 5)

    if predicted_level > 100:
        predicted_level = 100

    if predicted_level < 0:
        predicted_level = 0

    return jsonify({

        "predicted_level": predicted_level

    })


# -----------------------------
# SETTINGS
# -----------------------------
@app.route("/settings")
def settings():

    return jsonify({

        "theme": "Dark",
        "mode": mode,
        "notifications": True

    })


# -----------------------------
# RUN APPLICATION
# -----------------------------
if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )