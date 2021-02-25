#imports

from flask import Flask, render_template, request, redirect
import rsa
import requests

#create "Flask"
app = Flask(__name__)

#links dictionary
links = {
    'index': 'Home',
    'rsa': "RSA",
    'resources': 'GitHub',
    'test': 'test'}

def Binary_to_Text(binary):

    binary1 = binary
    decimal, d, n = 0, 0 , 0
    while (binary != 0):
        deci = binary % 10
        decimal = decimal + deci * pow(2, d)
        binary = binary//10
        d += 1
    return(decimal)

#home
@app.route('/')
def home():
    return render_template("homepage.html")

#CeaserCipher game
@app.route('/CeaserCipher')
def CeaserCipher():
    return render_template("caesarcipher.html", links = links)

#---------------------------------------------------------------------------
#runs CeaserCipher Game encryption
@app.route("/caesarcipher_encrypt", methods=['GET','POST'])
def encryptionCC():
    if request.method == 'POST':
        form = request.form
        text1 = form["CeaserCipher1"]
        s = int(form["s"])
        def encryptionCC1(text1,s):
            result = []
            # transverse the plain text

            # for letter in text1:
            for i in range(0,len(text1)):
                char = text1[i]
                # Encrypt uppercase characters in plain text

                if (char.isupper()):
                    L = chr((ord(char) + s-65) % 26 + 65)
                # Encrypt lowercase characters in plain text
                elif (char.islower()):
                    L = chr((ord(char) + s - 97) % 26 + 97)
                else:
                    L = chr(ord(char))
                result.append(L)
            return result
        result1=encryptionCC1(text1,s)
        encrypted="".join(result1)
        return render_template("caesarcipher.html", display = encrypted)
    return redirect("/caesarcipher")
#----------------------------------------------------------------------------------------------------------
#runs CeaserCipher Game decryption
@app.route("/caesarcipher_decrypt", methods=['GET','POST'])
def decryptionCC():

    if request.method == 'POST':
        form = request.form
        encrp_msg = form["CeaserCipher1"]
        decrp_key = int(form["s"])

        decrypted_text = []

        for i in range(len(encrp_msg)):
            if ord(encrp_msg[i]) == 32:
                decrypted_text += chr(ord(encrp_msg[i]))

            elif ((ord(encrp_msg[i]) - decrp_key) < 97) and ((ord(encrp_msg[i]) - decrp_key) > 90):
                # subtract key from letter ASCII and add 26 to current number
                temp = (ord(encrp_msg[i]) - decrp_key) + 26
                decrypted_text += chr(temp)

            elif (ord(encrp_msg[i]) - decrp_key) < 65:
                temp = (ord(encrp_msg[i]) - decrp_key) + 26
                decrypted_text += chr(temp)

            else:
                decrypted_text += chr(ord(encrp_msg[i]) - decrp_key)

        decrypted="".join(decrypted_text)
        return render_template("caesarcipher.html", display = decrypted)
    return redirect("/caesarcipher")

#Caesar Cipher Information Page
@app.route('/CaesarCipherInfo')
def CaesarCipherInfo():
    return render_template("caesarcipherinfo.html", links = links)
#------------------------------------------------------------------------------------------------------------
#binary game
@app.route('/binary')
def binaryEX():
    return render_template("binary.html", links = links)

#runs Binary Cipher encryption
@app.route("/bin_encrypt", methods=['GET','POST'])
def encryption():
    if request.method == 'POST':
        form = request.form
        B_text = form["bin1"]
        result = ''.join(format(ord(i), 'b') for i in B_text)
        return render_template("Binary.html", display = result)
    return redirect("/binary")

#runs Binary Cipher decryption
@app.route("/bin_decrypt", methods=['GET','POST'])
def decryption():
    if request.method == 'POST':
        form = request.form
        B_text = form["bin1"]
        string = ' '
        for d in range(0, len(B_text), 7):
            temporary = int(B_text[d:d + 7])
            decimal_data = Binary_to_Text(temporary)
            string = string + chr(decimal_data)
        return render_template("Binary.html", display = string)
    return redirect("/binary")

@app.route("/BinaryInfo")
def BinaryInfo():
    return render_template("binaryinfo.html")

#rsa demonstration
#default RSA (rsa encrypt)
@app.route ("/rsa", methods = ["POST", "GET"])
def rsaEncrypt ():
    if request.method == "POST":
        #get message
        message = request.form["msg"]
        #get keys
        pubKey1 = int(request.form["iKey1"])
        pubKey2 = int(request.form["iKey2"])
        #get encrypted and make into useable output
        encrypted = rsa.rsa(message, pubKey1, pubKey2)
        encrypted = encrypted[0]
        encrypted = ''.join(encrypted)
        #render page with output
        return render_template ("rsa.html", key1 = "Public Key 1", key2 = "Public Key 2", outputDisplay = "Encrypted", encrypted = "Encrypted: ", output = encrypted, page = "Encrypt", op1 = "KeyGenerator", op2 = "Decrypt", link1 = "rsa/key-generator", link2 = "rsa/decrypt")
    #render page without output
    else:
        return render_template ("rsa.html", page = "Encrypt", key1 = "Public Key 1", key2 = "Public Key 2", op1 = "Key Generator", op2 = "Decrypt", link1 = "rsa/key-generator", link2 = "rsa/decrypt")

