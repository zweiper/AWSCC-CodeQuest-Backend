sortList = []
namesList = []

def rewrite(sortList):
    with open('D:\Github\AWSCC-CodeQuest-Backend\submissions\challenges\day-11-challenge\studentList.txt', 'w') as file:
        file.writelines(sortList)
        file.close()

def sort():
    with open('D:\Github\AWSCC-CodeQuest-Backend\submissions\challenges\day-11-challenge\studentList.txt', 'r') as file:
        names = file.readlines()
        for line in names:
            namesList.append(line)
            sortList = sorted(namesList)
            rewrite(sortList)
        
sort()