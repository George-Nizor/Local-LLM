from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pyttsx3
import speech_recognition as sr



class TextToSpeechModel:
    def __init__(self, model, template):
        self.model = model
        self.template = template
        self.prompt = ChatPromptTemplate.from_template(template)
        self.chain = self.prompt | self.model
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)


    def speech_to_text(self):
        """
        Convert spoken words into text using Google's speech recognition API.

        This function listens for audio input from the microphone and attempts
        to recognize the spoken words using the Google Web Speech API. If successful,
        it returns the recognized text. In case of a request error or an unrecognized
        speech, it handles the exceptions by printing appropriate error messages.

        Returns:
            str: The recognized text from the audio input.

        Raises:
            sr.RequestError: If the API is unavailable or there is a connection issue.
            sr.UnknownValueError: If the speech is unintelligible or cannot be recognized.
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something...")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said: " + r.recognize_google(audio))
                return text
            except sr.RequestError:
                print("API unavailable")
            except sr.UnknownValueError:
                print("Unable to recognize speech")

    def handle_conversation(self) -> None:
        """
        Handle a conversation with the AI model, using speech-to-text input and text-to-speech output.
        """
        context = ""
        print("Welcome to the AI ChatBot, say 'exit' to quit.")
        while True:
            user_input = self.speech_to_text()
            if not user_input:
                continue
            if user_input.lower() == "exit":
                break

            result = self.chain.invoke({"context": context, "question": user_input})
            self.engine.say(result)
            print("Bot: ", result)
            self.engine.runAndWait()
            self.engine.stop()
            context += f"\nUser: {user_input}\nAI: {result}"