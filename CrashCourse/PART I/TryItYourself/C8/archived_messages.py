messages = ['I hate you.', 'You smell like a baboon.',
            'I am a legend.', 'They can stop it!']


def show_messages(msgs):
    print('The messages are:')
    for msg in msgs:
        print(f"- {msg}")


sent_messages = []


def send_messages(msgs, sent_msgs):
    while msgs:
        msg = msgs.pop(0)
        sent_msgs.append(msg)
    return sent_msgs


send_messages(messages[:], sent_messages)  # Use a copy of the messages list, retaining its contents! 
print(messages)
print(sent_messages)
# The messages list has not been changed!
