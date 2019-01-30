# Shell Permissions

## My Name Is Betty
Switching to another user ID using `su`.

## Who Am I
Displaying the name of the effective current user using `whoami`.

## Groups
Displaying the list of the current user's group memberships using `groups`.

## New Owner
Changing the user owner of a file with a fixed name using `chown`.

## Empty!
Creating an empty file with a fixed name using `touch`.

## Execute
Giving the owner of a file with a fixed name permission to execute it using `chmod`.

## Multiple Permissions
Giving various permissions to all ownership categories on a file with a fixed name, again using `chmod`.

## Everybody!
Giving everyone permission to execute a file with a fixed name, using `chmod` but without using any commas.

## James Bond
Set all permissions on a file with a fixed name to certain values, again using `chmod` but not commas.

## John Doe
Same as previous task, except permission which must be set are given in `chmod` symbolic form rather than written in English.

## Look in the Mirror
Set the permissions on one file to be the same as those on another file using `chmod`. Both files have fixed names.

## Directories
Recursively giving execute permission to the working directory, but only affecting directories. This uses a common `chmod` option and a rare symbolic permission.

## More Directories
Creating a directory with a fixed name and giving it certain permissions at the same time using `install`.

## Change Group
Changing just the owning group of a file with a fixed name using `chown`.

## Owner and Group
Changing both the owning group and owning user of all files and directories in the working directory using `chown`.
