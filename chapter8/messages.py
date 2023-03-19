def send_messages(text_messages, sent_messages):
    """Sends all the messages in the text_messages list"""
    if isinstance(text_messages, list) and isinstance(sent_messages, list):
        # Reverse the list so that messages are sent in the ascending order
        reversed_list = text_messages[::-1]
        while reversed_list:
            message = reversed_list.pop()
            print(f"\nSent message '{message}'")
            sent_messages.append(message)
        text_messages.clear()
    else:
        raise ValueError(f"Error: expecting list argument for text messages and sent messages, instead got text_messages={text_messages} and sent_messages={sent_messages}")