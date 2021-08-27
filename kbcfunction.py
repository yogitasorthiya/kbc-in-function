def kbc(question,options):    
    


    print()
    print("********WELCOME*********")
    print()
    print( "       🙏 🙏 🙏     ")
    print()
    print("QUIZE                🧠")
    print()

    i=0
    t=0
    t1=1
    lol=10000
    count=0
    solution = [3, 4, 1,2] 
    while i<len(question):
        print(question[i])
        j=0
        k=1

        while j<len(options):
            print(k,".",options[i][j])
            j+=1
            k+=1
        
        z=["3.seven","4.eight","2.bhopal","4.delhi","1.software engineering","2.conuseling","1.🟠","2. 🟧"]
        use=input("do you want life line,yes or no ")
        
        if use=="yes":
            print("50-50"," 💡 💡 💡")
            if count==0:
                print(z[i+t]) 
                print(z[i+t1])
                ans=int(input("enter a answer"))
                if solution[i]==ans:
                    print("right")
                    print( "👏 👏 👏")
                    print(("  CONGRATULATION  you Won🧑‍💼",lol))
                    count+=1
                else:
                    print("wrong,,game over"," 😝 😝 😝")
                    break
            else:
                print("you don't have life line")
                ans=int(input("enter answer"))
                if solution[i]==ans:
                    print("right")

                    print( "👏 👏 👏")
                    print("  CONGRATULATION  you Won🧑‍💼",lol)
                else:
                    print("wrong,,game over"," 😝 😝 😝")
                    break
            
        elif use=="no":
            user=int(input("enter a number"))
            if solution[i]==user:
                print("right")
                print( "👏 👏 👏")
                print(("  CONGRATULATION  you Won🧑‍💼",lol))
            else:
                print("game over"," 😝 😝 😝")
                break
        else:
            print("wrong")
        lol+=10000  
        t+=1
        t1+=1
        i+=1
        
deal=kbc(["How many continents are there?", "What is the capital of India?","NG mei kaun se course padhaya jaata hai?",
    "which is circle in these option?"], [["Four", "Nine", "Seven", "Eight"],
        ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
        ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
        [" 🟧 "," 🟠 "," 🔻"," 🔸"]
    ])
print(deal)
