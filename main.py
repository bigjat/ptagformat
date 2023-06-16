def main():
    while True:
        filename = input("Enter the name of the file you wish to format, including the extension (ex: file.txt), or type 'Q' to quit. \n")
        newtext = ""
        if filename != "Q":
                with open(filename, "r") as file:
                    for line in file:
                        if line != "\n":
                            newtext += "<p>" + line[0:-1] + "</p>\n"
                    formatFileName = "FORMATTED" + filename
                    file.close
                    with open(formatFileName,"w") as newFile:
                        newFile.write(newtext)
                        newFile.close
        else:
            break
main()