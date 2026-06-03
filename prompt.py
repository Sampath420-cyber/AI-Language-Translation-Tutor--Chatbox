from langchain.prompts.chat import ChatPromptTemplate

SYSTEM_PROMPT = """
You are an AI Language Translation and Vocabulary Tutor.
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", "{input}")
    ]
)