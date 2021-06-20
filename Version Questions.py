        #Questions for Cites Quiz.
for q in citesquiz.keys():
        print(q) #Printing one question at a time in order.
        print(optlist[index]) #Print first option.
        index=index+1
        print("            ")
        
        user_ans=input("Enter your answer:")
        answer = citesquiz[q] # Finding answer to the question in the dictionary.

        if user_ans==answer:
            print("That is correct, Keep up the good work")
            print("---------------------")
            score=score+1
            print("Score",score+0)
        else:
            print("That is not correct. The answer is", answer)


             

            print("---------------------")
               
            print("Your score is",score,"out of 10 points")  #Presenting the scores to the users.
            print("Quiz Complete, WELL DONE :)")

            

    
if ready== "x" :  #If the user inputs x or no, when they are asked if they want to contiue the quiz or not.
    print("Consider playing later")
elif ready== "no":
    print ("Consider playing later ")
exit()
