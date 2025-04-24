# 💙 My Cute Flask Web App 🐣✨

> A simple but adorable web app made for **Cognate / Elective Course 1** at **Batangas State University** 💻💙

---

## 🎨 Theme

- **Color Scheme**: Royale Blue + Soft Pastel
- **Vibes**: Cute, Clean, and Cozy 🌈
- **Framework**: Flask (I'm also familiar with Django! 😉)

---

## 👩‍💻 Developer Info

- **Name**: Bughao, Andrei Dennise R.  
- **Course**: BS Computer Engineering – 2nd Year  
- **School**: Batangas State University – Main Campus  
- **Subject**: Cognate / Elective Course 1  
- **Design Notes**: Minimalist & mobile-friendly, with emojis to make you smile! 😊

---

## 📬 Pages Included

- 🏠 **Home Page** – Welcome greeting and navigation 💖  
- 📘 **About Page** – Project info and developer details  
- 📩 **Contact Page** – Form with fields for name, email, and message

> 🐾 All pages have matching cute styles and Royale Blue theme! 💅

---

## 🚀 How to Run the Web App

1. 💾 Clone or copy the folder to your Lubuntu VM
2. 🔧 Open Terminal inside `myapp` folder
3. 🐍 Run this command:

```bash
python3 app.py
```
or using Flask CLI:

```bash
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=5000
```

## 🌐 Visit your web app in your browser:

```bash
http://<your-ip>:5000
```
Get your IP address using:

```bash
hostname -I
```

## 🔐 Allow Port Through Firewall

```bash
sudo apt install ufw -y
sudo ufw allow 5000
```
---
## 💌 Contact Page Features
- Form validation ✅
- Fields: Name, Email, Message
- Cute submit message with 🥰 emojis
- Button to send again and return to home 🏠
---

🧁 Extras
- 🎀 Royale Blue buttons with hover effects
- 🐣 Centered layout for a warm experience
- 🧁 Rounded corners and soft shadows
- 💡 Reflection

---
## Challenges Faced:
During deployment, I encountered issues running certain commands like sudo apt install python3-pip and pip3 install flask django on my Lubuntu VM. The commands didn't work without using &&, which caused some confusion. Additionally, there was an error with the __name__ variable in my app.py, which was missing double underscores (__) causing an issue during execution. After fixing these issues, everything ran smoothly.

## What I Learned:
I learned that configuring Linux servers for hosting web apps can sometimes be tricky, especially when certain commands don't work as expected due to missing dependencies or incorrect syntax. Setting up firewalls and ensuring the correct IP address is used for accessing the web app remotely is also key.

##  Framework Experience:
Flask was the easiest for me to use, especially since I’m already familiar with Django. Flask’s minimalistic approach allowed me to focus more on the design and functionality of the app without getting overwhelmed by complex setups.

## Real-World Simulation:
Deploying this app in a VM was a great way to simulate real-world cloud hosting. It gave me insight into how a web app can be hosted on a remote server, accessed via an IP address, and managed through commands in the terminal.
---
