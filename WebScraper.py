from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys #for exiting
import os



def linkGrabber( pageUrl , linkList ): #Function that grabs links from specified url and puts them into a list
    page = urlopen(pageUrl)
    soup = BeautifulSoup(page, 'html.parser')

    for links in soup.find_all('a'):
        if links.get('href') is not None:
            linkList.append(links.get('href'))
    return;

def linkFormatter( linkList ):
    for i,links in enumerate(linkList):
        url = "http://www.uah.edu" + links
        linkList[i] = url
    
    return;

def infoGrabber( linkList ):
    college = str(input("Enter 2-3 letter college code for class(i.e. MA for math):"))
    for links in linkList:
        if links.find(college) != -1:
            print(links)
            page = urlopen(links)
            soup = BeautifulSoup(page, 'html.parser')
            for info in soup.find_all('a'):
                if info.pre.text is not None:
                    print(info.pre.text)
                
        
    return;


def MenuPrint():
    print("What semester would you like to view classes for? Hit q to exit")
    semesterList = ["Spring", "Summer", "Fall"]

    idx = 1
    for semester in semesterList:
        print ('{}. {}'.format(idx,semester))
        idx = idx + 1

#function to obtain semester choice
#Includes error handling on user input
def getSemester():

    validChoiceChosen = 0
    while validChoiceChosen==0:
        MenuPrint()
        userAns = input(">>> ")

        if userAns == 'q':
            print("\nGoodbye!\n")
            sys.exit()
        try:
            userAns = int(userAns)
        except ValueError:
            print("Not a Number, please enter a valid integer.\n")
            continue
        validChoice = [1,2,3]
        if userAns in validChoice:
            validChoiceChosen = 1
            break
        if userAns not in validChoice:
            print("Invalid Number, please enter a valid integer. \n")
            continue
    return userAns

def PrintHeader():

    #Clear terminal and print header
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the cgi-bin scraper. \n\n\n")


def main():

    PrintHeader()

    pageQuote = "https://www.uah.edu/cgi-bin/schedule.pl?"

    mainLinks = []
    springLinks = []
    summerLinks = []
    fallLinks = []

    linkGrabber( pageQuote , mainLinks)

    for links in mainLinks:
        
        if links.find('sprg') != -1:
            linkGrabber(links, springLinks)
            
        if links.find("sum") != -1:
            linkGrabber(links, summerLinks)

        if links.find("fall") != -1:
            linkGrabber(links, fallLinks)

    linkFormatter(springLinks)
    linkFormatter(summerLinks)
    linkFormatter(fallLinks)





    #Cue for input from user
    userAns = getSemester()


    if userAns == 1:
        infoGrabber(springLinks)
    elif userAns == 2:
        infoGrabber(summerLinks)
    elif userAns == 3:
        infoGrabber(fallLinks)
    else:
        print("You shouldn't see this")
        


if __name__=="__main__":
    main()