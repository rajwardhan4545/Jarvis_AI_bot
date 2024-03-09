# Jarvis_AI_bot
Jarvis AI
Jarvis AI is a Python script that serves as a virtual assistant, capable of performing various tasks such as responding to voice commands, opening applications, browsing the web, and interacting with users through natural language.

Features:
Voice Recognition: Utilizes the speech_recognition library to recognize voice commands.
Speech Synthesis: Utilizes the win32com.client library to convert text responses into speech.
Web Browsing: Opens specified websites like YouTube, Wikipedia, and Google based on user commands.
Music Playback: Opens a predefined music file when commanded.
Time Information: Provides the current time upon request.
AI Chatbot: Utilizes the OpenAI API to generate responses for general chat queries.
File Generation: Generates text files with OpenAI responses for specified prompts.
Usage:
Install the required dependencies using pip install -r requirements.txt.
Obtain necessary API keys for OpenAI.
Update the apikey variable in the config.py file with your OpenAI API key.
Run the script using python jarvis.py.
Commands:
Open [Website Name]: Opens specified websites like YouTube, Wikipedia, or Google.
Open Music: Plays a predefined music file.
What's the time: Provides the current time.
Jarvis Write [Prompt]: Generates a text file with an OpenAI response based on the provided prompt.
Open [Application Name]: Opens specified applications like Telegram, Visual Studio Code, or IRIS.
Contributing:
Feel free to contribute to this project by forking the repository and submitting pull requests.

