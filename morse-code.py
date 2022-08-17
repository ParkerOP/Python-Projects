# THE MORSE CODE PROJECT


print("Hi there, User!")

userInput = input("Type a sentence to convert it into morse code :\n").lower()

lis = ["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] 

lis2 = ["!", "@", "#", "$", "^", "&", "*", "(", ")", "-", "_", "%", "[", "]", "{", "}", "\\", "|", ";", ":", ",", "<", ".", ">", "/", "?"]

for i in lis2 :
    if(i in userInput) :
        print("Only alphanumerical letters and spaces are allowed!")
        exit(1)
    else :
        pass

userInput = userInput.replace("a", "• —  ")             
userInput = userInput.replace("b", "— • • •  ")   
userInput = userInput.replace("c", "— • — •  ")   
userInput = userInput.replace("d", "— • •  ")      
userInput = userInput.replace("e", "•  ")
userInput = userInput.replace("f", "• • — •  ")       
userInput = userInput.replace("g", "— — •  ")
userInput = userInput.replace("h", "• • • •  ")        
userInput = userInput.replace("i", "• •  ")        
userInput = userInput.replace("j", "• — — —  ")        
userInput = userInput.replace("k", "— • —  ")        
userInput = userInput.replace("l", "• — • •  ")        
userInput = userInput.replace("m", "— —  ")        
userInput = userInput.replace("n", "— •  ")         
userInput = userInput.replace("o", "— — —  ")         
userInput = userInput.replace("p", "• — — •  ")       
userInput = userInput.replace("q", "— — • —  ")       
userInput = userInput.replace("r", "• — •  ")     
userInput = userInput.replace("s", "• • •  ")
userInput = userInput.replace("t", "—  ")
userInput = userInput.replace("u", "• • —  ")
userInput = userInput.replace("v", "• • • —  ")
userInput = userInput.replace("w", "• — —  ")
userInput = userInput.replace("x", "— • • —  ")
userInput = userInput.replace("y", "— • — —  ")
userInput = userInput.replace("z", "— — • •  ")
userInput = userInput.replace(" ", "    ")
userInput = userInput.replace("1", "• — — — —  ")
userInput = userInput.replace("2", "• • — — —  ")
userInput = userInput.replace("3", "• • • — —  ")
userInput = userInput.replace("4", "• • • • —  ")
userInput = userInput.replace("5", "• • • • •  ")
userInput = userInput.replace("6", "— • • • •  ")        
userInput = userInput.replace("7", "— — • • •  ")        
userInput = userInput.replace("8", "— — — • •  ")        
userInput = userInput.replace("9", "— — — — •  ")        
userInput = userInput.replace("0", "— — — — —  ")        

print(userInput)

