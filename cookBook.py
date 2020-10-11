import random, tkinter as tk

root = tk.Tk()
add =tk.Tk()
xnumberOfrecipe=tk.Entry(root)
addOtherRecipe=tk.Entry(add)
addPizzaRecipe=tk.Entry(add)
addChickenRecipe=tk.Entry(add)
addSoupRecipe=tk.Entry(add)
addBeefRecipe=tk.Entry(add)
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
         labellist.append(tk.Label(root,text=i))
    row=0
    for i in labellist:
        row+=1
        i.grid(row=row, column=1)


def xmealButtonCommand():

    try :
        if int(xnumberOfrecipe.get())>len(recipes):
            return len(recipes)
        else:return mealButtonCommand(int(xnumberOfrecipe.get()))
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
mealButton=tk.Button(root,text="get a random recipe", command=mealButtonCommand)
xMealButton=tk.Button(root,text="get any number of random recipe", command=xmealButtonCommand)
fiveMealButton=tk.Button(root,text="get 5 random recipes",command=fiveMealButtonCommand)
threeMealButton=tk.Button(root,text="get 3 recipes",command=threeMealButtonCommand)
#addRecipeWindowButton=tk.Button(root,text="add a new recipe",command=add.mainloop)

#add recipe buttons
addSoupButton=tk.Button(add,text="add a soup",command=addSoupCommand)
addpizzaButton=tk.Button(add,text="add a pizza",command=addPizzaCommand)
addChickemButton=tk.Button(add,text="add a Chicken recipe",command=addChickenCommand)
addBeefButton=tk.Button(add,text="add a beef recipe",command=addBeefCommand)
addRecipeButton=tk.Button(add,text="add a recipe",command=addRecipeCommand)

#labels

#Enterys
#def buildFrame():
   # root = tk.Tk()
root.title('cook book')
    #packList=[]

mealButton.grid(row=0)
threeMealButton.grid(row=1)
fiveMealButton.grid(row=2)
xMealButton.grid(row=3)
xnumberOfrecipe.grid(row=4)
#addRecipeWindowButton.grid(row=5)

addOtherRecipe.grid(row=0)
addRecipeButton.grid(row=0,column=1)
addPizzaRecipe.grid(row=1)
addpizzaButton.grid(row=1,column=1)
addBeefRecipe.grid(row=2)
addBeefButton.grid(row=2,column=1)
addChickenRecipe.grid(row=3)
addChickemButton.grid(row=3,column=1)
addSoupRecipe.grid(row=4)
addSoupButton.grid(row=4,column=1)

    # #packList.append(mealButton)
    # packList.append(fiveMealButton)
    # packList.append(threeMealButton)
    # packList.append(xMealButton)
    # packList.append(xnumberOfrecipe)
    # packList.append(addSoupButton)
    # packList.append(addSoupRecipe)
    # packList.append(addChickemButton)
    # packList.append(addChickenRecipe)
    # packList.append(addpizzaButton)
    # packList.append(addPizzaRecipe)
    # packList.append(addBeefButton)
    # packList.append(addBeefRecipe)
    # packList.append(addRecipeButton)
    # packList.append(addOtherRecipe)

    # for i in packList:i.pack()
root.mainloop()
soup=makeRecipeLists("soup.txt")
beef=makeRecipeLists("beef.txt")
other=makeRecipeLists("other.txt")
chicken=makeRecipeLists("chicken.txt")
pizza=makeRecipeLists("pizza.txt")
recipes= beef + other + chicken + pizza + soup



