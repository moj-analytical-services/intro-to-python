# intro-to-python

This training is designed to be worked through in your own time. However, if you think you or your team may benefit from having someone on hand to help, then please contact George.Kelly1@justice.gov.uk via Slack, Teams or email to arrange a session.

If you have any comments or something you'd like to add/edit, feel free to [raise an issue](https://github.com/moj-analytical-services/intro-to-python/issues) or submit your own Pull Request!

## Prerequisites

This is intended for people who have never (or very rarely) used jupyterlab on the Analytical Platform (AP), or python, before. The only prerequisite is that you have followed the instructions [here](https://user-guidance.services.alpha.mojanalytics.xyz/github.html#jupyterlab) to allow you to clone this repository on the AP.

You'll then need to open JupyterLab via Control Panel, under Analytical Tools. Any version should work (go for the latest one if you aren't sure).

Throughout this training, there are some inline solutions to help you. You can see these by clicking on them.

## Part 1: JupyterLab and the command line

### Command Line

To clone a github repository in JupyterLab, we need to use the command line/Terminal. To open the Terminal, click the `+` button in the top left and click on Terminal. You should see a command line prompt.

Before we clone the repository, it is worth knowing some basic commands which will allow you to navigate your directories and files in JupyterLab. 

#### Task

Use the commands below to create a folder/directory called `training`. Inside this directory, create a file called `main.py`.

* `mkdir <directory_name>`: create a new directory/folder
* `cd <directory_name>`: navigate into a directory
* `touch <file_name>`: create a file
* `ls`: list files in a directory

<details>
  <summary><h4>Solution</h4></summary>
  
  ```bash
  mkdir training
  cd training
  touch main.py

  ```
</details>

#### Task

Let's practice moving and deleting files. Use the commands below to move the `main.py` file to your home directory. Navigate back to the home directory and then remove the `main.py` file. Note that `~` can be used to refer to your home directory, and `..` can be used to refer to a directory one step back/up from the one you are in.

* `rm <filename>`: delete file(s)
* `cp <filename> <new_location>`: copy a file from current location to a new one
* `mv <filename> <new_location>`: move a file from current location to a new one

<details>
  <summary><h4>Solution</h4></summary>
  
  ```bash
  mv main.py ~
  cd ~
  rm main.py
  ```
</details>

#### Task

Clone this git repository! Using `cd`, navigate into the `training` directory you created. You can clone this repository using `git clone git@github.com:moj-analytical-services/intro-to-python.git`. Navigate into your newly cloned repository. Create a new branch to work on, using the command `git checkout -b <your_branch_name>` (name the branch with your name or initials, or something unique!). We'll revisit some other git commands later in the training.

<details>
  <summary><h4>Solution</h4></summary>
  
  ```bash
  cd training
  git clone git@github.com:moj-analytical-services/intro-to-python.git
  cd intro-to-python
  git checkout -b my_branch
  ```
</details>

## Part 2: Installing and importing packages

Packages make your life easier when coding in python. You can use them to do things that would be very time consuming to do in base python, so it is worth understanding how to install them early on.

#### [Optional] Create a virtual environment

Virtual environments keep your projects separate, so you don't have clashes between package versions. For the purposes of this exercise, it isn't necessary, but you may want to read [this guidance](https://user-guidance.services.alpha.mojanalytics.xyz/tools/jupyterlab.html#using-a-virtual-environment-in-jupyter) on how to create them and use them in JupyterLab.

#### Task: Install the pandas package

Pandas is a data analysis package which you are likely to use a lot when coding in python. We use `pip` via the command line to install package using `pip install <package_name>`. Install pandas now.

<details>
  <summary><h4>Solution</h4></summary>
  
  ```bash
  pip install pandas
  ```
</details>

#### Task: Import the pandas package

In JupyterLab, go to the file navigator on the left of screen and click on `training` -> `intro-to-python` -> `intro-to-python.ipynb`. This should open a juptyer notebook with the rest of this training session's content.

