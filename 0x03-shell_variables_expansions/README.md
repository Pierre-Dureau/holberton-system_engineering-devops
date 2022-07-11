# 0x03. Shell, init files, variables and expansions

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
	What happens when you type $ ls -l *.txt
### Shell Initialization Files
	What are the /etc/profile file and the /etc/profile.d directory
	What is the ~/.bashrc file
### Variables
	What is the difference between a local and a global variable
	What is a reserved variable
	How to create, update and delete shell variables
	What are the roles of the following reserved variables: HOME, PATH, PS1
	What are special parameters
	What is the special parameter $??
### Expansions
	What is expansion and how to use them
	What is the difference between single and double quotes and how to use them properly
	How to do command substitution with $() and backticks
### Shell Arithmetic
	How to perform arithmetic operations with the shell
### The alias Command
	How to create an alias
	How to list aliases
	How to temporarily disable an alias
### Other help pages
	How to execute commands from a file in the current shell

## Tasks

### 0. \<o\>
Create a script that creates an alias.

### 1. Hello you
Create a script that prints hello user, where user is the current Linux user.

### 2. The path to success is to take massive, determined action
Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.

### 3. If the path be beautiful, let us not ask where it leads
Create a script that counts the number of directories in the PATH.

### 4. Global variables
Create a script that lists environment variables.

### 5. Local variables
Create a script that lists all local variables and environment variables, and functions.

### 6. Local variable
Create a script that creates a new local variable.

### 7. Global variable
Create a script that creates a new global variable.

### 8. Every addition to true knowledge is an addition to human power
Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.

### 9. Divide and rule
Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.

### 10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath
Write a script that displays the result of BREATH to the power LOVE

### 11. There are 10 types of people in the world -- Those who understand binary, and those who don't
Write a script that converts a number from base 2 to base 10.

### 12. Combination
Create a script that prints all possible combinations of two letters, except oo.

### 13. Floats
Write a script that prints a number with two decimal places, followed by a new line.

### 14. Decimal to Hexadecimal
Write a script that converts a number from base 10 to base 16.

### 16. Everyone is a proponent of strong encryption
Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.

### 15. What is the difference between a hard link and a symbolic link?
Write a blog post explaining what are hard and symbolic links on Linux, how to create them, and what is the difference between the two. Use examples to illustrate.

### 17. The eggs of the brood need to be an odd number
Write a script that prints every other line from the input, starting with the first line.

### 18. I'm an instant star. Just add water and stir.
Write a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.
