# ⚡ Termux Remote Runner

A web-based control panel for Termux that allows you to execute predefined commands on your Android device using a dynamic UI.

---

## 🚀 Features

- 🔧 Schema-driven UI (auto-generates forms from command definitions)
- ⚙️ Dynamic command execution (no hardcoding logic)
- 📱 Mobile-friendly interface
- 🧠 Safe execution layer (validated inputs + no shell injection)
- 🎯 Supports multiple Termux API commands:
  - Torch, SMS, Battery, Location
  - File operations
  - Notifications, Audio, Sensors
  - Network utilities

---

## 🧠 How It Works

1. Commands are defined in "command_schema.py"
2. Frontend fetches schema → builds UI dynamically
3. User inputs parameters
4. Backend constructs command safely
5. Executes in Termux → returns output

---

## ⚙️ Setup (Termux)

Install dependencies:
``` bash
pkg update
pkg install python termux-api
pip install flask
```
---

## ▶️ Run the App
``` bash
python app.py
```
Open in browser:
```
http://localhost:5000
```
---

## 🔐 Security Notes

- Only predefined commands are allowed
- No raw shell execution
- Input validation is enforced
- Avoid exposing this server publicly without authentication

---

## 🧩 Example Command Schema
``` json
"torch": {
    "command": ["termux-torch", "{state}"],
    "fields": {
        "state": {
            "type": "select",
            "options": ["on", "off"]
        }
    }
}
```

---

## 📌 Future Improvements

- Authentication system
- Command history/logs
- Background task queue
- UI enhancements (animations, better feedback)
- Remote access with proper security

---

## ⚠️ Disclaimer

This project can control device-level features.
Use responsibly. Misuse can lead to data loss or unintended behavior.

---

## 🧑‍💻 Author

Built as a learning project exploring:

- Flask backend systems
- Dynamic UI generation
- Mobile automation via Termux
