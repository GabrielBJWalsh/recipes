import random, tkinter as tk
xnumberOfrecipe=tk.Entry()
addOtherRecipe=tk.Entry()
addPizzaRecipe=tk.Entry()
addChickenRecipe=tk.Entry()
addSoupRecipe=tk.Entry()
addBeefRecipe=tk.Entry()
def addRecipe(url, category="other"):
    file= open(category+".txt","a")
    file.write(url+","+"\n")
    file.close()

def makeRecipeLists(file):
    myFile=open(file,'r')
    recipe = myFile.read().split(',')
    myFile.close()
    return recipe

def randomMeal(recipe,mealCount=0):
    mealList=[]
    for i in range(mealCount):
        mealList.append( recipe[random.randint(0, len(recipe) - 1)])
    return mealList

def mealButtonCommand(number=1):
    if number =='':number=1
    labellist=[]
    for i in randomMeal(recipes, number):
         labellist.append(tk.Label(text=i))
    for i in labellist:i.pack()


def xmealButtonCommand():
    try :
        return mealButtonCommand(int(xnumberOfrecipe.get()))
    except:
        return mealButtonCommand()
def fiveMealButtonCommand(): return mealButtonCommand(5)
def threeMealButtonCommand(): return mealButtonCommand(3)
def addSoupCommand(): return addRecipe(addSoupRecipe.get(), "soup")
def addPizzaCommand(): return addRecipe(addPizzaRecipe.get(), "pizza")
def addChickenCommand(): return addRecipe(addChickenRecipe.get(), "chicken")
def addBeefCommand(): return addRecipe(addBeefRecipe.get(), "beef")
def addRecipeCommand(): return addRecipe(addOtherRecipe.get())

    #get Recipe buttons
mealButton=tk.Button(text="get a random recipe", command=mealButtonCommand)
xMealButton=tk.Button(text="get any number of random recipe", command=xmealButtonCommand)
fiveMealButton=tk.Button(text="get 5 random recipes",command=fiveMealButtonCommand)
threeMealButton=tk.Button(text="get 3 recipes",command=threeMealButtonCommand)

#add recipe buttons
addSoupButton=tk.Button(text="add a soup",command=addSoupCommand)
addpizzaButton=tk.Button(text="add a pizza",command=addPizzaCommand)
addChickemButton=tk.Button(text="add a Chicken recipe",command=addChickenCommand)
addBeefButton=tk.Button(text="add a beef recipe",command=addBeefCommand)
addRecipeButton=tk.Button(text="add a recipe",command=addRecipeCommand)

#labels
myLabel = tk.Label(text="Recipe Randomizer")
#Enterys
def buildFrame():
    root = tk.Tk()
    packList=[]
    packList.append(myLabel)
    packList.append(mealButton)
    packList.append(fiveMealButton)
    packList.append(threeMealButton)
    packList.append(xMealButton)
    packList.append(xnumberOfrecipe)
    packList.append(addSoupButton)
    packList.append(addSoupRecipe)
    packList.append(addChickemButton)
    packList.append(addChickenRecipe)
    packList.append(addpizzaButton)
    packList.append(addPizzaRecipe)
    packList.append(addBeefButton)
    packList.append(addBeefRecipe)
    packList.append(addRecipeButton)
    packList.append(addOtherRecipe)

    for i in packList:i.pack()
    root.mainloop()
soup=makeRecipeLists("soup.txt")
beef=makeRecipeLists("beef.txt")
other=makeRecipeLists("other.txt")
chicken=makeRecipeLists("chicken.txt")
pizza=makeRecipeLists("pizza.txt")
recipes= beef + other + chicken + pizza + soup



