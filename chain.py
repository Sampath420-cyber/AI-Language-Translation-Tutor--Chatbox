from llm import get_llm
from prompt import prompt

llm = get_llm()

chain = prompt | llm


class SimpleConversationChain:

    def invoke(self, data, config=None):

        response = chain.invoke(
            {
                "input": data["input"]
            }
        )

        return response


conversation_chain = SimpleConversationChain()