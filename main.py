from TextToSpeechModel import TextToSpeechModel
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pyttsx3
import speech_recognition as sr

def main():
    template = """
    Answer the question below.

    Here is the conversation history: {context}

    Question: {question}

    Answer: 
    """
    model = OllamaLLM(model="llama3", max_tokens=100)
    chatbot = TextToSpeechModel(model, template)
    chatbot.handle_conversation()
    
if __name__ == "__main__":    
   main()
