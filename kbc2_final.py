import random
print("************************************WELOCOME TO KAUN BANEGA CROREPATI*********************")
Name = input("Enter Your Name: ")
def fiftyfifty(que):
    print("\nFifty-Fifty have been activated. Two Wrong Options have been removed")
    a = random.randint(1, 4) 
    while que[-1] == a: #a random number is generated between 1 and 4 till it is not equal to answer
        a = random.randint(1, 4)
    b = random.randint(1, 4)
    while que[-1] == b or b == a: #another random is generated between 1 and 4 till it is not equal to answer and the first number
        b = random.randint(1, 4)
    que[a] = "" #both the options are set as empty string
    que[b] = ""

def doubledip(que):
    print("\nDouble Dip have been activated. Now you can choose Two options")
    print(f"\nQ.{i+1}",que[0])
    print(f"\n1.{que[1]}\n2.{que[2]}\n3.{que[3]}\n4.{que[4]}")
    ans = input("\nEnter Your Answer: ")
    if ans == que[-1]: #if first answer is correct it is returned
        return ans
    else : #if the first answer is incorrect then u get another chance and it is returned as it is to check in the main function
        ans2 = input(f"\n{ans} is the incorrect answer you have one more chance: ")
        return ans2
    
def flipque(que):
    print("\nFlip the Question has been activated")
    print("\nChoose the topic for question\n1). Current Affair\t2).Science\n3).Sports\t4).Mythology\n")
    flipquestion = [["Recently, where was the 6th edition of International Conference on Disaster Resilient Infrastructure held?","New Delhi","Chennai","Hyderabad","Bengaluru",1],
                    ["Entomology is the science that studies","Behavior of human beings","Insects","The origin and history of technical and scientific terms","The formation of rocks",2],
                    ["Track and field star Carl Lewis won how many gold medals at the 1984 Olympic games?","Two","Three","Four","Eight",3],
                    ["According to Padma Purana, which king had to live as a tiger for a hundred years due to a deer's curse?","Kshemadhurti","Dharamdatta","Mitadhvaja","Prabhanjana",4]]
    top=int(input()) #input is taken so that flipped question can be choosen according to the topic
    if(top==1):
        return flipquestion[0]
    elif(top==2):
        return flipquestion[1]
    elif(top==3):
        return flipquestion[2]
    elif(top==4):
        return flipquestion[3]

def expertAdvice(que): #expert displays the answer
    print(f"\nExpert Advice has been activated. Expert says {que[-1]}")


#question list with options and correct answer
questions = [['Who invented the BALLPOINT PEN?', 'Biro Brothers', 'Waterman Brothers', 'Bicc Brothers', 'Write Brothers', 'None', 1,],
             ['In which decade was the first solid state integrated circuit demonstrated?','1950s','1960s','1970s','1980s','None',1,],
             ['Which scientist discovered the radioactive element radium','Isaac Newton','Albert Einstein','Benjamin Franklin','Marie Curie','None',4,],
             ['The absorption of ink by blotting paper involves:','viscosity of ink','capillary action phenomenon','diffusion of ink through the blotting','siphon action','None',2],
             ['Large transformers, when used for some time, become very hot and are cooled by circulating oil. The heating of the transformer is due to','the heating effect of current alone','hysteresis loss alone','both the heating effect of current and hysteresis loss','intense sunlight at noon','None',3],
             ['The most electronegative element among the following is','sodium','bromine','fluorine','oxygen','None',3],
             ['The names of the scientists, Newlands, Mendeleev, and Meyer are associated with the development of','atomic structure','metallurgy','periodic table of contents','discovery of elements','None',3],
             ['''The "http" you type at the beginning of any site's address stands for''','HTML Transfer Technology Process','Hyperspace Terms and Tech Protocol','Hyperspace Techniques & Tech Progress','Hyper Text Transfer Protocol','None',4],
             ['The main computer that stores the files that can be sent to computers that are networked together is...','Clip art','Mother board','Peripheral','File server','None',4],
             ['The first death anniversary day of Sri Rajiv Gandhi was observed as the','National Integration Day','Peace and Love Day','Secularism Day','Anti-Terrorism Day','None',4],
             ['Stethoscope was invented by ?','Bessemer','Rane Laennec','Henry Becquerel','None of these',2],
             ['Which former Indian President died as a result of a road accident','Rajendra Prasad','Faqruddin Ali Ahmed','Giani Zail Singh','R.Venkatraman',3],
             ["What is the name of India's First Solar powered ferry that operates between Vaikom and Thavanakadavu in Kerala",'Ayush','Aditya','Advait','Akshat',2],
             ["Who commanded the 'Hector', the first British trading ship to land at Surat",'Paul Canning','William Hawkins','Monkey D Luffy','Jack Sparrow',2],
             ["The fine step-well complex of 'Agrasen ki Baoli' is located at",'Gwalior','Amritsar','Agra','New Delhi',4],
             ["What is the unique to the naming of two elements in the preiodic table with the atomic numbers 96 and 109, respectively",'Named after Nobel laureates','Named after women scientists','Named after Indian Scientists','They are unnamed',2],
             ['First Woman to climb Mount Everest ','Miharu Fukushima','Junko Tabei','Joshi Tohan','Bachendri Pal',2],
             ['Which legendary baseball player holds the record for most career home runs in baseball','Babe Ruth','Jackie Robinson','Hank Aaron','Derek Jeter',1],
             ['For which movie did the legendary director Christopher Nolan win his first oscar for the best director','Oppenheimer','Interstellar','Bal Hanuman','He never won an Oscar',1],
             ['Who won the Candidates Chess Tournament 2024','Vidit Gujrathi','Hikaru Nakamura','Gukesh D','Magnus Carlsen',3]]

