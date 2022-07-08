# Clean
Tool made for cleaning up unorganized folders more easily

Only os & sys modules included in python is used.

Instruction File: A file that will define the instructions of what to do with certain instructions. Different use cases will need different rules.
This is why the program is not hard coded to keep all jpegs in a pictures folder. Instead a user can define depending on what he wants to achieve
if a jpeg should go to a folder called Pictures or thumbnails or anything else he defines in this so called Instruction File.

It is a simple txt file and can be at any location. If it is in the same location of the cleanup directory the program will not ignore that file.
The program will however ignore the script file.

Instruction File syntax: Folder>EXT,EXT,EXT

One line = One rule
You can make as many rules as you need.

OTHERS FOLDER:
Others folder is the folder that all the files that do not fit into a rule defined in the instructions folder goes.

TODO FOR FUTURE:
1. Others folder name can be user defined
2. sorting files based on a file name (TV SHOWS)
3. ...
