import os
from collections import defaultdict
import hashlib

# 🔧 CONFIG
SCAN_PATH = "/sdcard/Download"
REPORT_FILE = "/sdcard/threat_report.txt"
AUTO_DELETE = False  # change to True to enable auto cleanup

suspicious_extensions = (".apk", ".exe", ".sh", ".bat")

duplicate_files = defaultdict(list)
report_lines = []


# 🔐 Function to hash files (memory efficient)
def get_file_hash(filepath):
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except:
        return None


# 🚀 Scan files
for root, dirs, files in os.walk(SCAN_PATH):
    for file in files:
        full_path = os.path.join(root, file)

        try:
            size = os.path.getsize(full_path)
        except:
            continue

        # 📦 Large file detection (>50MB)
        if size > 50 * 1024 * 1024:
            report_lines.append(f"[LARGE FILE] {file} - {size/1024/1024:.2f} MB")

        # ⚠️ Suspicious file detection
        if file.lower().endswith(suspicious_extensions):
            report_lines.append(f"[SUSPICIOUS FILE] {file}")

        # 🧬 Duplicate detection
        file_hash = get_file_hash(full_path)
        if file_hash:
            duplicate_files[file_hash].append(full_path)


# 🧹 Process duplicates
for hash_value, file_list in duplicate_files.items():
    if len(file_list) > 1:
        report_lines.append("\n[DUPLICATES FOUND]")

        for i, f in enumerate(file_list):
            report_lines.append(f)

            # 🔥 AUTO_DELETE = True
            if AUTO_DELETE and i > 0:
                try:
                    os.remove(f)
                    report_lines.append(f"[DELETED] {f}")
                except:
                    report_lines.append(f"[FAILED DELETE] {f}")


# 📝 Save report
with open(REPORT_FILE, "w") as f:
    f.write("\n".join(report_lines))


print("✅ Scan complete. Report saved to:", REPORT_FILE)
