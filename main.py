from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()

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
        user_input = input("You: ")
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

    while(1):    
    # Exception handling to handle
    # exceptions at the runtime
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level 
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input 
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print(f"Did you say: {MyText}")

        except sr.RequestError as e:
            print(f"Could not request results;{e}")
            
        except sr.UnknownValueError:
            print("Unknown Error occurred")


if __name__ == "__main__":
    #handle_conversation()
    speech_to_text()