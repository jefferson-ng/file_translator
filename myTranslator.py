from translate import Translator
translator = Translator(to_lang="de")

try:
    with open("./toTranslate.txt", mode="r") as toTranslate:
        text = toTranslate.read()
except FileNotFoundError as e:
    print("Check your file path ,Buddy!")


translation = translator.translate(text)
translated = open("translated.txt", mode="w")
translated.write(translation)
translated.close()
print(translation)
