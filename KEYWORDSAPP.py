def findProduct(value):
    import csv
    import glob
    import os
    
    from tabulate import tabulate
    from operator import itemgetter
    burKeyWords = ["bur", "diamond"]
    sutureKeyWords = ["suture", "chromic", "polypropylene", "pga"]
    boneKeyWords = ["allograft", "bone", "cortical", "cancellous"]
    customKeyWords = []
    keywords = []
    list_of_files = glob.glob(r"C:\Users\GDS3\Downloads\*")
    latest_file = max(list_of_files, key=os.path.getctime)   
    if "globaldentalshop" or "vitality-product" in latest_file:
        try:
            with open(latest_file, mode='r') as csvfile:
                type = ""
                key1 = ""
                key2 = ""
                reader = csv.reader(csvfile)
                header = next(reader)
                # Column Numbers of the Moz Generated CSV Keyword Report
                keywordIndex = 0
                dateIndex = 9  
                currentRankIndex = 10
                positionChangeIndex = 11
                count = 0
                keys = []
                print("")
                if value == 3:
                    for i in range(len(sutureKeyWords)): 
                        keywords.append(sutureKeyWords[i])
                    type = "Suture "          
                elif value == 2:
                    for i in range(len(burKeyWords)): 
                        keywords.append(burKeyWords[i])
                    type = "Bur "          
                elif value == 1:
                    for i in range(len(boneKeyWords)): 
                        keywords.append(boneKeyWords[i])
                    type = "Bone "            
                elif value == 4:
                    while (True):
                        key1 = input("enter a keyword or 1 to exit: ")
                        if (key1 == ""):
                            print("invalid input try again")
                        elif (key1 == "1"):
                            break
                        else:
                            keywords.append(key1)
                    type = ""
                    for i in range(len(keywords)):
                        type += (keywords[i] + " ")      
                elif value == 5:    
                    
                    type = "All "  
                    date = next(reader)[9] # set date to last time crawled
                
                for row in reader:
                    if row[dateIndex] != date: # once the latest crawl date is parsed then break
                        newDate = row[dateIndex]
                        break    
                    for i in (range(len(keywords))):
                        if (keywords[i] in row[0].lower()): 
                            keyword = row[keywordIndex]
                            date = row[dateIndex]
                            curRank = row[currentRankIndex]
                            posChange = row[positionChangeIndex]   
                            try:
                                c = int(curRank)
                                p = int(posChange)
                                pr = c + p
                                values = [keyword, pr, c, p, date]
                            except ValueError:
                                continue                 
                            p = int(posChange)           
                            keys.append(values)
                            count+=1
                            break
                    if value == 5: 
                        keyword = row[keywordIndex]
                        date = row[dateIndex]
                        curRank = row[currentRankIndex]
                        posChange = row[positionChangeIndex]   
                        try:
                            c = int(curRank)
                            p = int(posChange)
                            pr = c + p
                            values = [keyword, pr, c, p,  date]
                        except ValueError:
                            continue                 
                        p = int(posChange)           
                        keys.append(values)
                        count+=1
                if len(keys) > 0:            
                    choice1 = input("Enter 1 to sort by Keyword Ranking\nEnter 2 to sort by Ranking Change: ")
                    headers=["Keyword", "Previous Ranking", "Current Google Rank", "7 Day Ranking Change Since:\n" + newDate, "Latest Crawl Date"]
                    print()
                    if choice1 == "1":
                        print(type + "Keyword Report")
                        keys.sort(key = lambda x: int(x[2]))           
                    elif choice1 == "2":
                        print(type + "Keyword Report")
                        keys.sort(key = lambda x: int(x[3]), reverse=True)       
                    print()             
                    print(tabulate(keys, headers, tablefmt="presto"))   
                    print("Keywords Found: " + str(count))    
                    keys.clear    
                else:
                    print("keyword not found")
        except FileNotFoundError:
            msg = "File is not found"   
            print(msg)   
        
    else:
        print("ERROR: Please run captureCSV.py first and make sure the Moz generated CSV is your latest download.")

  

while True:
    print("1 - Bone Keyword report")
    print("2 - Bur Keyword report")
    print("3 - Suture Keyword report")
    print("4 - Custom Keyword report")
    print("5 - All Keywords report")    
    print("6 - Fetch Latest Moz Keyword Report")   
    choice = input("enter your choice or 0 to exit: ")
    match choice:
        case "1":
            findProduct(1)
        case "2":
            findProduct(2)
        case "3":
            findProduct(3)
        case "4":
            findProduct(4)
        case "5":
            findProduct(5)
        case "6":
            print("")
            choice = input("Enter 1 for GDS\nEnter 2 for Vitality Product: ")
            if int(choice) == 1 or int(choice) == 2:            
                import captureCSV
                captureCSV.captureCSV_(int(choice))
            else:
                print("invalid choice")
        case "0":
            break