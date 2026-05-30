🛡️ Mobile Threat Hunter (Android + Termux)

📌 Overview

Mobile Threat Hunter is a Python-based cybersecurity tool designed to run on Android using Termux.
It performs file system analysis to identify potential risks such as duplicate files, suspicious file types, and large files.

This project demonstrates real-world endpoint security analysis in a mobile environment.

---

🚀 Features

- 🔍 Detects duplicate files using hash-based analysis (MD5)
- 📦 Identifies large files (>50MB)
- ⚠️ Flags suspicious file types (.apk, .exe, .sh, etc.)
- 📄 Generates a detailed scan report
- 📱 Works entirely on Android using Termux

---

🛠️ Tech Stack

- Python 3
- Termux (Linux environment on Android)
- File hashing (MD5)
- OS file system operations

---

🚀 How to Run

1. Install Termux on your Android device

2. Install Python:
   
   pkg install python

3. Clone the repository:
   
   git clone https://github.com/ZacariahCyberSec/Mobile-Threat-Hunter.git

4. Navigate into the project:
   
   cd Mobile-Threat-Hunter

5. Run the script:
   
   python threat_hunter.py

---

📄 Example Output

[DUPLICATES FOUND]
/sdcard/Download/file1.pdf
/sdcard/Download/file1 (1).pdf

[LARGE FILE]
/sdcard/Download/video.mp4

[SUSPICIOUS FILE]
/sdcard/Download/app.apk

---

🛡️ Use Case (SOC Perspective)

This tool simulates tasks performed by a Security Operations Center (SOC) analyst:

- Monitoring endpoint storage
- Identifying redundant or suspicious files
- Detecting potential risks from unknown file types
- Supporting digital forensic analysis

It demonstrates practical cybersecurity skills in threat detection and system analysis.

---

📂 Project Structure

Mobile-Threat-Hunter/
│── threat_hunter.py
│── sample_report.txt
│── README.md

---

📈 Future Improvements

- 📧 Email alert integration
- 📊 Log monitoring system
- 🌐 Threat intelligence API integration
- ⏱️ Real-time scanning automation

---

👨‍💻 Author

Tinashe Zacariah Nyandoro
Cybersecurity Analyst | Python | Threat Detection

GitHub: https://github.com/ZacariahCyberSec

---

⭐ Acknowledgements

This project is part of a hands-on cybersecurity learning journey focused on building real-world skills using mobile tools.