#winnings and money won
winnigs = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 700000000]
money = 0
#following variables control the lifelines
fifty = True
dip = True
flip = True
expert = True

for i in range(16): #loop is execuuted 16 times for 16 questions
    n = random.randint(0, len(questions) - 1)
    question = questions.pop(n) #a random question is popped out of the questions list

    print(f"\nQ.{i+1}",question[0])
    print(f"\n1.{question[1]}\n2.{question[2]}\n3.{question[3]}\n4.{question[4]}")

    ans = input("\nEnter your option or press Q to quit:\nOr press L for lifeline: ") #input your answer
    
    if ans.capitalize() == "Q":#if answer is equal to Q you quit and break the loop
        if i==0: 
            print("\nYou have quit the game")
            money = 0 #if you quit at first question you win 0 money
            break
        else:
            print("\nYou have quit the game")
            money = winnigs[i-1] #if you quit at any other question you win money won in previous question
            break

    if ans.capitalize() == "L": 

        print("\nChose From the following")
        life = int(input("\n1:Fifty-Fifty  2:Double Dip 3:Flip the Question 4:Expert Advice: ")) #choose the lifeline
        #life line only works if the lifeline variable is true and it is set to false after calling the lifeline
        #if the lineline variable is false then the code executes normally and asks for the answer
        if life == 1:
            if fifty == True:
                fiftyfifty(question)
                fifty = False       
                print(f"\nQ.{i+1}",question[0])
                print(f"\n1.{question[1]}\n2.{question[2]}\n3.{question[3]}\n4.{question[4]}")
                ans=input("Enter your option: ") #two wrong options are removed
            
            else:
                print("\nYou Don't Have this lifeline")
                ans=input("\nEnter your option: ")

        elif life == 2:
            if dip == True:
                ans = doubledip(question) #you get two chances to answer
                dip = False
            
            else:
                print("\nYou Don't Have this lifeline")
                ans = input("\nEnter your option: ")

        elif life == 3:
            if flip == True:
                question = flipque(question) #flipped question is returned and displayed
                flip = False
                print("\nYour Flipped Question is:",question[0])
                print(f"\n1.{question[1]}\n2.{question[2]}\n3.{question[3]}\n4.{question[4]}")
                ans = input("\nEnter your option: ")

            else:
                print("\nYou Don't Have this lifeline")
                ans = input("\nEnter your option: ")

        elif life == 4:
            if expert == True:
                expertAdvice(question) #expert helps in answering the question
                expert = False
                ans = input("\nEnter your option: ")

            else:
                print("\nYou Don't Have this lifeline")
                ans = input("\nEnter your option: ")

        else:
            print("\nNot a Valid Life line") #if you dont input between 1 and 4 code executes normally
            ans = input("\nEnter your option: ")

    if int(ans) == question[-1]:
        print(f"\nCorrect Answer! You won Rs.{winnigs[i]}") #you win money if answered correctly
        if i == 4:
            print("\nCongrats! You have crossed level 1 and have now secured Rs.10000") #when u cross a level you secure the winnig money there are 2 levels

            money=winnigs[i]
        elif i == 9:
            print("\nCongrats! You have crossed level 2 and have now secured Rs.320000")

            money=winnigs[i]
        elif i == 15:
            print("\nCongratulations! You are a Crorepati")
            money = winnigs[i] #when u answer all 16 questions correctly u win 7cr rupees
    else:
        print("\nWrong Answer! You lose")
        break # if u answer incorrectly the loop breaks and u win the money secured in the level crossed

print(f"\n{Name}:Your winning Amount is Rs.{money}") #winning amount is displayed