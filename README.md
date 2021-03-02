### (1843496- Rivan Nayak)

# Link to Website
[Link to CypherCrypto](http://76.176.58.222:8080/)

# Scrum Board Overview
[Scrum Board](https://github.com/NoahPidding/CollegeBoardProject/projects/1)

[Project (Scope)Plan](https://docs.google.com/document/d/1BwrLotvabNXMWuHMsrePWA0r2USNPfR9TTbbI6gdCSU/edit)

Our scrum board consists of several columns in which the scrum master (Noah) records our overall team goals, as well as weekly assignments for the scrum team. The scrum master also tracks the progress made by the group as a whole, and logs whether something may still be in progress, or whether it has been completed. 

# CypherCryptoWebsite
CypherCrypto is a website where different ciphers such as Caesar Cipher and Binary can be used to encrypt and decrypt messages inputted by a user. Our website contains 5 different ciphers including Caesar Cipher, Binary, RSA, Morse Code and Pig Latin. There are information pages on all the ciphers which provide a history of the cipher and how it generally works. The user can then use the ciphers by inputting messages into textboxes and choosing to either encrypt or decrypt the message. There is also a multiple choice quiz game on the site, which tests the user on their knowledge of the ciphers based on the information pages of the ciphers. The stats of the quiz are then recorded on a table like database, so the user is able to see their scores, attempts an questions they got wrong. There is also a message encryptor section, which we used an API to get random quotes, then used all of our ciphers to encrypt the message to display the encrypted quote with the corresponding cipher. 

# Technicals Achieved
Below is a list of the technicals and other things we incorporated into our website, including our ciphers, quiz, databse, api/quote encryptor and easter egg, along with the process and methods we used to code, and how it generally is intended to function. 

## Ciphers
### Caesar Cipher (Made by Tri 1 students)
The Caesar Cipher is a cipher that encrypts letters with a shift pattern. So "A" with a shift pattern of 1 would be "B" and so on. Same applies with negative numbers as well. There are separate parts for both capitol letters and lowercase letters in the ascii library and it's very important to make sure that it is separate. Same thing applies for decryption except decryption is much harder. This code does the decryption and encryption part of the project for Caesar Cipher only. This code contains functions, loops, input/output, print statements, variables, arrays, and lists. It also has a visual. The Caesar Cipher html files also contaion html tags(<>) which help build the website and structure the website. We were able to use flask and "POST" to run our previous python code, and we were able to add images and videos and change colors as well. Adding a background color was also a hassle as we had to find a good enough picture to fit well.  

[Link to py code]() | [Runtime link to cipher](http://76.176.58.222:8080/CeaserCipher)

[Link to html code]() [Runtime link to info](http://76.176.58.222:8080/CaesarCipherInfo)

[Link to info page code]()

### Binary (Made by Tri 1 students)
Binary is basically just a bunch of 1s and 0s combined. This code has functions, variables, input/output, loops, print statements,as well as a couple visuals. This code also holds several html tags(<>) such as p, h, b, etc. A bunch of tags to make up a website. It also contain several html files where we added a background picture, images, and the buttons for the game. This code does the decryption and encryption part of the project for Binary only. It however can't encrypt/decrypt spaces. It can't be fixed, so we recommend doing one word or if multiple words, don't space them. If you do space them, space=100000 

[Link to py code]() [Runtime link to cipher](http://76.176.58.222:8080/binary)

[Link to html code]() [Runtime link to info](http://76.176.58.222:8080/BinaryInfo)

[Link to info page]()

### RSA (Made by Tri 1 students)
RSA is one of the first public-key cryptology and is widely used for secure data transmission. The acronym RSA is the initial letters of the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman, who publicly described the algorithm in 1977. A user of RSA creates and then publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers must be kept secret. More often, RSA passes encrypted shared keys for symmetric key cryptography which in turn can perform bulk encryption-decryption operations at much higher speed. It's a little similar to the Ceaser Cipher as well. The code has a few similarities too. This code does the decryption and encryption part of the project for RSA only. This code contains functions, loops, input/output, print statements, variables, arrays, and lists. It has a visual too. The html files also contains background pictures, html tags(<>), textbox, buttons, and runs its code from the main.py. 

[Link to py code]() [Runtime link to cipher](http://76.176.58.222:8080/rsa)

[Link to html code]() [Runtime link to info](http://76.176.58.222:8080/about-rsa)

[Link to info page]()

### Morse Code (Made by Adam)
Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes or dits and dahs. Morse code is named after Samuel Morse, an inventor of the telegraph. We decided to do only do the symbols as we could not figure out how to incorporate audio into the website. We were able to make both an encryption and decryption option for the morse code cipher and had a textbox for the user to input either english words or phrases, or morse code symbols.  We essentially made 2 lists, one with the english alphabet and one with the corresponding morse code symbols. Using different sections of code, we were able to iterate through each of the lists to determine whether the user's input was in morse code or english, and get the corresponding letters or symbols. Like all the other ciphers, we also provided an information page for the morse code cipher, with some background on how it came about, with some resources and an explanation of how the cipher generally works. 

[Link to py code]() [Runtime link to cipher](http://76.176.58.222:8080/Morsecode)

[Link to html code]() [Runtime link to info](http://76.176.58.222:8080/Morsecodeinfo)

[Link to info page]()

### Pig Latin (Made by Noah)
Pig Latin is a pretty basic language that involves a simple formula for translating words or phrases. To translate from English to Pig Latin, you are to remove everything before the first vowel of the word, moving it to the end, and adding an "ay" at the end of the word. An example of this would be "hello" turning into "ellohay". If the word begins with a vowel, then all you have to do is add "yay" to the end of the word. This means "apple" would turn into "appleyay". For the encryption of Pig Latin, it wasn't too hard. The way we approached it, was by first defining all the vowels. We then used for loops to loop through the word(s) listed by the user, to find the first vowel in each word. We used if and else statements to tell if the vowel was at the beginning, then "yay" would be added on to the end, otherwise everything before the first vowel, along with "ay" would go at the end. Decryption on the otherhand was found to be nearly impossible, as words could be the exactly the same in Pig Latin, but different in English. For example, the words smile and miles are the exact same in Pig Latin, being "ilesmay". The format of the Pig Latin cipher page and the info page are similar to the other ciphers, as it provides an encryption option on the cipher page, as well as some information about Pig Latin, some resources we used and how we coded it on the information page. 

[Link to py code]() [Runtime link to cipher](http://76.176.58.222:8080/PigLatin)

[Link to html code]() [Runtime link to info](http://76.176.58.222:8080/PigLatininfo)

[Link to info page]()

## Cipher Quiz and Database (Made by Nihar and Rivan)


[Link to py code]() [Runtime link to Cipher Quiz](http://76.176.58.222:8080/QuizGame) 

[Link to html code for Cipher Quiz]() [Runtime link to Database](http://76.176.58.222:8080/database)

[Link to javascript code for Database]() 

## Quote Encryptor (Made by Noah)


[Link to py code]() [Runtime link to Quote Encryptor](http://76.176.58.222:8080/api) 

[Link to html code]()

## Easter Egg (Made by Adam and Noah)


[Link to py code]() [Runtime link to Easter Egg](http://76.176.58.222:8080/easteregg)

[Link to html code]()

## College Board Requirements (Week 9)
1) Inputs: We are using user input, in which our website allows a user to input words or phrases into a textbox to then be encrypted by a cipher of their choosing

[Link to Inputs Code](https://github.com/NoahPidding/CollegeBoardProject/blob/116a644b9371889ce81f42b9f46a50e430650910/templates/PigLatin.html#L89)

2) Lists: We have lists for some cyphers such as morse code where it lists out the numbers and dots and dashes and runs through the list again and again until it fully encrypted or decrypted a message

[Link to Lists Code](https://github.com/NoahPidding/CollegeBoardProject/blob/116a644b9371889ce81f42b9f46a50e430650910/main.py#L256-L259)

3) Procedures: We are using procedures within our ciphers, in which we used the procedures we made to encrypt or decrypt the inputted messages by the user to then display a decrypted or encrypted result. 

[Link to Procedures Code](https://github.com/NoahPidding/CollegeBoardProject/blob/116a644b9371889ce81f42b9f46a50e430650910/templates/caesarcipher.html#L109-L122)

4) Algorithims: We are using algorithms within our ciphers, in which we used them to encrypt and decrypt the messages through code we coded ourselves. 

[Link to Algorithims Code](https://github.com/NoahPidding/CollegeBoardProject/blob/116a644b9371889ce81f42b9f46a50e430650910/main.py#L207-L238)

5) Outputs: We are using whatever message has been inputted into a cypher to output a encrypted or decrypted message

[Link to Outputs Code](https://github.com/NoahPidding/CollegeBoardProject/blob/116a644b9371889ce81f42b9f46a50e430650910/templates/PigLatin.html#L94-L97)

## Crossover Suggestions (Week 9)
1) Work on the styling of our navigation bar and make it more condensed and organized

[Link to Code](https://github.com/NoahPidding/CollegeBoardProject/blob/31a37b33af2ea91a9391848c33ededd641c16e7d/templates/home.html#L16-L43)

2) Change some of the pictures so that they are more visible with backgrounds

[Link to Code](https://github.com/NoahPidding/CollegeBoardProject/blob/31a37b33af2ea91a9391848c33ededd641c16e7d/templates/Morsecode.html#L82)

## Tickets (Week 9)
Noah: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801450)


Nihar: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801415)


Adam: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801482)


Rivan: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801434)

## Explanation of Tickets (Week 9)
### Noah: 
Noah's ticket for this week was to continue working on the API. Our plan for the API was to get quotes from a simple rapid api, then use our ciphers to encrypt the quotes and display the encrypted message below. Noah was able to successfully do this with both the Binary, Morse Code and Pig Latin ciphers, but is still working on getting the Caesar Ciphers to work (we are not going to be putting in RSA). Continuing to work on the API is going to be Noah's ticket for next week too. 

### Nihar:
Nihar's ticket was to finish up the user login system, in order to add more security to the database. Our database stores to scores for our Quiz Game, however it is viewable by everyone, so we want to make it more secure so only the user can see their own scores and results. 

### Adam:
Adam's ticket was to work on the organization and neatness of our navigation bar. Because there is beginning to be too many things on our nav bar, we wanted to condense it so that there aren't as many things. Adam worked on this by putting all the ciphers into one dropdown nav option, as well as all the info pages. 

### Rivan:
Rivan's ticket for this week was to work on the recommendations given to us by our crossover group, which they said that we needed to work on the styling of our website, which they pointed out that some of the images we had were not very visible due to the background image. Rivan also worked on adding a background image to the quiz game to make it more appealing. 


## Link to Code (Week 9)
### Noah's code:

[API work py](https://github.com/NoahPidding/CollegeBoardProject/blob/d591a6c151b29e88d0ff3e1525d8b7e65081a4ff/main.py#L322-L381)

[API work html](https://github.com/NoahPidding/CollegeBoardProject/blob/116a644b9371889ce81f42b9f46a50e430650910/templates/api.html#L52-L65)


### Nihar's code:


[Datbase Link/Show Questions](https://github.com/NoahPidding/CollegeBoardProject/blob/e564e38dda4f37546717fef3760d4f7d69f4ae6c/templates/database.html#L187-L200)

[User/Login Account](https://github.com/NoahPidding/CollegeBoardProject/blob/f3e59268d09ae64a501a7f4716bd14f62d5d76f3/templates/profile.html#L1-L69)

[Account Setup](https://github.com/NoahPidding/CollegeBoardProject/blob/8485b3dd0752022fb8f69fc06f430c3008ad0ec2/templates/security.html#L211-L219)

### Adam's code:


[Links to Nav Bar Changes](https://github.com/NoahPidding/CollegeBoardProject/blob/017c168c8c144ed94c3bc40d8fb923838d7892d1/templates/home.html#L16-L43)


### Rivan's code:

[Link to Quiz Game Background](https://github.com/NoahPidding/CollegeBoardProject/blob/fa47534b29d9f4bbdcbe6a4b9671b3df4bdc94ce/templates/QuizGame.html#L15-L19)

[Link to Morse Code Image](https://github.com/NoahPidding/CollegeBoardProject/blob/fa47534b29d9f4bbdcbe6a4b9671b3df4bdc94ce/templates/Morsecode.html#L11-L15)


## Grading (Week 7)
### Noah: 25/25
### Nihar: 25/25
### Adam: 24/25
### Rivan: 23/25


## Team Goals Completed (Week 7)
1) Get the API done, it's our first priority

2) Add a user login system to the database to make the site more secure

3) Make the Easter egg look good and add repsoitories, TPT corrections, and journals

4) Idea for API, get a simple rapid api (like quotes or jokes) and use the ciphers in our website to encrypt them

## Easter Egg
[Link to easter egg on website](http://76.176.58.222:8080/easteregg)

### Status: 
We created an additional HTML page with a separate navigation bar and have also added several buttons onto the navigation bar, including our journal, project plan and TPT corrections and reflections. We are prepared for the things that Mr M has ready for us for this separate area. 

[Link to Website](http://76.176.58.222:8080/)

## Tickets (Week 7)
Noah: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801450)


Nihar: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801415)


Adam: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801482)


Rivan: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801434)

## Explanation of Tickets (Week 7)
### Noah: 
Noah's ticket is to work on the api work. Our plan for this ticket, as our previous strategies had failed, it to take a simple rapid api such as quotes or jokes, and display it on the page from that api. After doing so, we plan to encrypt the message displayed from the api using the ciphers on our website, and display the encrypted message below. This way we can have the api related to our website.

### Nihar:
Nihar's ticket is to create a user login system, where the user can input their information and make the database more secure. Nihar will do this through the help of Mr M's example provided in class. 

### Adam:
Adam's ticket is working on the Easter Egg. We want to add in several buttons into the Easter Egg, such as things like our journal, project plan and TPT corrections and reflections. We also plan to add an about us page, with information about each of us, regarding both our general lives, as well as our progress over the months of coding we have had in this class. 

### Rivan:
Rivan's ticket is to work on a change we want to make in our database. We had the idea to link each question the user got wrong, which is displayed in the database, to the questions on the quiz, as the user would have to go through the quiz again in order to see the correct answers. 


## Link to Code (Week 7)
### Noah's code:

[API work py](https://github.com/NoahPidding/CollegeBoardProject/blob/4d434cf3959a07683fce08578ce919e03cdb2bc0/main.py#L321-L356)

[API work html](https://github.com/NoahPidding/CollegeBoardProject/blob/4d434cf3959a07683fce08578ce919e03cdb2bc0/templates/api.html#L1-L54)

Noah's ticket was to work on the api, as shown above with the explanation and links to tickets and proven in the code linked above. Noah used a rapid api for quotes and was able to diplay the quotes as well as encrypt the phrases in Pig Latin. This code includes both the python code and html code used to display the quotes and encrypt them. For now, we only have one cipher being used, however, we do plan to figure out a way to use more for future tickets. 

### Nihar's code:


[Datbase Link/Show Questions](https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/database.html#L183-L198)

[User/Login Account](https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/security.html#L1-L346)

Nihar's ticket is to create a user login system, where the user can input their information and make the database more secure. Nihar will do this through the help of Mr M's example provided in class.

### Adam's code:


[Links to Journals / Project Plan](https://github.com/NoahPidding/CollegeBoardProject/commit/fdd09d09442b9aab07748fe5d50042f6f7fbced4)

Adam's ticket had been to work on the easter egg as well as help with the API. Adam had put the links to the journals as well as the project plan for the Wildcats. One problem that Adam had faced was that he couldn't help much with developing the API of the website.

### Rivan's code:

[database questions](https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/database.html#L179-L198)

[User login](https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/security.html#L1-L346)

Rivan's ticket is to work on a change we want to make in our database. We had the idea to link each question the user got wrong, which is displayed in the database, to the questions on the quiz, as the user would have to go through the quiz again in order to see the correct answers.

## Team Goals Completed (Week 6)
1) Get the API done, it's our first priority

2) Add a user login system to the database to make the site more secure

3) Potentially add a new cipher and just make the website look better

4) Make the Easter egg look good and add repsoitories, corrections, and journals

## Easter Egg
[Link to easter egg on website](http://76.176.58.222:8080/easteregg)

[Link to Website](http://76.176.58.222:8080/)
## Tickets (Week 6)
Noah: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801450)


Nihar: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801415)


Rivan: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801434)


Adam: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-53801468)

## Explanation of Tickets (Week 6)
### Noah: 
Noah's ticket is mainly for finsihing the API. We are behind on the API and we are struggling on it and we need to get this API done or we'll keep loosing points.

### Nihar:
Nihar's ticket is about adding extra security to the database and also making the database more user friendly. Also to make the database better. Nihar is also expected to make the Easter egg better. 

### Rivan:
Rivan's ticket is the same as Nihar's as both Nihar and Rivan need to work together and make the database better and more secure. 

### Adam:
Adam's ticket is to work with Noah and finish the API. As told before we are behind on the API and we don't want to keep loosing points. Adam is also expected to make the site better. 

## Team Goals Completed (Week 4)
1) Added more buttons to navigation bar
2) Completed the Pig Latin cipher and information page
3) Completed the Morse code cipher and information page
4) Completed quiz game, including 10 questions and multiple options for answers on each question based on the different ciphers and their information pages
5) Added a databse (in progress)
6) We were able to successfully deploy it

## Tickets (Week 4)
Noah: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-52852206)

[Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-51521944)

Nihar: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-52849626)

[Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-52849559)

[Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-51521944)

Rivan: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-52849559)

[Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-51521911)

Adam: [Link to Ticket](https://github.com/NoahPidding/CollegeBoardProject/projects/1#card-52849626)

## Link to Code (Week 4)
### Noah's code:
Runs Pig Latin Cipher encryption
(main.py line 205 - 236)    

[Pig Latin](https://github.com/NoahPidding/CollegeBoardProject/blob/main/main.py#L205-L236)

With the code under this app route, located in the main.py file, I was able to run an encryption function on our website for Pig Latin, to translate a word or phrase from English to Pig Latin. I used python code I tested in REPL to implement it into the main.py file using POST in order to get it to work and running on the HTML page. 

### Nihar's code:
main.py lines (205-236), lines (248-301), the database.html file, the quizgame.html file, and the morsecode.html file. That was all the code I did. 

[Pig latin POST](https://github.com/NoahPidding/CollegeBoardProject/blob/main/main.py#L205-L236)

[Morsecode POST](https://github.com/NoahPidding/CollegeBoardProject/blob/main/main.py#L248-L301)

[QuizGame](https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/QuizGame.html#L1-L388)

[Database](https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/database.html#L1-L219)

[Morsecode](https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/Morsecode.html#L1-L103)


I added a database like table in the navigation bar and that was the database file. I did the POST stuff for morse code and Pig Latin, I then made all the questions and answers in the quizgame file. I was able to make a dictionary in Javascript and make it into an online quiz. With a submit button and a next/previous button. I will work on connecting that to the database and making the database function as currently I just added it only. The morsecode file is where I added the encrypt/decrypt buttons and used POST to give them their functions and allow them to encrypt and decrypt. I used Python, HTML, Javascript, CSS, and tried using SQLAlchemy but I was having trouble importing the functions and packages. The database still has a lot of work needed. 

### Adam's code:
main.py (Lines 248-301)

[Morsecode](https://github.com/NoahPidding/CollegeBoardProject/blob/main/main.py#L248-L301)

Adam coded the Python for Morse code for both the encryption and the decryption. Lines (248-301). His intellij wasn't working so he emailed his code and his work is commented "Adam's work for Morse code". Nihar did the POST work. 

### Rivan's code:
The quizgame file, the navigation bar

[Quizgame](https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/QuizGame.html#L1-L388)

[Navigation Bar](https://github.com/NoahPidding/CollegeBoardProject/blob/main/templates/home.html#L48-L68)

I worked with Nihar mainly and we both worked together on the quizgame file and made the questions and answers and were able to make a Javascript dictionary. I also added the buttons on the navigation bar and was able to aid Nihar with the database. We are currently figuring out how to make the database and the quizgame file work togther. We learned that we needed a lot of POST for this and that's our biggest challenge. 

My WIFI turns off at 11:00 so try to grade before that time. Thank you!
## Grading (Week 4)
### Noah 19/20
Noah completed his assignment of implementing the Pig Latin cipher as well as the information pages. He also helped with other parts of the website including some of the styling and format. Being the scrum master, Noah also monitored the scrum board, assigning scrum members to do different tasks and setting goals for the team to complete before the deadline. 

### Nihar 20/20
Nihar has done a lot for the team, as he is the most experienced coder out of us all. He has helped implement both ciphers into the project html pages using POST, while also creating the new quiz game, which included 10 questions and different options for the answers for each question. He also added the database which he is currently working on. He was also able to get the website deployed and running, and has proved very useful and helpful over the weeks, making several big and important commits to the project.  

### Adam 18/20
Adam was able to complete the code for the Morse code cipher in a REPL, however he could not get his Intellij to work, and as a result was unable to make any commits to the project. Because of this he was forced to email the code to others who did have Intellij up and running, and have them implement the code for him. 

### Rivan 18/20
Rivan was able to add more buttons onto the navigation bar we currently had, in which a Pig Latin, Morse code, quiz game and database buttons were added. He also helped a little bit with the addition of the quiz game, however Nihar was the main contributor on that assignment. 

