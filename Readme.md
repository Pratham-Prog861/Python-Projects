<div align="center">

# 🐍 Python Projects Collection

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Projects](https://img.shields.io/badge/Projects-9-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

_A curated collection of Python projects showcasing automation, AI, multimedia processing, and practical utilities_

[Getting Started](#-getting-started) • [Projects](#-projects) • [Tech Stack](#-tech-stack) • [Contributing](#-contributing)

---

</div>

## 📋 Table of Contents

- [🎮 Tic-Tac-Toe Game](#-tic-tac-toe-game)
- [🎥 Screen Recorder](#-screen-recorder)
- [✍️ Spell Checker](#️-spell-checker)
- [💰 Rent Calculator](#-rent-calculator)
- [🖼️ Slideshow](#️-slideshow)
- [📱 QR Code Generator](#-qr-code-generator)
- [🎬 ASCII Video Player](#-ascii-video-player)
- [🤖 AI Task Agent](#-ai-task-agent)
- [🗄️ Python MongoDB Integration](#️-python-mongodb-integration)

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/Pratham-Prog861/Python-Projects.git

# Navigate to a specific project
cd <project-folder>

# Install dependencies (if requirements.txt exists)
pip install -r requirements.txt

# Run the project
python <main-file>.py
```

---

## 🎯 Projects

### 🎮 Tic-Tac-Toe Game

> Classic two-player game with a clean GUI interface

```bash
📂 tic-tac-toe/
└── tictactoe.py
```

**Features:**

- Interactive GUI using Tkinter
- Two-player gameplay
- Win detection algorithm
- Clean and intuitive interface

**Run:**

```bash
cd tic-tac-toe
python tictactoe.py
```

---

### 🎥 Screen Recorder

> Capture your screen activity and save as video

```bash
📂 screen recorder/
└── sr.py
```

**Features:**

- Real-time screen capture
- Video file output
- Keyboard interrupt handling

**Run:**

```bash
cd "screen recorder"
python sr.py
# Press Ctrl+C to stop recording
```

**Tech:** `pyautogui`, `cv2`, `numpy`

---

### ✍️ Spell Checker

> Intelligent spell checking utility for text validation

```bash
📂 spell checker/
└── spellchecker.py
```

**Features:**

- Real-time spell checking
- Suggestion engine
- Custom dictionary support

**Run:**

```bash
cd "spell checker"
python spellchecker.py
```

**Tech:** `spellchecker`

---

### 💰 Rent Calculator

> Split rent fairly among roommates

```bash
📂 rent calculator/
└── rentCalculator.py
```

**Features:**

- Multi-person rent splitting
- Custom calculation logic
- User-friendly interface

**Run:**

```bash
cd "rent calculator"
python rentCalculator.py
```

---

### 🖼️ Slideshow

> Automated image slideshow viewer

```bash
📂 slideshow/
└── slideshow.py
```

**Features:**

- Automatic image transitions
- Customizable timing
- Support for multiple formats

**Run:**

```bash
cd slideshow
python slideshow.py
```

**Tech:** `PIL/Pillow`, `tkinter`

---

### 📱 QR Code Generator

> Generate QR codes for UPI payments and more

```bash
📂 qrcode/
└── qrcode.py
```

**Features:**

- UPI payment QR generation
- Customizable QR codes
- High-quality output

**Run:**

```bash
cd qrcode
python qrcode.py
```

**Tech:** `qrcode`, `PIL`

---

### 🎬 ASCII Video Player

> Convert videos to ASCII art in real-time

```bash
📂 ascii-video/
├── main.py
├── pyproject.toml
├── uv.lock
└── vid.mp4
```

**Features:**

- Video to ASCII conversion
- Real-time playback
- Modern Python packaging with `uv`

**Run:**

```bash
cd ascii-video
python main.py
```

**Tech:** `opencv-python`, `numpy`

---

### 🤖 AI Task Agent

> Intelligent task management agent powered by AI

```bash
📂 ai-agent/
├── task_agent.py
├── tasks.txt
├── .env
└── .gitignore
```

**Features:**

- AI-powered task processing
- Environment configuration
- Task persistence

**Run:**

```bash
cd ai-agent
python task_agent.py
```

**Tech:** AI/ML libraries, environment management

---

### 🗄️ Python MongoDB Integration

> Database operations with MongoDB

```bash
📂 python_mongodb/
├── main.py
├── requirements.txt
├── .env
└── .env.example
```

**Features:**

- MongoDB CRUD operations
- Environment-based configuration
- Secure credential management

**Setup:**

```bash
cd python_mongodb
cp .env.example .env
# Edit .env with your MongoDB credentials
pip install -r requirements.txt
python main.py
```

**Tech:** `pymongo`, `python-dotenv`

---

## 🛠️ Tech Stack

<div align="center">

| Category             | Technologies                                                                                    |
| -------------------- | ----------------------------------------------------------------------------------------------- |
| **Core**             | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)    |
| **GUI**              | ![Tkinter](https://img.shields.io/badge/Tkinter-3776AB?style=flat)                              |
| **Computer Vision**  | ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)    |
| **Database**         | ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white) |
| **Automation**       | ![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-3776AB?style=flat)                          |
| **Image Processing** | ![Pillow](https://img.shields.io/badge/Pillow-3776AB?style=flat)                                |

</div>

### Key Libraries

- `tkinter` - GUI development
- `opencv-python (cv2)` - Computer vision and video processing
- `pyautogui` - GUI automation
- `spellchecker` - Spell checking functionality
- `Pillow (PIL)` - Image manipulation
- `qrcode` - QR code generation
- `pymongo` - MongoDB database driver
- `python-dotenv` - Environment variable management

---

## 💡 Use Cases

These projects are perfect for:

- 🎓 **Learning Python** - Hands-on examples of Python concepts
- 🔧 **Automation** - Automate repetitive tasks
- 🎨 **Multimedia Processing** - Work with images and videos
- 🗃️ **Database Operations** - Learn MongoDB integration
- 🤖 **AI Integration** - Explore AI-powered applications
- 🛠️ **Utility Tools** - Practical everyday utilities

---

## 📦 Installation

Most projects require external dependencies. Install them using:

```bash
# For individual projects with requirements.txt
pip install -r requirements.txt

# Common dependencies
pip install tkinter pyautogui opencv-python spellchecker pillow qrcode pymongo python-dotenv
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest new features
- 🔀 Submit pull requests
- ⭐ Star this repository

---

<div align="center">

**Made with ❤️ and Python**

⭐ Star this repo if you find it helpful!

</div>
