# 1843496- Rivan Nayak


# Team Goals Completed
1) Added more buttons to navigation bar
2) Completed the Pig Latin cipher and information page
3) Completed the Morse code cipher and information page
4) Completed quiz game, including 10 questions and multiple options for answers on each question based on the different ciphers and their information pages
5) Added a databse (in progress)
6) We were able to successfully deploy it

# Scrum Board Overview
Our scrum board consists of several columns in which the scrum master (Noah) records our overall team goals, as well as weekly assignments for the scrum team. The scrum master also tracks the progress made by the group as a whole, and logs whether something may still be in progress, or whether it has been completed. 

# Link to Code
## Noah's code:
#runs Pig Latin Cipher encryption
@app.route("/PL_encrypt", methods=['GET','POST'])
(main.py line 205 - 236)    

[Pig Latin](https://github.com/NoahPidding/CollegeBoardProject/blob/main/main.py#L205-L236)

With the code under this app route, located in the main.py file, I was able to run an encryption function on our website for Pig Latin, to translate a word or phrase from English to Pig Latin. I used python code I tested in REPL to implement it into the main.py file using POST in order to get it to work and running on the HTML page. 

## Nihar's code:
main.py lines (205-236), lines (248-301), the database.html file, the quizgame.html file, and the morsecode.html file. That was all the code I did. 

[Pig latin POST]---(https://github.com/NoahPidding/CollegeBoardProject/blob/main/main.py#L205-L236)

[Morsecode POST]---(https://github.com/NoahPidding/CollegeBoardProject/blob/main/main.py#L248-L301)

[QuizGame]---(https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/QuizGame.html#L1-L388)

[Database]---(https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/database.html#L1-L219)

[Morsecode]---(https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/Morsecode.html#L1-L103)


I added a database like table in the navigation bar and that was the database file. I did the POST stuff for morse code and Pig Latin, I then made all the questions and answers in the quizgame file. I was able to make a dictionary in Javascript and make it into an online quiz. With a submit button and a next/previous button. I will work on connecting that to the database and making the database function as currently I just added it only. The morsecode file is where I added the encrypt/decrypt buttons and used POST to give them their functions and allow them to encrypt and decrypt. I used Python, HTML, Javascript, CSS, and tried using SQLAlchemy but I was having trouble importing the functions and packages. The database still has a lot of work needed. 

## Adam's code:
main.py (Lines 248-301)

[Morsecode](https://github.com/NoahPidding/CollegeBoardProject/blob/main/main.py#L248-L301)

Adam coded the Python for Morse code for both the encryption and the decryption. Lines (248-301). His intellij wasn't working so he emailed his code and his work is commented "Adam's work for Morse code". Nihar did the POST work. 

## Rivan's code:
The quizgame file, the navigation bar

[Quizgame](https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/QuizGame.html#L1-L388)

[Navigation Bar](https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/home.html#L48-L68)

I worked with Nihar mainly and we both worked together on the quizgame file and made the questions and answers and were able to make a Javascript dictionary. I also added the buttons on the navigation bar and was able to aid Nihar with the database. We are currently figuring out how to make the database and the quizgame file work togther. We learned that we needed a lot of POST for this and that's our biggest challenge. 
# Instructions for Running
https://github.com/nighthawkcoders/flask-idea-homesite/blob/master/README.md

The instructions are in the readme.md on this github linked above.
# Link to Website
http://76.176.58.222/

My WIFI turns off at 11:00 so try to grade before that time. Thank you!
# Grading
## Noah 19/20
Noah completed his assignment of implementing the Pig Latin cipher as well as the information pages. He also helped with other parts of the website including some of the styling and format. Being the scrum master, Noah also monitored the scrum board, assigning scrum members to do different tasks and setting goals for the team to complete before the deadline. 

## Nihar 20/20
Nihar has done a lot for the team, as he is the most experienced coder out of us all. He has helped implement both ciphers into the project html pages using POST, while also creating the new quiz game, which included 10 questions and different options for the answers for each question. He also added the database which he is currently working on. He was also able to get the website deployed and running, and has proved very useful and helpful over the weeks, making several big and important commits to the project.  

## Adam 18/20
Adam was able to complete the code for the Morse code cipher in a REPL, however he could not get his Intellij to work, and as a result was unable to make any commits to the project. Because of this he was forced to email the code to others who did have Intellij up and running, and have them implement the code for him. 

## Rivan 18/20
Rivan was able to add more buttons onto the navigation bar we currently had, in which a Pig Latin, Morse code, quiz game and database buttons were added. He also helped a little bit with the addition of the quiz game, however Nihar was the main contributor on that assignment. 
# CollegeBoardProject
Nice call my Young Padawan.
Hello There.
General Kenobi. (COUGH COUGH).
It's over Anikin, I have the high ground.
You Underestimate my power.
Don't try it.
Screams in agony.
"I HATE YOU"

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
