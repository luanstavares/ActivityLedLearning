def treatOptions(option, selectedCase1, selectedCase2):
    while (option != "1" and option != "2"):
        option = str(input("Invalid option, only 1/2 is allowed "))
    if (option == "1"):
        return selectedCase1
    else:
        return selectedCase2


print("In the countryside of the Netherlands there was this little cottage where lived a coder known as Daan. His main activity was programming for a company called Nanosoft and despite his work title, he was not as nerdy as many people may think of him, as when he was not coding he usually played with his peculiar wild pet. This particular attachment to wild animals started when Daan was travelling abroad and faced himself with this rounded face with spotted and shiny skin with a long tail animal, a snake. The humble Dutch man fell in love with how the animal moves and its mysterious movements through... \n")

option1 = str(input(
    " 1. ...the terrain of the rainforest \n 2. ...a dark and damp cavern \n Select (1/2) "))
case1 = "...the terrain of the rainforest."
case2 = "...the dark and damp cavern."


print("\n", treatOptions(option1, case1, case2), "The animal sparked several ideas and enhanced the creative side of Daan in a way that he decided to take his new lucky charm back home. \nBack on Dutch soil, Daan decides to name the snake and ends up choosing to call it Guido. He then accommodates it in a glass wall cage with leaves, water, and with all the parameters of climate and temperature to satisfy the necessary comfort for the survival and well-being of his new pet.")

print("Guido itself was having the best treatment that a snake can have, his owner loved him and aways did the best to ensure his favourite pet and lucky charm was having all he needed to keep giving him great nights coding. One particular night though, Daan started struggling with those waterfalls of lines of code and had the weird feeling that maybe the snake was not a real lucky charm, maybe it was only a thing that he created in his mind. Disappointed, he then decides to go for a walk to keep his mind fresh for the next batch of code that would come. After seeing his owner disappointed, Guido tries to find a way to make him happy and in the darkness of a room, Guido crawling through his cage sees a little light coming out of Dann’s office.")


print("Guido, slipping his tail through the gaps to undo the latches, slithered out of his cage and through the office to try and see what Daan had been doing, climbing up his chair and onto the table, he tried to read the code. He wanted to understand it, perhaps Daan would be happy if Guido was able to help with it.\n\n")

option2 = str(input(
    "1. Guido is caught by Daan \n2. Guido isn't caught by Daan\n Select your choice: "))

case1 = "As he did this, Daan came back and was surprised to see that Guido had somehow escaped his cage, so he picked him up and brought Guido back to his cage.\n\nGuido wasn’t put off by this failure. The next night, he would try again, slithering out in the darkness. Heading straight to the pc, recalling what he had seen Daan do before, he used his tail to turn it on, and studied the code that Daan had written, code for a game called snake. Guido began to understand it, and spent the entire night testing the code, learning and even starting to make small improvements. Guido was so focussed that he almost didn’t notice the footsteps approaching the office, he rushed to turn the pc off and get back into the cage. This night was a success."

case2 = "As he did this, Guido heard Daan coming back, so he quickly turned off the pc and raced back to his cage.\n\nGuido was nearly caught, but he wasn't disheartened. The next night, he would try again, slithering out in the darkness. Heading straight to the pc, recalling what he had seen Daan do before, he used his tail to turn it on, and studied the code that Daan had written, code for a game called snake. Guido began to understand it, and spent the entire night testing the code, learning and even starting to make small improvements. Guido was so focussed that he almost didn’t notice the footsteps approaching the office, he rushed to turn the pc off and get back into the cage. This night was a success."

print(treatOptions(option2, case1, case2), "\n\nDaan didn’t seem to notice the small changes that Guido had made, so once again, Guido escaped, he tried to continue the code from where Daan had left it, writing new code rather than improving on what was already written. Daan had hit a wall in his code and couldn’t figure out how to program certain areas, such as detecting failure conditions and keeping the snake movements smooth. It was difficult but over a couple more nights, Guido was able to figure it out and completed areas of the code that Daan Wasn’t able to, However Guido wasn’t happy with the code, he felt like it was inefficient and over complicated and decided to try and figure out a way to change this.")

