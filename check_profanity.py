import urllib

def read_text(file_name):
    contents = open(file_name)
    contents_of_file = contents.read()
    #print contents_of_file
    contents.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if output == "true":
        output = "YES! Get back at it."
    elif output == "false":
        output = "NONE I can find. Good job!"
    print "Does your file have any curse words? "+output
    connection.close()

users_file = raw_input("Enter the file name to check for profanity : ")
read_text(users_file)
