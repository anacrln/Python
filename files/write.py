file = open("main.txt", "a")
file.write("Writing new content to this file")

file = open("rewrite.txt", "w")#rewrite
file.write("Another content to a file")

file.close()

