# AI Text Formalizer

A macOS utility to quickly make selected text more formal using Google Gemini.

---

## Features

* Works as a macOS Service / Quick Action.
* Trigger via menu or custom keyboard shortcut (e.g., Cmd+M).
* Automatically copies selected text, sends it to Gemini for formalization, and pastes the result.
* Uses a dedicated Python virtual environment for dependencies.

---

## Requirements

* macOS 10.15+
* Python 3.10+
* Google Gemini API access
* Python packages: `google-generativeai`, `pyperclip`

---

## Installation

1. Clone the repository:

```bash
cd getformal
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install pyperclip google-generativeai
```

4. Set up Automator / Shortcuts with the shell script:

```zsh
cd "<project-folder>"
./venv/bin/python3 ai_formalizer.py
```

---

## Usage

1. Select any text in any macOS application.
2. Trigger the Quick Action from **Services → Formalize Text** or your custom shortcut.
3. The text is replaced with a more formal version automatically.

---

## Notes

* Ensure macOS Accessibility permissions are granted for Automator/Shortcuts to simulate clipboard actions.
* The script uses Gemini via `google-generativeai`. Make sure your API key is correctly set in `ai_formalizer.py`.
