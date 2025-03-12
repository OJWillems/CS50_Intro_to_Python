emoticon = ":("

def main():
    global emoticon
    # IF YOU WANT TO MODIFY A GLOBAL VARIABLE IN A LOCAL CONTEXT, YOU HAVE TO SPECIFY IT!
    say("Is anyone there?")
    emoticon = ":)"
    say("Oh, hi!")

def say(phrase):
    print(phrase, emoticon)

main()