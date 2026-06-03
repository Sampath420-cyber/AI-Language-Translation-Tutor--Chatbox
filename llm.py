import asyncio

from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm():

    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key="AIzaSyCcGcTxph99Dhj0XD_EpKv_i3o3H4yuF5Y",
        temperature=0.3
    )