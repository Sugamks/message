from nltk.chat.util import Chat,reflections
def main(input):
    pairs=[
        ["(Hi|Hey|How are you|Is anyone there|Hello|Good day)",["Hey :-)","Hello, thanks for visiting","Hi there, what can I do for you?","Hi there, how can I help?"]]
    ]
    chat = Chat(pairs,reflections)
    output = chat.respond(input)
    return ""+str(output)