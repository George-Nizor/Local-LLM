from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()

class TextToSpeechModel:

    def __init__(self, engine, model, template):
        self.model = model
        self.engine = engine
        self.prompt = ChatPromptTemplate(template)
        self.chain = prompt | model
        self.voices = engine.getProperty('voices')
        
    def handle_conversation():
        context = ""
        print("Welcome to the AI ChatBot, Type 'exit' to quit")
        while True:
            user_input = speech_to_text()
            if user_input.lower() == "exit":
                break
        result = chain.invoke({"context":context,"question":user_input})
        engine.say(result)
        print("Bot: ", result)
        engine.runAndWait()
        engine.stop()
        context += f"\nUser: {user_input}\nAI: {result}"


template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""

model = OllamaLLM(model="llama3", max_tokens = 100)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def handle_conversation():
    context = ""
    print("Welcome to the AI ChatBot, Type 'exit' to quit")
    while True:
        user_input = speech_to_text()
        if user_input.lower() == "exit":
            break
        
        result = chain.invoke({"context":context,"question":user_input})
        engine.say(result)
        print("Bot: ", result)
        engine.runAndWait()
        engine.stop()
        context += f"\nUser: {user_input}\nAI: {result}"

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        try:
            print("You said: " + r.recognize_google(audio))
            return text
        except sr.RequestError:
            print("API unavailable")
        except sr.UnknownValueError:
            print("Unable to recognize speech")


if __name__ == "__main__":
    handle_conversation()    