#rsa key generator
@app.route('/rsa/key-generator', methods = ["POST", "GET"])
def rsaKeyGen():
    if request.method == "POST":
        #get message
        message = request.form["msg"]
        #generate keys
        keys = rsa.keyGen()
        pubKey1 = keys[0]
        pubKey2 = keys[1]
        privKey = keys[2]
        #encrypt message
        encrypted = rsa.rsa(message, pubKey1, pubKey2)
        encrypted = encrypted[0]
        encrypted = ''.join(encrypted)
        return render_template ("keygen.html", display = "Encrypted", display1 = "Public Key 1", display2 = "Public Key 2", display3 = "Private Key", output = encrypted, pubKey1 = pubKey1, pubKey2 = pubKey2, privKey = privKey, op1 = "Encrypt", op2 = "Decrypt", link1 = "/rsa", link2 = "/rsa/decrypt")
    else:
        return render_template ("keygen.html", op1 = "Encrypt", op2 = "Decrypt", link1 = "/rsa", link2 = "/rsa/decrypt")

#rsa decrypt
@app.route ('/rsa/decrypt', methods = ["POST", "GET"])
def rsaDecrypt():
    if request.method == "POST":
        #get message
        #get message
        message = request.form["msg"]
        #get keys
        pubKey1 = int(request.form["iKey1"])
        privKey = int(request.form["iKey2"])
        #get encrypted and make into useable output
        decrypted = rsa.rsa(message, pubKey1, privKey)
        decrypted = decrypted[0]
        decrypted = ''.join(decrypted)
        #render page with output
        return render_template ("rsa.html", page = "Decrypt", key1 = "Public Key 1", key2 = "Private Key", op1 = "Encrypt", op2 = "Key Generator", link1 = "/rsa", link2 = "key-generator", outputDisplay = "Decrypted", output = decrypted)
    else:
        return render_template ("rsa.html", page = "Decrypt", key1 = "Public Key 1", key2 = "Private Key", op1 = "Encrypt", op2 = "Key Generator", link1 = "/rsa", link2 = "key-generator")

#rsa info
@app.route('/about-rsa')
def rsaAbout():
    return render_template("rsainfo.html")

#Pig Latin game
@app.route('/PigLatin')
def PigLatin():
    return render_template("PigLatin.html", links = links)

#runs Pig Latin Cipher encryption
@app.route("/PL_encrypt", methods=['GET','POST'])
def encryptionPL():
    if request.method == 'POST':
        form = request.form
        #!/usr/bin/env python
        # This program translates a string to Pig Latin
        sentence = form["PL1"]
        vowels = ['a', 'e', 'i', 'o', 'u']
        # Split sentence into a list of words
        words = sentence.split()
        for i, word in enumerate(words):
            # Split each word into a list of letters
            letters = list(word)
            first_vowel = 0
            # Loop through letters of the word to find the first vowel
            for j, letter in enumerate(letters):
                if letter.lower() in vowels:
                    first_vowel = j
                    break
            # Add 'yay' if the word starts with a vowel
            if first_vowel == 0:
                word = word + "yay"
            # Otherwise, move the beginning consonants + 'ay' to the end of the word
            else:
                word = word[first_vowel:len(word)] + word[0:first_vowel] + "ay"
            # Replace the English word with the Pig Latin word in the list
            words[i] = word.lower()
        # Reconstructs a new Pig Latin sentence from the list of words
        sentence = " ".join(words)
        return render_template("PigLatin.html", display = sentence)
    return redirect("/PigLatin")

#Pig Latin info
@app.route('/PigLatininfo')
def PigLatininfo():
    return render_template("PigLatininfo.html")

#Morse Code
@app.route('/Morsecode')
def Morsecode():
    return render_template("Morsecode.html")

#runs Pig Latin Cipher encryption
@app.route("/MC_encrypt", methods=['GET','POST'])
def encryptionMC():
    if request.method == 'POST':
        form = request.form
        while True:
            encryptoutput =(".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. ")
            alphabet = list(encryptoutput.split(" "))
            encryptinput=('a b c d e f g h i j k l m n o p q r s t u v w x y z ' )
            encrypt=list(encryptinput.split(" "))
            morse=""
            userinput= form["MC1"]

            for i in userinput.lower():
                if i.isspace():
                    morse+=" / "

                else:
                    counter=-1
                    while i != encrypt[counter]:
                        counter+=1
                        if i == encrypt[counter]:
                            morse+=alphabet[counter] + " "
            sentence="Morse code: "+morse
            return render_template("Morsecode.html", display = sentence)
    return redirect("/Morsecode")

