# 🧠 GrowEI – Personal Emotional Intelligence Tracker

A minimal, elegant, and research-backed desktop app to help you build emotional awareness, resilience, and reflection.

Built with ❤️ using Python and inspired by the emotional intelligence model proposed in the MDPI journal:  
**"Emotional Intelligence: A Theoretical Framework and Review"** [🔗 Link](https://www.mdpi.com/2673-8392/4/1/37)

---

## 🎯 Purpose

**GrowEI** is a personal journaling tool to help you:
- Track your emotions and situations across the day
- Log your coping strategies (and revisit them later!)
- Analyze your emotional trends visually (daily, weekly, monthly)
- Learn and practice new coping methods from a curated list
- Build long-term emotional awareness and regulation

---

## 🖥️ Features

✅ **Multi-tab GUI**  
- **Add Emotion**: Log current emotions, situations, and how you’re coping  
- **History**: Review past entries and optionally play back reflections  
- **Coping Strategies**: Find healthy methods to deal with emotions  
- **Reports**: Auto-generated visual pie-charts of emotion patterns  
- **Clear Buttons**: Wipe old data or just reset inputs

✅ **Safe & Local**  
- All entries saved as JSON in your local folder  
- No internet or AI needed. Works offline 💻

✅ **Cross-platform**  
- Works on **Windows (.exe)**, **Linux (.AppImage)**, and **macOS (.dmg)**  
- Installers provided for all major OSes

---

## 🛠️ Installation



### 💡 Prerequisites

- Python 3.10 or above  
- `pip install -r requirements.txt` (Install dependencies)

### Create the installer for your system.

🪟 Windows (create .exe)
```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed main.py

```

🍎 macOS (create .app or .dmg)
1. On MacOS System

```bash
pip install pyinstaller
pyinstaller --noconfirm --windowed --onefile main.py --icon=icon.icns
```
2. To make a .dmg install
```bash
brew install create-dmg
create-dmg 'dist/main.app'
```

🐧 Linux (create .AppImage)
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

### 📦 OR Download Executable (Recommended)

Download the installer for your OS:

| Platform | Installer Link |
|---------|----------------|
| 🪟 Windows | `GrowEI.exe` |
| 🍎 macOS | `GrowEI.dmg` |
| 🐧 Linux | `GrowEI.AppImage` |

> No Python needed with these – just install and launch!

---

## 📷 Screenshots


- Main Logging Page
> ! [Screenshot](Screenshot from 2025-07-07 15-09-12.png)
> ! [Screenshot](Screenshot from 2025-07-07 15-09-28.png)
> ! [Screenshot](Screenshot from 2025-07-07 15-09-50.png)

---

## 🧠 Based on Research

This app’s emotion modeling, coping prompts, and journal schema is based on this scientific article:  
**“Emotional Intelligence: A Theoretical Framework and Review” – MDPI (2024)**  
Link: https://www.mdpi.com/2673-8392/4/1/37

---

## 🚀 Motivation

> “You can’t control your emotions if you can’t understand them.”  
We built this to help individuals:
- Reflect mindfully on their emotional states
- Avoid unhealthy emotional patterns
- Grow in self-awareness and mental clarity

Whether you're dealing with stress, or just curious about your inner patterns – this is your mirror.

---

## 👨‍💻 Built With

- Python 🐍  
- Tkinter (GUI)  
- Matplotlib (Reports)  
- JSON (storage)  
- Pure offline logic (no AI needed)

---

## 🪄 Future Features

- Weekly & monthly PDF reports  
- Guided journaling prompts  
- Custom emotion labels  
- Passcode lock  
- AI integration (optional, future)

---

## ⭐ Support & Contribute

If you like this project:
- ⭐ Star it on GitHub
- 🪄 Suggest features via issues
- 📬 Share with someone who needs it!

---

## 🙌 Made during Mission Prime – 31 Tools in 31 Days
I’m building 31 tools in 31 days to get better, ship more, and help real people with small utilities.  
Follow my journey on LinkedIn → [🔗 [https://www.linkedin.com/in/shreekantsinsinwar/]]



---
