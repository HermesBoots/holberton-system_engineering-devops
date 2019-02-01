# Shell Redirections

## Hello World
Printing the string "Hello, World" followed by a line feed to the terminal using `echo`.

## Confused Smiley
Printing a string full of special characters by carefully escaping them before letting `echo` process them.

## Let's Display a File
Displaying the entire contents of a file at a fixed path using `cat`.

## What about 2?
Displaying the entire contents of two files at once using `cat`.

## Last Lines of a File
Displaying only the last 10 lines of a file at a fixed path using `tail`.

## I'd Prefer the First Ones Actually
Displaying only the first 10 lines of a file at a fixed path using `head`.

## Line #2
Displaying only the third line of a file by piping `head` into `tail`.

## It Is a Good File That Cuts Iron without Making a Noise
Printing a specific string (followed by a line feed) into a file that needs to be heavily escaped in `bash`. Single quotes are very helpful for this.

## Save Current State of Directory
Redirecting the output of `ls` into a file, overwriting that file if it exists.

## Duplicate Last Line
Duplicating the last line in a file by using `tail` and append redirection.

## No More JavaScript
Recursively removing regular files that end with ".js" using `find` and `rm`.

## Don't Just Count Your Directories, Make Your Directories Count
Count the number of descendant directories of the working directory using `find`, `tail`, and `wc`.

## What's New
Displaying the 10 files with the most recent modification times in the current directory using `ls` and `head`.

## Being Unique Is Better Than Being Perfect
Taking a series of lines as input, sorting them, and displaying only the unique ones using `sort` and `uniq`.

## It Must Be in That File
Displaying lines from a file at a fixed path if they contain a given string using `grep`.

## Count That Word
Displaying the number of lines in a file that match a pattern using `grep` and `wc`.

## What's Next?
Displaying the lines from a file that match a pattern and the following 3 lines after each of them using `grep`.

## I Hate Bins
Displaying the lines from a file that _don't_ match a pattern using `grep`.

## Letters Only Please
Displaying the lines from a file that start with a letter using `grep` character classes and the beginning-of-line symbol.

## A to Z
Replacing certain characters from the input with others using `tr`.
