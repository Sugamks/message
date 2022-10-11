from nltk.chat.util import Chat,reflections
def main(input):
    reflections = {
        "i am"       : "you are",
        "i was"      : "you were",
        "i"          : "you",
        "i'm"        : "you are",
        "i'd"        : "you would",
        "i've"       : "you have",
        "i'll"       : "you will",
        "my"         : "your",
        "you are"    : "I am",
        "you were"   : "I was",
        "you've"     : "I have",
        "you'll"     : "I will",
        "your"       : "my",
        "yours"      : "mine",
        "you"        : "me",
        "me"         : "you"
    }
    pairs=[
        ["my name is (.*)",["Hello %1, How are you today ?"]],
        ["(hi|hey|hs anyone there|hello|good day)",["Hey :-)","Hello, thanks for visiting","Hi there, what can I do for you?","Hi there, how can I help?"]],
        ["(.*) your name ?",["My name is EDITH"]],
        ["how are you ?",["I'm doing goodnHow about You ?"]],
        ["sorry",["Its alright","Its OK, never mind"]],
        ["i am fine",["Great to hear that, How can I help you?"]],
        ["(i'm|i am|im) doing good",["Nice to hear that","How can I help you?:)"]],
        ["(what do you do|what can you do|what is your purpose|what do you serve)"["I am a Chat Bot for E-commerce, where i can answer your questions regarding the products"]],
        ["quit",["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]],
    ]
    chat = Chat(pairs,reflections)
    output = chat.respond(input)
    return ""+str(output)