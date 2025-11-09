import pyperclip, time, subprocess
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel("gemini-flash-latest")

def make_formal(text):
    prompt = f"""Rewrite the following text in a more formal, corporate and kind tone. Return ONLY the rewritten text with no explanations, alternatives, or additional formatting:

{text}"""
    response = model.generate_content(prompt)
    return response.text.strip()

# Copy selected text
subprocess.run(["osascript", "-e", 'tell application "System Events" to keystroke "c" using {command down}'])
time.sleep(0.3)
text = subprocess.run("pbpaste", capture_output=True, text=True).stdout.strip()

if text:
    formal = make_formal(text)
    subprocess.run("pbcopy", input=formal, text=True)
    subprocess.run(["osascript", "-e", 'tell application "System Events" to keystroke "v" using {command down}'])

