if __name__ == "__main__":
    # Loop to input file name until user enters correct one.
    while(True):
        fname = input("Enter file name: ")
        try:
            file = open(fname)                
        except:
            print("File not found. Please Try Again...")
            continue
        break
    
    count = {} # --> Dictionary to store word and number of times it appeared.
    # Calculate How many times each word appear in the file.
    for line in file:
        words = line.split()
        for word in words:
            count[word] = count.get(word,0) + 1
        

    # Now calculate which word appears most
    bigword = None
    bigNumber = None

    for name,number in count.items():
        if bigNumber is None or number > bigNumber:
            bigNumber = number
            bigword = name
    # Now printing the final results.
    print(f"Most occuring word is {bigword} as it appears {bigNumber} times.")
    fname.close()