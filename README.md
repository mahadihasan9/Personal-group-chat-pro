# 💬 Termux-Royal Chat Web Pro

> A modern, lightweight, real-time private web chat application built with Flask + Flask-SocketIO, optimized for mobile users and local networks (Android + Termux / Hotspot). Speedy, mobile-optimized, low-resource friendly, and private.

---

## ✨ Features

### 🚀 Core Features
- Real-time Messaging: Instant message delivery via Socket.IO
- Persistent Storage: Chats saved in local JSON → messages survive server restarts
- Room Protection: Optional password-secured rooms for privacy

### 📱 Mobile-Optimized UI
- Dark Mode & touch-friendly layout
- Swipe-to-Reply: Gesture-based reply for mobile users
- Message Replies: Reply to specific messages elegantly
- Live Reactions: Long-press or double-tap to react ❤️👍😂
- Typing Indicator: See who is typing in real-time

### 🖼 Media & Notifications
- Image Sharing: Upload & preview images in chat
- System Notifications: Alerts for users joining or leaving

---

## 🧠 Designed For
- Android users running Termux
- Local network chatting via Hotspot / Wi-Fi
- Lightweight private group chats without cloud dependency
- Learning Flask + Socket.IO through a practical project

---

## 🚀 Installation & Setup

### 📦 Prerequisites
- Python 3.9+
- Termux (optional, for Android users)

### 📚 Required Libraries
pip install Flask Flask-SocketIO eventlet
> Why eventlet? Socket.IO requires an async worker. Eventlet is lightweight, fast, and perfect for mobile/local setups.

### ▶️ Running the Server
git clone YOUR_REPOSITORY_URL
cd chating_web_pro
python app.py
- Server starts at: http://0.0.0.0:5000
- Access from any device on the same network: http://YOUR-IP:5000
- Example: http://192.168.43.1:5000

---

## ⚙️ Configuration
Edit config.py:
SECRET_KEY = "YOUR_FLASK_SECRET_KEY"   # Flask security key
SITE_PASSWORD = "YOUR_CHAT_PASSWORD"   # Chat room password

---

## ⚠️ Known Issues
- Reaction Persistence Bug: Reactions on old messages may not save after restart
- Presence Stability: Unstable mobile networks may show false disconnects
- Eventlet Deprecation Warning: Future updates may migrate to a newer async framework
> Core messaging remains fully functional. Improvements will come in future releases.

---

## 🤝 Contribution
- Report bugs ✅
- Suggest features ✅
- Submit pull requests ✅
> All contributions are welcome to make Termux-Royal Chat Web Pro better!

---

## 👤 Author
Mahdi bin Iqbal  
Python Developer | Web Enthusiast  
islammdmahadi943@gmail.com

---

💡 Tip: Perfect for private, local, mobile-first chat, especially when you don’t want to rely on cloud servers