#runs Pig Latin Cipher decryption
@app.route("/MC_decrypt", methods=['GET','POST'])
def decryptionMC():
    if request.method == 'POST':
        form = request.form
        while True:
            decrpytoutput =("a b c d e f g h i j k l m n o p q r s t u v w x y z ")
            alphabet = list(decrpytoutput.split(" "))
            decryptinput=(  '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. ')
            encrypt=list(decryptinput.split(" "))
            morse=""
            userinput= form["MC1"]
            newlist = list(userinput.lower().split(" "))

            for i in range(len(newlist)):
                if(newlist[i] == "/") :
                    morse+= " "
                    continue
                index = encrypt.index(newlist[i])

                morse+=alphabet[index]

            sentence= "Output: "+morse
            return render_template("Morsecode.html", display = sentence)
    return redirect("/Morsecode")

#Morse Code info
@app.route('/Morsecodeinfo')
def Morsecodeinfo():
    return render_template("Morsecodeinfo.html")

#Quiz Game
@app.route('/QuizGame')
def QuizGame():
    return render_template("QuizGame.html")

#Database
@app.route('/database')
def Database():
    return render_template("database.html")

@app.route('/easteregg')
def easteregg():
    return render_template("easteregghomepage.html")

@app.route('/api',  methods=['GET', 'POST'])
def api():
    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        'x-rapidapi-key': "fbc28ca63amsh13b8750406531e6p1bf8a9jsnabe9c216b21b",
        'x-rapidapi-host': "quotes15.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    quote = response.json().get('content')
    """print(response.text)"""
    sentencepl = quote
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Split sentence into a list of words
    words = sentencepl.split()
    for i, word in enumerate(words):
        # Split each word into a list of letters
        letters = list(word)
        first_vowel = 0
        # Loop through letters of the word to find the first vowel
        for j, letter in enumerate(letters):
            if letter.lower() in vowels:
                first_vowel = j
                break
        # Add 'yay' if the word starts with a vowel
        if first_vowel == 0:
            word = word + "yay"
        # Otherwise, move the beginning consonants + 'ay' to the end of the word
        else:
            word = word[first_vowel:len(word)] + word[0:first_vowel] + "ay"
        # Replace the English word with the Pig Latin word in the list
        words[i] = word.lower()
    # Reconstructs a new Pig Latin sentence from the list of words
    sentencepl = " ".join(words)

    B_text = quote
    result = ''.join(format(ord(i), 'b') for i in B_text)

    code = (".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..")
    # tuple containing the Morse code for digits
    digit = ("-----",".----","...--","....-",".....","-....","--...","---..","----.")
    morse = ""
    # Morse code has no cases, so work in upper case
    text = quote.upper()
    # look through each character in the input
    for char in text:
        # if it's a letter
        if char >= "A" and char <= "Z":
            # use ASCII code to calculate as index for code
            # A=65, B=66... so subtracting 65 gives 0, 1...
            morse += (code[ord(char)-65] + " ")
        # if it's a digit
        if char >= "0" and char <= "9":
            # use the integer version as index for digit
            morse += (digit[eval(char)] + " ")
            # if it's a space
        if char == " ":
            morse += " / "

    text1 = quote
    s = 1
    def encryptionCC1(text1,s):
        result = []
        # transverse the plain text

        # for letter in text1:
        for i in range(0,len(text1)):
            char = text1[i]
            # Encrypt uppercase characters in plain text

            if (char.isupper()):
                L = chr((ord(char) + s-65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            elif (char.islower()):
                L = chr((ord(char) + s - 97) % 26 + 97)
            else:
                L = chr(ord(char))
            result.append(L)
        return result
    result1=encryptionCC1(text1,s)
    sentencecc="".join(result1)

    message = quote
    keys = rsa.keyGen()
    pubKey1 = 9
    pubKey2 = 169133477
    #get encrypted and make into useable output
    encrypted = rsa.rsa(message, pubKey1, pubKey2)
    encrypted = encrypted[0]
    encrypted = ''.join(encrypted)
    # Private Key = 150317579
    return render_template("api.html", quote=quote, encryptPL=sentencepl, binary=result, encryptMC=morse, encryptCC=sentencecc, encryptRSA=encrypted)

#account login
@app.route('/security')
def security():
    return render_template("security.html")

#profile
@app.route('/profile')
def profile():
    return render_template("profile.html")

#about us
@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

#run file
if __name__ == "__main__":
    app.run(debug = True)

