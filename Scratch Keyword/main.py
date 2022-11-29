import os

def detectWord(filename): 
    with open (item) as f:
        content = f.read()
        content = content.lower() # --> Converting in lower case alphabets as pyhton is a case sensitive language.
    if 'python developer' in content:
        return True
    else:
        return False

if __name__ == "__main__":
    directoryContent = os.listdir() # --> Creates list of all the directories

# Running detectWord function for each text file.
    filesList = []
    for item in directoryContent:
        if item.endswith('txt'):
            print(f'Detecting pyhton developer in {item}')
            find = detectWord(item)
            if find:
                print(f"Python Developer is found in {item}")
                filesList.append(item)
            else:
                print(f"Python Developer is not found in {item}")

# Summary how many files has been detected.
print('****Python Developer Detection Summary****')
print (f'Python Developers have been detected in {filesList} files.')