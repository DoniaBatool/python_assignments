import pywhatkit
# kisi bhi number pe mesaage send kernay k liyae
pywhatkit.sendwhatmsg("+923180736608","Welcome to python",23,30,20)

#kisi wattsapp group pe message dend kernay k liyae
pywhatkit.sendwhatmsg_to_group("wattsapp_group_link","Welcome to python",23,30,20, True,5)

#To send message to a number instantly
pywhatkit.sendwhatmsg_instantly("+923180736608","Welcome to python",20)

#pywhatkit se google search bhi kersaktay hain through a keyword or in sentence 
# format i.e a regular search as we do on google browser
pywhatkit.search("python learning tutorials")


#pywhatkit se keyword k through youtube pe us keyword se related videos bhi search kersaktay hain 
pywhatkit.playonyt("simplilearn")