#!/usr/bin/env python3
"""
TRAINING SAMPLE ONLY — harmless ransomware-behaviour simulator.

This program is NOT ransomware. It does not encrypt, rename, delete,
overwrite, or transmit user files. It creates a few clearly labelled
dummy files and a ransom-note-like text file inside ./lab_workspace only.
Run it only in the designated disposable Kali lab VM.
"""
from pathlib import Path
import hashlib
import platform
import time

BASE = Path.cwd() / "lab_workspace"
VICTIM_DIR = BASE / "victim_files"
NOTE = BASE / "READ_ME_SIMULATION.txt"
LOG = BASE / "simulation_activity.log"

def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def main():
    print("[SIMULATION] Harmless training sample starting.")
    print("[SIMULATION] Platform:", platform.system(), platform.release())
    print("[SIMULATION] Working directory:", Path.cwd())

    # Create only a dedicated lab directory and dummy data.
    VICTIM_DIR.mkdir(parents=True, exist_ok=True)
    dummy_files = {
        "student_record_demo.txt": "DEMO DATA ONLY - student record example\n",
        "project_report_demo.txt": "DEMO DATA ONLY - project report example\n",
        "photo_description_demo.txt": "DEMO DATA ONLY - photo description example\n",
    }

    for filename, content in dummy_files.items():
        target = VICTIM_DIR / filename
        if not target.exists():
            target.write_text(content, encoding="utf-8")
            print(f"[FILE_CREATE] {target}")
        else:
            print(f"[FILE_EXISTS] {target}")

    # Read the dummy files to generate observable file-access events.
    for target in sorted(VICTIM_DIR.glob("*.txt")):
        data = target.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        print(f"[FILE_READ] {target.name} size={len(data)} sha256={digest[:16]}...")

    # Create a harmless note that imitates a ransomware note for analysis.
    note_text = (
        "TRAINING SIMULATION - NO FILES HAVE BEEN ENCRYPTED\n"
        "This is a harmless ransomware-behaviour exercise for SWS405.\n"
        "Indicator: SIMULATED_RANSOM_NOTE\n"
        "Message: YOUR FILES ARE LOCKED (SIMULATION TEXT ONLY).\n"
        "Do not make any payment. This is not a real incident.\n"
    )
    NOTE.write_text(note_text, encoding="utf-8")
    print(f"[NOTE_CREATE] {NOTE}")

    # Record a small activity log inside the lab directory.
    event = (
        f"{time.strftime('%Y-%m-%d %H:%M:%S')} "
        f"SIMULATION_COMPLETE sha256_marker={sha256_text(note_text)[:16]}\n"
    )
    with LOG.open("a", encoding="utf-8") as handle:
        handle.write(event)
    print(f"[LOG_WRITE] {LOG}")
    print("[SIMULATION] Complete. No encryption, deletion, persistence, or network activity.")

if __name__ == "__main__":
    main()
