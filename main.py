from agent.chat_agent import get_chat_response

def main():
    response = get_chat_response("What is my name?", thread_id="test_thread_2")
    print(response)


if __name__ == "__main__":
    main()
