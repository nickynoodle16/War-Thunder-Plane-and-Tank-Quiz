question1 = input("In War Thunder, which vehicle is not ampibious? a.LVT-A1, b. M163, c.BMP-1, d. none of the above :\n") 

  if question1 == "d":
   count = count + 1
   right = right + 1
   print("Great Job! You're a tanker!")

  else:
    print("Go back to boot camp, Beetle Bailey!")
    count = count + 1 
  
  question2 = input("Which Russian bomber is a reverse engineered copy of the B-29 Superfortress? a.B-50, b.Tu-4, c.B-18,d.Tu-22. :\n")
  
  if question2 == "b":
   print("Hooray! You're a Superfortress!")
   count = count + 1
   right = right + 1

  else:
   print("Go back to ground school, lieutenant!")
   count = count + 1

  question3 = input("What is the heaviest tank in War Thunder? a. E-100 b. Jagdpanzer E-100, c. Panzer Kampfwagen VIII Maus, d.T95 Super Heavy. :\n" ) 

  if question3 == "c":
    print("Great job! You really know your tanks!")
    count = count + 1
    right = right + 1
  
  else:
    print("OMG, commander! You can't tell a tank from a wheelbarrow!")
    count = count + 1
  
  question4 = input("What piston engined plane in War Thunder shot down a Mig-15 jet in 1952 during the Korean War? a.F4-U Corsair, b.F6F-5 Hellcat, c.P-47 Thunderbolt, d.P-51D Mustang. :\n")

  if question4 == "a":
    print("You're an ace pilot now!")
    count = count + 1
    right = right + 1
  
  else:
    print("Bail out of your plane pilot! You got that one wrong!")
    count = count + 1

  question5 = input("Which bomber is a flying boat? a.Boeing 314 Clipper, b.Pby Catalina, c.B-25 Mitchell, d.B-24 Liberator:\n")

  if question5 == "b":
    print("Fighter pilot! RAHHHHHHHHHHHH BOOOOOOOM BOOM! PEEWWWWWWWWW DIVE BOMB! Patrick!")
    count = count + 1
    right = right + 1
  else:
    print("(Crashes plane)")
    count = count + 1

  question6 = input("True or false: The Cobra King premium at a Battle Rating of 5.0, is another M4A3E2 Sherman Jumbo, but with historical camoflauge. a.True, b.False :\n")
  
  if question6 == "a":
    print("Great Job, tanker!")
    count = count + 1
    right = right + 1
  else:
    print("Even if you drove an M1 Abrams, you would lose a battle to an AI Vehicle")

  print("You've got", right, "out of 6 questions.")
  if right == 6:
     print("Congratulations. You are an ace warrior. See you in battle!")
  if right == 5:
    print("You are almost there. Review and take the quiz again and you'll be a war thunder master") 
  if right == 4:
    print("keep studying")
  if right < 4:
    print("Ummm. War gaming is not your thing. Go back to playing Tetris!") 
    
  break



