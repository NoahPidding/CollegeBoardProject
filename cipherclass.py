class Cipher:
    def __init__(self, quote):
        # constant definitions for encrption
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.code = (".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..")
        self.digit = ("-----",".----","...--","....-",".....","-....","--...","---..","----.")
        # self.morrse = ""
        # stack of functions that encrypt
        self._quote = quote
        self.words = quote.split()
        self._piglatin = self.piglatin()
        self._binary = self.binary()
        self._morse = self.morse()
        text1 = quote
        s = 1
        result1=self.caesar(text1,s)
        sentencecc="".join(result1)
        # self.rsa()

    def piglatin(self):
        words = self.words
        vowels = self.vowels
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
        return words

    @property
    def pig(self):
        return self._piglatin

    @property
    def quote(self):
        return self._quote


    def binary(self):
        B_text = self._quote
        return ''.join(format(ord(i), 'b') for i in B_text)

    @property
    def bin(self):
        return self._binary

    def morse(self):
        # Morse code has no lower case, so work in upper case
        text = self.quote.upper()
        # look through each character in the input and add morse code to "morse"
        morse = ""
        for char in text:
            # if it's a letter
            if char >= "A" and char <= "Z":
                # use ASCII code to calculate as index for code
                # A=65, B=66... so subtracting 65 gives 0, 1...
                morse += (self.code[ord(char)-65] + " ")
            # if it's a digit
            if char >= "0" and char <= "9":
                # use the integer version as index for digit
                morse += (self.digit[eval(char)] + " ")
                # if it's a space
            if char == " ":
                morse += " / "
        return "Morse code: "+morse

    @property
    def morc(self):
        return self._morse

    def caesar(self,text1,s):
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

"""
    def rsa(self):
        message = quote
        keys = rsa.keyGen()
        pubKey1 = 9
        pubKey2 = 169133477
        #get encrypted and make into useable output
        encrypted = rsa.rsa(message, pubKey1, pubKey2)
        encrypted = encrypted[0]
        encrypted = ''.join(encrypted)
        # Private Key = 150317579
"""

if __name__ == "__main__":
    cipher = Cipher("A man a plan a canal panama")
    print(cipher.quote)
    print(cipher.pig)
    print(cipher.bin)
    print(cipher.morc)