#1843496- Rivan Nayak
# CollegeBoardProject
Hello There My Young Padawan 
General Kenobi (COUGH COUGH)

# Team Goals Completed
1) Completed the Morse code cipher and information page
2) Completed the quiz game, including 10 questions and multiple options for answers on each question based on the different ciphers and their information pages
3) Added a databse (in progress)
4) We were able to successfully deploy it

# CypherCryptoWebsite
# Main.py
This is where the flask runs and where we run all of our python code in our website. We were able to use our python code for the ciphers and run them on the website without having to use html. The main.py also runs everything with the app.routes. Very important for our website.  

# Caesar Cipher
Caesar Cipher is the 2nd option on the navigation bar.
<br/>
The Caesar Cipher is a cipher that encrypts letters with a shift pattern. So "A" with a shift pattern of 1 would be "B" and so on. Same applies with negative numbers as well. There are separate parts for both capitol letters and lowercase letters in the ascii library and it's very important to make sure that it is separate. Same thing applies for decryption except decryption is much harder. This code does the decryption and encryption part of the project for Caesar Cipher only. This code contains functions, loops, input/output, print statements, variables, arrays, and lists. It also has a visual. The Caesar Cipher html files also contaion html tags(<>) which help build the website and structure the website. We were able to use flask and "POST" to run our previous python code, and we were able to add images and videos and change colors as well. Adding a background color was also a hassle as we had to find a good enough picture to fit well.  

# Binary
Binary is the 3rd option on the navigation bar.
<br/>
Binary is basically just a bunch of 1s and 0s combined. This code has functions, variables, input/output, loops, print statements,as well as a couple visuals. This code also holds several html tags(<>) such as p, h, b, etc. A bunch of tags to make up a website. It also contain several html files where we added a background picture, images, and the buttons for the game. This code does the decryption and encryption part of the project for Binary only. It however can't encrypt/decrypt spaces. It can't be fixed, so we recommend doing one word or if multiple words, don't space them. If you do space them, space=100000 

# RSA
RSA is the 4th option on the navigation bar. 
RSA is one of the first public-key cryptology and is widely used for secure data transmission. The acronym RSA is the initial letters of the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman, who publicly described the algorithm in 1977. A user of RSA creates and then publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers must be kept secret. More often, RSA passes encrypted shared keys for symmetric key cryptography which in turn can perform bulk encryption-decryption operations at much higher speed. It's a little similar to the Ceaser Cipher as well. The code has a few similarities too. This code does the decryption and encryption part of the project for RSA only. This code contains functions, loops, input/output, print statements, variables, arrays, and lists. It has a visual too. The html files also contains background pictures, html tags(<>), textbox, buttons, and runs its code from the main.py. 

# Morse Code
Morse Code is the 6th option on the navigation bar.

# Pig Latin
Pig Latin is the 7th option on the navigation bar. 
Pig Latin is a pretty basic language that involves a simple formula for translating words or phrases. To translate from English to Pig Latin, you are to remove everything before the first vowel of the word, moving it to the end, and adding an "ay" at the end of the word. An example of this would be "hello" turning into "ellohay". If the word begins with a vowel, then all you have to do is add "yay" to the end of the word. This means "apple" would turn into "appleyay". For the encryption of Pig Latin, it wasn't too hard. The way we approached it, was by first defining all the vowels. We then used for loops to loop through the word(s) listed by the user, to find the first vowel in each word. We used if and else statements to tell if the vowel was at the beginning, then "yay" would be added on to the end, otherwise everything before the first vowel, along with "ay" would go at the end. Decryption on the otherhand was found to be nearly impossible, as words could be the exactly the same in Pig Latin, but different in English. For example, the words smile and miles are the exact same in Pig Latin, being "ilesmay". The format of the Pig Latin cipher page and the info page are similar to the other ciphers, as it provides an encryption option on the cipher page, as well as some information about Pig Latin, some resources we used and how we coded it on the information page. 

# Scrum Board Overview
Our scrum board consists of several columns in which the scrum master (Noah) records our overall team goals, as well as weekly assignments for the scrum team. The scrum master also tracks the progress made by the group as a whole, and logs whether something may still be in progress, or whether it has been completed. 

# Link to Code
Noah's code:

#runs Pig Latin Cipher encryption
@app.route("/PL_encrypt", methods=['GET','POST'])

With this code, we were able to run an encryption function on our website for Pig Latin, to translate a word or phrase from English to Pig Latin. We used POST to use python code we tested in REPL, and implement it into the main.py file using POST in order to get it to work on the HTML page. 


# Instructions for Running
