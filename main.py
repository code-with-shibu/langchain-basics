from agent.chat_agent import get_chat_response

def main():
    response = get_chat_response("5 multiplied by 6 and then add 123, then add 2345 and then multiply by 234", thread_id="test_thread_2")
    print(response)
    
#5 multiplied by 6 and then add 123, then add 2345 and then multiply by 234

if __name__ == "__main__":
    main()
