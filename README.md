# 🧠 Personal Voice Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-blue.svg)](CONTRIBUTING.md)

A voice-controlled Python assistant that can perform various tasks such as searching Wikipedia, sending emails, playing music, opening popular websites, checking the time, and launching applications — all by just using your voice!

## 👤 Author

## Author

- [@manojchoudhary404](https://github.com/manojchoudhary404)

---

## 🔧 Tech Stack

- **Python 3.8+**
- `speech_recognition` – For converting speech to text
- `pyttsx3` – For text-to-speech conversion
- `wikipedia` – To fetch summaries
- `smtplib` – To send emails
- `webbrowser` – For opening websites
- `os` – For system interactions
- `datetime` – For fetching current time

---

## 🎯 Features

- 🎙️ Voice-controlled interaction
- 📚 Search topics on Wikipedia
- 📧 Send emails via SMTP
- 🎵 Play music from local storage
- 🌍 Open websites like YouTube, Google, GitHub, etc.
- 🕒 Get current time using system clock
- 🖥️ Launch Visual Studio Code
- 🛑 Exit assistant using voice command

---

## 🗣️ Voice Commands

| Command                        | Description                                |
|-------------------------------|--------------------------------------------|
| ` Google [topic]   `          | Google search results are open in your default browser
| `Wikipedia [topic]`           | Search and summarize a Wikipedia topic     |
| `Email to [name]`             | Send an email to a predefined contact      |
| `Play music`                  | Play music from your local folder          |
| `Open YouTube`                | Launch YouTube in your browser             |
| `Open Google`                 | Open Google homepage                       |
| `Open GitHub`                 | Navigate to GitHub                         |
| `Open drive`                  | Access Google Drive                        |
| `Open stackoverflow`          | Open Stack Overflow                        |
| `What is the time`            | Speak the current system time              |
| `Open code`                   | Open Visual Studio Code                    |
| `Exit`                        | Close the assistant                        |

---

## 🧪 Example Interactions

- **You:** *"Wikipedia Python"*  
  **Assistant:** *"According to Wikipedia, Python is a programming language..."*

- **You:** *"Play music"*  
  **Assistant:** *Playing your favorite track...*

- **You:** *"Open YouTube"*  
  **Assistant:** *Opening YouTube...*

---

## 🛠️ Installation

Follow these steps to set up the assistant on your local machine:

```bash
# 1. Clone the repository
git clone https://github.com/manojchoudhary404/PersonalVoiceAssistant.git

# 2. Navigate to the project directory
cd PersonalVoiceAssistant

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the assistant
python main.py

```

## 📁 Folder Structure

```
PersonalVoiceAssistant/
├── assets/                  # (Optional) Icons, audio clips, etc.
├── music/                   # Folder for local music files
├── main.py                  # Main script to start the assistant
├── requirements.txt         # Python package requirements
├── README.md                # This documentation
└── LICENSE                  # Project license (MIT)
```

## 🛣️ Roadmap

- [ ] Add more intelligent commands  
- [ ] Improve accuracy of speech recognition  
- [ ] Add multi-language support  
- [ ] Integrate Google Calendar and Maps  
- [ ] Implement GUI interface (optional)

## 🤝 Contribution

Contributions are welcome!

```bash
# Fork this repo
# Create a new branch: git checkout -b feature/FeatureName
# Commit your changes: git commit -m "Add feature"
# Push to your branch: git push origin feature/FeatureName
# Open a Pull Request 🎉
```

## 📫 Contact Me
####  I’m always open to questions, suggestions, or collaborative opportunities! Feel free to connect with me through:

- LinkedIn: [Manoj Choudhary](www.linkedin.com/in/manoj-choudhary7)
- github: [@manojchoudhary404](https://github.com/manojchoudhary404)
- Email: manojchoudhary7.in@gmail.com

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

© 2025 Manoj T Choudhary. This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- Thanks to the Python community and open-source libraries.
- Voice recognition powered by [Google Speech Recognition](https://pypi.org/project/SpeechRecognition/).
- Documentation and debugging help from Stack Overflow.

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on [GitHub](https://github.com/[YourGitHubUsername]/PersonalVoiceAssistant)!






