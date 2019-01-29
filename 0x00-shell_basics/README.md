# Shell Basics
How to use the shell. Covers basic commands and builtins, and how to use those to navigate the file system and manage files.

## Where Am I?
Determining your location on the file system using `pwd`.

## What's in There?
Listing names of non-hidden files in the working directory using `ls`.

## There Is No Place Like Home
Changing the working directory to the current user's home directory using `cd`.

## The Long Format
Listing the names of non-hidden files in the working directory and details about them using `ls` options.

## Hidden Files
Listing the names of all files in the working directory and details about them, again using `ls` options.

## I Love Numbers
Listing the names of all files in the working directory and details about them, this time with numeric user and group IDs. Once again this is done with `ls` options.

## Welcome Holberton
Creating a new directory using `mkdir`.

## Betty in Holberton
Moving a file from one directory to another using `mv`.

## Bye Bye Betty
Deleting a file from at a fixed path using `rm`.

## Bye Byte Holberton
Deleting a directory at a fixed path. This could use `rmdir` or `rm`, depending on whether we can assume the directory is empty. I'm guessing `rmdir`.

## Back to the Future
Changing the working directory to a previous one using an unusual option accepted by `cd`.

## Lists
Listing the files, including hidden ones and details, from multiple directories at once by giving multiple arguments to `ls`.

## File Type
Displaying the type of a file at a fixed path using `file`.

## We Are Symbols, and Inhabit Symbols
Creating a symbolic link to a file at a fixed path using `ln`.

## Copy HTML Files
Copy HTML files between directories using `rsync`, but only if they're newer in the source than in the destination.

## Let's Move
Move files from the working directory to the directory at a fixed location, only if those files' names start with an uppercase letter. This uses `mv` and special `bash` globs.

## Clean Emacs
Delete all files that look like `emacs` backup files using `rm`.

## Tree
Create 3 nested directories using minmal white space. This uses `mkdir` and `bash` substitutions.
This exact question appeared on the quiz during level 3 of the Holberton application.

## Life Is a Series of Commas, Not Periods
Listing the files in the working directory using a variety of `ls` options to achieve an unusual format.
