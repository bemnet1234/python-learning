def emoji_converter(text):
    words= text.split(" ")
    emojis={
        ":)": "😊",
        ":(": "😞"
    }
    output=""
    for word in words:
        output += emojis.get(word, word) + " "  
    return output
text=input(">")
output=print(emoji_converter(text))
