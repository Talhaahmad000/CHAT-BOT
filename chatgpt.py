def chatbot(user):
    user = user.lower()

    if "hello" in user:
        return "hi!"
    elif "how are you" in user:
        return "i'm fine thanks!"
    elif "bye" in user:
        return "good bye"
    else:
        return "ur prompt is wrong"


while True:
    print("how my chatbot help u")
    user = input("enter ur prompt: ")
    response = chatbot(user)
    print("chatbot reply:", response)

    if "bye" in user.lower():
        exit()