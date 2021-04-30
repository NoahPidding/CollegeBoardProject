import rsa


class Cipher:
    def __init__(self, quote):
        self._quote = quote
        # Stack of functions that encrypt
        self._piglatin = self.piglatin()
        self._binary = self.binary()
        self._morse = self.morse()
        self._caesar = self.caesar()
        self._rsa = self.rsa()

    def piglatin(self):
        words = self.quote.split()
        # Constant definition for encryption
        vowels = ['a', 'e', 'i', 'o', 'u']
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
        text = self._quote
        return ''.join(format(ord(i), 'b') for i in text)

    @property
    def bin(self):
        return self._binary

    def morse(self):
        # Morse code has no lower case, so work in upper case
        text = self.quote.upper()
        # constant definitions for encryption
        code = (
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
            ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")
        digit = ("-----", ".----", "...--", "....-", ".....", "-....", "--...", "---..", "----.")
        # Look through each character in the input and add morse code to "morse"
        morse = ""
        for char in text:
            # If it's a letter
            if "A" <= char <= "Z":
                # Use ASCII code to calculate as index for code
                # A=65, B=66... so subtracting 65 gives 0, 1...
                morse += (code[ord(char) - 65] + " ")
            # if it's a digit
            if "0" <= char <= "9":
                # Use the integer version as index for digit
                morse += (digit[eval(char)] + " ")
                # If it's a space
            if char == " ":
                morse += " / "
        return morse

    @property
    def morc(self):
        return self._morse

    def caesar(self):
        # "S" is the key where you shift the letters, or the Caesar Cipher offset
        s = 1
        # Transverse the plain text
        text = self.quote
        # For letter in text1:
        result = []
        for i in range(0, len(text)):
            char = text[i]
            # Encrypt uppercase characters in plain text

            if char.isupper():
                let = chr((ord(char) + s - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            elif char.islower():
                let = chr((ord(char) + s - 97) % 26 + 97)
            else:
                let = chr(ord(char))
            result.append(let)
        return result

    @property
    def caesarc(self):
        return self._caesar

    def rsa(self):
        message = self.quote
        # keys = rsa.keyGen()
        pubkey1 = 9
        pubkey2 = 169133477
        # Get encrypted and make into usable output
        encrypted = rsa.rsa(message, pubkey1, pubkey2)
        encrypted = encrypted[0]
        encrypted = ''.join(encrypted)
        return encrypted

    @property
    def rsac(self):
        return self._rsa


if __name__ == "__main__":
    cipher = Cipher("A man a plan a canal panama")
    print(cipher.quote)
    # The "," separates the words
    print("Pig Latin:", cipher.pig)
    # Binary is one continuous string of 1s and 0s
    print("Binary:", cipher.bin)
    # The "/" means a space for the encryption
    print("Morse Code:", cipher.morc)
    # The "," separates the letters
    print("Caesar Cipher:", cipher.caesarc)
    # The ")" means a space for the encryption
    print("RSA:", cipher.rsac)
