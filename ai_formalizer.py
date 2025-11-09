import pyperclip, time, subprocess
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def make_formal(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Make this text more formal:\n\n{text}"}]
    )
    return response.choices[0].message.content.strip()

# Copy selected text
subprocess.run(["osascript", "-e", 'tell application "System Events" to keystroke "c" using {command down}'])
time.sleep(0.3)
text = subprocess.run("pbpaste", capture_output=True, text=True).stdout.strip()

if text:
    formal = make_formal(text)
    subprocess.run("pbcopy", input=formal, text=True)
    subprocess.run(["osascript", "-e", 'tell application "System Events" to keystroke "v" using {command down}'])

