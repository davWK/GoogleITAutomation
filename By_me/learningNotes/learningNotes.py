to  open file in python
    variableName = open("filePath/filename")   ==> here file object is created and methode is used , like varableName.read, etc ..
    variableName.readline() allow to read one line a time in the file
    variableName.read() read from the current line to the end
    variableName.close()
    # you can work with file everywhere in the script

To avoid forget close file use :
    with open("filePath") as variableName:
        ...statement...
    # all work with file is restricted in this bloc

.stripe() : To remove all white space (tabs, etc)
.sort() : # we can sort line in a file

to write to a file open it with w argument or r+ 'overwrite actual content '
to add use 'a' argument
    variableName.write() write to a file

#get file informations
os.path.exists("filePath") //import os module before
os.path.getsize('file')
os.path.getmtime('file') : get time file was modified
    datetime.datetime.fromtimestamp(last_modfied) = convert into readable
    last_modfied.strftime("%Y-%m-%d")) covert into human readable

os.path.abspath('fie') : print the absolute path of a file
os.getcwd() <==> pwd
os.mkdir()
os.rmdir() :remove only empty dir
os.listdir('path') = ls
os.path.isdir() : verfy if is a dir
os.chdir <==> cd
os.path.join(dir, file ) return dir/file
os.rename('old', 'new')
os.remove('filePath')

// To create use write like above


//MANIPULATE CSV
import csv before
csv.reader() ==> parse a file content using csv module (read like csv based content)

//REGEX
import re module  before
 grep -i = to make search not case sensitive
 a dot (.) matches any character
 ^ indicate the beginning ===> grep ^pattern
 $ indicate the end ===> grep pattern$

 re.search(r"pattern", "the_word") ===> to store in a variable
  re.search(r"pattern", "the_word", re.IGNORECASE) ===> to ignore case sensitivity
