import getpass
import os
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")


hello = model.invoke("Hello, world!")

print(hello.content)

##################
print("\n__________________________________________\n__________________________________________\n")
##################

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage("Translate the following from English into French"),
    HumanMessage("hello there, I am a translated text !"),
]

traduction = model.invoke(messages)

print(traduction.content)

##################
print("\n__________________________________________\n__________________________________________\n")
##################

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage("Maomao est le potit chat d'Elise"),
    HumanMessage("Est-ce que Maomao sera grand plus tard ?"),
]

test = model.invoke(messages)

print(test.content)