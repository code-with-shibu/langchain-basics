from agent.utils.llm import llm_client
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage



def get_chat_response(user_message: str, thread_id: str) -> str:
    
    # message = HumanMessage(content=user_message)

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    response = llm_client.agent.invoke(
        {
            "messages": [user_message]
        },
        config=config
    )

    return response["messages"][-1].content



