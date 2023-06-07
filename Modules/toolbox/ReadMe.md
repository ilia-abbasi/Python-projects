toolbox v1.0.0  Windows
Developer: Ilia Abbasi
-----------------------------------


Documentation:

save_file()
 - It save some contents in a file with an options.
 - This function recieves everything that a open() function needs.
 - It has an extra argument named "smart" as a boolean with the default value of False.
 - If "smart" is True then the function will not overwrite previously existing files with the same name.
 - An integer will be added recursively at the end of the file name to find an empty spot.

raw_or_file()
 - It recieves the argument "s".
 - If "s" exists as a file, return the contents of it. If not then return "s" itself.
 - This function can be used when you want to give user the option to either enter a value or the file name that contains that value.

handle_answer()
 - This function is used when you want to handle the answer of user for a prompt.
 - "options" is the list of expected answers.
 - "case_sensitive" indicates whether the answer should be case sensitive or not. False as default.
 - "one_char" indicate whether the answer can have 1 character only or not. True as default.
 - "default" is the default answer, if user entered nothing. If left empty and user also didn't enter anything, then the function will throw an error.

own_file_name()
 - Returns the name of the current file which is running.

cwd()
 - Returns current working directory.

path_splitter()
 - Returns the splitter character for paths based on the OS. \ for windows and / for linux.

roaming_appdata()
 - Returns the roaming appdata path.

local_appdata()
 - Returns the local appdata path.

get_cmd_result()
 - Returns the result of the given command and doesn't print anything to stdout.
 - If you had a faster solution, please make a pull request.
