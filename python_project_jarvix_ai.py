import google.generativeai as genai
import os
from google.colab import userdata

try:
    api_key = userdata.get('GOOGLE_API_KEY')
    if api_key is None:
        raise KeyError("GOOGLE_API_KEY not found in Colab secrets.")
except KeyError:
    api_key = os.environ.get('GOOGLE_API_KEY')
    if api_key is None:
        raise ValueError("Gemini API key not found in Colab secrets or environment variables.")

genai.configure(api_key=api_key)
print("Gemini API key configured successfully.")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while True:
  user_input = input("Enter your message: ")
  if user_input.lower() in ["quit", "exit"]:
    break
  response = chat.send_message(user_input)
  print(response.text)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-1.5-flash-latest')
chat = model.start_chat(history=[])

while True:
  user_input = input("Enter your message: ")
  if user_input.lower() in ["quit", "exit"]:
    break
  response = chat.send_message(user_input)
  print(response.text)

import google.generativeai as genai

!pip install gTTS
!pip install IPython

!pip install gTTS
!pip install IPython

import google.generativeai as genai
import os
from google.colab import userdata
from gtts import gTTS
from IPython.display import Audio, display
import random

try:
    api_key = userdata.get('GOOGLE_API_KEY')
    if api_key is None:
        raise KeyError("GOOGLE_API_KEY not found in Colab secrets.")
except KeyError:
    api_key = os.environ.get('GOOGLE_API_KEY')
    if api_key is None:
        raise ValueError("Gemini API key not found in Colab secrets or environment variables.")

genai.configure(api_key=api_key)
print("Gemini API key configured successfully.")

model = genai.GenerativeModel('gemini-1.5-flash-latest')
# Initialize the chat session with an empty history *before* the loop
chat = model.start_chat(history=[])

language = 'en' # Default language is English
# Map language codes to names
language_map = {'en': 'English', 'kn': 'Kannada', 'ta': 'Tamil', 'hi': 'Hindi', 'ru': 'Russian', 'te': 'Telugu', 'ja': 'Japanese', 'ml': 'Malayalam', 'ko': 'Korean', 'tcy': 'Tulu'}

# Predefined greetings for different languages
greetings_map = {
    'en': ["Hello!", "Hi there!", "Hey!"],
    'kn': ["Namaskara!", "ಹಲೋ!"],
    'ta': ["Vanakam!", "வணக்கம்!"],
    'hi': ["Namaste!", "नमस्ते!"],
    'ru': ["Privet!", "Привет!"],
    'te': ["Namaskaram!", "ನಮಸ್ಕಾರಮ್!"],
    'ja': ["Konnichiwa!", "こんにちは！"],
    'ml': ["Namaskaram!", "നಮಸ್കാരം!"],
    'ko': ["Annyeonghaseyo!", "안녕하세요!"],
    'tcy': ["Namaskara!"] # Added a simple greeting for Tulu
}


while True:
    # Customize the input prompt here
    language_options = ", ".join([f"'switch to {code}'" for code in language_map.keys()])
    user_input = input(f"Enter your message (or type {language_options}):\n ")


    if user_input.lower() in ["quit", "exit"]:
        break
    elif user_input.lower().startswith("switch to "):
        lang_code = user_input.lower().replace("switch to ", "").strip()
        if lang_code in language_map:
            language = lang_code
            print(f"Jarvix.AI: Switched to {language_map[language]}.")
        else:
            print(f"Jarvix.AI: Invalid language code.")
        continue

    # Check if the user input is a greeting, making it case-insensitive and stripping whitespace
    user_greetings = ["hello", "hi", "hey", "hi there", "hello there", "good morning", "good afternoon", "good evening", "whats up"]

    # Prioritize predefined greetings for common greeting phrases
    is_greeting = False
    for greeting in user_greetings:
        if user_input.strip().lower().startswith(greeting):
            is_greeting = True
            break

    if is_greeting:
        if language in greetings_map:
            response_text = random.choice(greetings_map[language])
        else:
            response_text = "Hello!" # Default greeting if language not in greetings_map
    else:
        # Modify the prompt to request information about the input in the selected language
        prompt = f"Provide a response in {language_map[language]} language about: {user_input}"
        response = chat.send_message(prompt)
        response_text = response.text

    # Print the chat history for debugging
    print("\n--- Chat History ---")
    for message in chat.history:
        print(f"{message.role}: {message.parts[0].text}")
    print("--------------------\n")


    # Add a newline before printing the response text
    print("\nJarvix.AI:")

    # Adjusting output format - split by paragraphs
    paragraphs = response_text.split('\n\n')
    for paragraph in paragraphs:
        print(paragraph)


    try:
        # Check if the language is supported by gTTS before generating audio
        if language in gTTS.LANGUAGES:
            tts = gTTS(text=response_text, lang=language) # Use selected language for TTS
            tts.save("response.mp3")
            display(Audio("response.mp3", autoplay=True))
        else:
            print(f"Jarvix.AI: Audio output not supported for {language_map[language]}.")

    except Exception as e:
        print(f"Jarvix.AI: Could not generate audio: {e}")

    # Add an extra newline after the output before the next input
    print("\n")