print("The following night Guido once again escaped from his cage, slithering through the table to get to the computer. Once he got to it, the snake re-read all the recent code that he and his owner had typed up together; he remembered every night after helping Daan how tired he would feel once getting back into his cage. 'I need a way to shorten everything down so it will be easier for me to code', Guido thought,as the tired snake continued coding, the lines he typed became shorter and shorter.")
print("\n Private void createAccBtn_Click(object sender, EventArgs e) \n { \n String username = userEnt.Text; \n String password = pass1Ent.Text;		 \n String confirmedPassword = pass2Ent.Text;			 \n If ((!string.IsNullOrEmpty(username)) &&  \n (!string.IsNullOrEmpty(password)) &&  \n (!string.IsNullOrEmpty(confirmedPassword)) \n {	 \n if(password == confirmedPassword)	 \n {		 \n FileStream fileStream = new  \n FileStream(@”F:\Daan\Game - Snake)		 \n StreamWrit... \n . \n . \n .	 \n Username = input(“ ”)	 \n Password = input(“ ”)	 \n Print(Username)	 \n Print(Password)")
print("The exhausted creature having stayed up all night in front of the computer was dragging his body towards his cage as fast as he could as he could hear his owner’s footsteps getting closer and closer.")

option3 = str(input(
    "1. Guido gets into his cage in time. \n 2. Guido gets stuck. \n Select choice: "))
case1 = "Guido just managed to pull his tail in but forgot to close the little gap he had created. The owner paid no mind to the gap as he thought he forgot to close it properly from the previous night."
case2 = "Guidio gets stuck in the gap he created when the escaped that night. Daan entered the room catching the snake in the act. 'You're always trying to go somewhere!', He chuckled as he helped his friend get back into the cage, thinking nothing of it "
print(treatOptions(option3, case1, case2), "\n\n After checking on his slithery companion, Daan went straight to his computer dreading to complete the rest of the code when to his surprise, the computer had been left open which he never does for security reasons. His confusion was mixed with excitement in the thought of this mystery coder helping him with his work again, when read through the program, he was amazed by this new way the game had been coded in the end. He immediately understood what had been coded and what he had to do to complete the last few lines.")

option4 = str(input(
    "1. While Daan was drinking his coffee  \n2.Guidou tried to tell Daan the reality  \n Select choice : "))

case1 = "Next night, the sky was clear, a few clouds moved slowly, he looked through his clear glass window, the coffee was prepared, just ready to drink, the man had a deep breath and his mind was full of ideas about that stranger that helped him to create the best ever code he has made, then suddenly the weather started to change, he opened the window, listening to the sound of sky, singing of birds coming from far away and the scratches of his garden animals. Daan has taken mouthful of his warm coffee, his cup of coffee looked like going to be cold, as he drinks it slowly always while thinking, a lot of thoughts came across, thinking about that stranger who had helped and supported making such an excellent code without leaving anything behind"
case2 = "Who could be that one, Daan asked in his mind, the situation was full of ideas and surprises for him as well as Guido went into a deep thought too, to find a way to tell his friend that he had made this code, but how can he sort out that a tiny little snake can make such a interesting game that will entertain millions of people, Guido said, then a sudden idea came to his mind, Guido thought to write a simple story with his new programming skills and leave it to Daan on his computer, but how can he open it? I should find an easy way, Guido said again, as night went to the middle and everything looked quiet and went to sleep, Guido moved slowly from his cage as he did all last night, but as Daan was awake, he could hear the noise that came out of his beloved snake, then Guido started to speak as human, Daan was full of fear and joy, for his lovely snake started to speak like a human"
print(treatOptions(option4, case1, case2), "\n\n it was a long conversation between two creatures one from human and the other from the animals, could you know what they say? Despite the amazing talk, Guido finally told his new friend that he created this incredible programming language and named it Python. Later on humans started to discover Python and improve it to develop software. Nowadays, Python is one of the most used programming languages and has been used by programmers of all ages.")
