# intro-to-python

## Prerequisites

This is intended for people who have never (or very rarely) used jupyterlab on the Analytical Platform (AP), or python, before. The only prerequisite is that you have followed the instructions [here](https://user-guidance.services.alpha.mojanalytics.xyz/github.html#jupyterlab) to allow you to clone this repository on the AP.

## Part 1: JupyterLab and the command line

### Command Line

To clone a github repository in JupyterLab, we need to use the command line/Terminal. To open the Terminal, click the `+` button in the top left and click on Terminal. You should see a command line prompt.

Before we clone the repository, it is worth knowing some basic command which will allow you to navigate you directories and files in JupyterLab. 

#### Task 1

Use the commands below to create a folder/directory called `training`. Inside this directory, create a file called `main.py`.

* `mkdir <directory_name>`: create a new directory/folder
* `cd <directory_name>`: navigate into a directory
* `touch <file_name>`: create a file
* `ls`: list files in a directory

#### Task 2

Let's practice moving and deleting files. Use the commands below to move the `main.py` file to your home directory. Navigate back to the home directory and then remove the `main.py` file. Note that `~` can be used to refer to your home directory, and `..` can be used to refer to a directory one step back/up from the one you are in.

* `rm <filename>`: delete file(s)
* `cp <filename> <new_location>`: copy a file from current location to a new one
* `mv <filename> <new_location>`: move a file from current location to a new one

#### Task 3

Clone this git repository! Using `cd`, navigate into the `training` directory you created. You can the clone this repository using `git clone git@github.com:moj-analytical-services/intro-to-python.git`. Navigate into your newly cloned repository. Create a new branch to work on, using the command `git checkout -b <your_branch_name>` (name the branch with your name or initials, or something unique!). We'll revisit some other git commands later in the training.



## Answers to Part 1

Add some answers later