# This cell is a duplicate and can be removed.
# !pip install gTTS
# !pip install IPython

!pip install gTTS
!pip install IPython

import google.generativeai as genai
import os
from google.colab import userdata
from gtts import gTTS
from IPython.display import Audio, display
import random

try:
    api_key = userdata.get('GOOGLE_API_KEY')
    if api_key is None:
        raise KeyError("GOOGLE_API_KEY not found in Colab secrets.")
except KeyError:
    api_key = os.environ.get('GOOGLE_API_KEY')
    if api_key is None:
        raise ValueError("Gemini API key not found in Colab secrets or environment variables.")

genai.configure(api_key=api_key)
print("Gemini API key configured successfully.")

model = genai.GenerativeModel('gemini-1.5-flash-latest')
# Initialize the chat session with an empty history *before* the loop
chat = model.start_chat(history=[])

language = 'en' # Default language is English
# Map language codes to names
language_map = {'en': 'English', 'kn': 'Kannada', 'ta': 'Tamil', 'hi': 'Hindi', 'ru': 'Russian', 'te': 'Telugu', 'ja': 'Japanese', 'ml': 'Malayalam', 'ko': 'Korean', 'tcy': 'Tulu'}

# Predefined greetings for different languages
greetings_map = {
    'en': ["Hello!", "Hi there!", "Hey!"],
    'kn': ["Namaskara!", "ಹಲೋ!"],
    'ta': ["Vanakam!", "வணக்கம்!"],
    'hi': ["Namaste!", "नमस्ते!"],
    'ru': ["Privet!", "Привет!"],
    'te': ["Namaskaram!", "ನಮಸ್ಕಾರಮ್!"],
    'ja': ["Konnichiwa!", "こんにちは！"],
    'ml': ["Namaskaram!", "നಮസ്കാരം!"],
    'ko': ["Annyeonghaseyo!", "안녕하세요!"],
    'tcy': ["Namaskara!"] # Added a simple greeting for Tulu
}


while True:
    # Customize the input prompt here
    language_options = ", ".join([f"'switch to {code}'" for code in language_map.keys()])
    user_input = input(f"Enter your message (or type {language_options}):\n ")


    if user_input.lower() in ["quit", "exit"]:
        break
    elif user_input.lower().startswith("switch to "):
        lang_code = user_input.lower().replace("switch to ", "").strip()
        if lang_code in language_map:
            language = lang_code
            print(f"Jarvix.AI: Switched to {language_map[language]}.")
        else:
            print(f"Jarvix.AI: Invalid language code.")
        continue

    # Check if the user input is a greeting, making it case-insensitive and stripping whitespace
    user_greetings = ["hello", "hi", "hey", "hi there", "hello there", "good morning", "good afternoon", "good evening", "whats up"]

    # Prioritize predefined greetings for common greeting phrases
    is_greeting = False
    for greeting in user_greetings:
        if user_input.strip().lower().startswith(greeting):
            is_greeting = True
            break

    if is_greeting:
        if language in greetings_map:
            response_text = random.choice(greetings_map[language])
        else:
            response_text = "Hello!" # Default greeting if language not in greetings_map
    else:
        # Modify the prompt to request information about the input in the selected language
        prompt = f"Provide a response in {language_map[language]} language about: {user_input}"
        response = chat.send_message(prompt)
        response_text = response.text

    # Print the chat history for debugging
    print("\n--- Chat History ---")
    for message in chat.history:
        print(f"{message.role}: {message.parts[0].text}")
    print("--------------------\n")


    # Add a newline before printing the response text
    print("\nJarvix.AI:")

    # Adjusting output format - split by paragraphs
    paragraphs = response_text.split('\n\n')
    for paragraph in paragraphs:
        print(paragraph)


    try:
        # Generate audio output
        tts = gTTS(text=response_text, lang=language) # Use selected language for TTS
        tts.save("response.mp3")
        display(Audio("response.mp3", autoplay=True))

    except Exception as e:
        print(f"Jarvix.AI: Could not generate audio: {e}")

    # Add an extra newline after the output before the next input
    print("\n")
