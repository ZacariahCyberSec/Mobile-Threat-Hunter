# 🛡️ Mobile Threat Hunter (Termux + Python)

## 📌 Overview
Mobile Threat Hunter is a lightweight cybersecurity tool built using Python and Termux on Android. It scans device storage to detect:

- Duplicate files (hash-based detection)
- Large files consuming storage
- Suspicious file types (.apk, .exe, .sh)

This project simulates real-world endpoint analysis and threat detection workflows.

---

## ⚙️ Features

- 🔍 Recursive file scanning
- 🧬 MD5 hash-based duplicate detection
- 📦 Large file identification (>50MB)
- ⚠️ Suspicious file detection
- 🧹 Optional automatic duplicate cleanup
- 📄 Report generation

---

## 🛠️ Technologies Used

- Python 3
- Termux (Android Linux environment)
- File system analysis techniques

---

## 🚀 How to Run

```bash
pkg install python
termux-setup-storage

python threat_hunter.py
