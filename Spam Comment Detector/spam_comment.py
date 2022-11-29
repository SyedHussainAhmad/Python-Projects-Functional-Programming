comment = input("Enter you comment\n")

if ("make a lot of money" in comment):
    spam = True
elif ("click this" in comment):
    spam = True
elif ("subscribe this" in comment):
    spam = True
elif ("buy now" in comment):
    spam = True
else:
    spam = False

if (spam):
    print("Your comment is spam Please use appropriate words")
else:
    print(comment)

