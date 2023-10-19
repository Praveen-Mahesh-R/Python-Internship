from nltk.chat.util import Chat, reflections

#questions and it's responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?",
        ["My name is Chatty!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) (place) ?",
        ['I live in some secret corner of the computer you are using right now',]
    ],
    [
        r"how is your health(.*)",
        ["I'm always healthy as long as this computer is healthy",]
    ],
    [
        r"(.*) fact",
        ["Alexander Graham Bell, who invented the telephone in 1876, suggested answering calls with \"ahoy.\"","Africa is the only continent with land in all four hemispheres.","The odds of giving birth to a baby at 12:01 a.m. on January 1 are around 1 in 526,000—roughly the same as the odds of getting struck by lightning."]
    ],
    [
        r"(.*) joke",
        ["What is the least spoken language in the world? \nSign Language","The Sergeant-Major growled at the young soldier: I didn’t see you at camouflage training this morning. \nThank you very much, sir.","What do you call a group of killer whales playing instruments? \nAn Orca-stra."]
    ],
    [
        r"quit",
        ["Bye have a great day :) ","It was nice talking to you. hi:)"]
    ],
]
#function to call chatbot instance
def chat():
    print("Hi! I am a chatbot, nice to meet you!!")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()