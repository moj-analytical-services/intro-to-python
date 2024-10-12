# Part 1: JupyterLab and the command line

## Command Line

To clone a github repository in JupyterLab, we need to use the command line/Terminal. To open the Terminal, click the `+` button in the top left and click on Terminal. You should see a command line prompt.

Before we clone the repository, it is worth knowing some basic commands which will allow you to navigate your directories and files in JupyterLab. 

#### Task

Use the commands below to create a folder/directory called `training`. Inside this directory, create a file called `main.py`.

* `mkdir <directory_name>`: create a new directory/folder
* `cd <directory_name>`: navigate into a directory
* `touch <file_name>`: create a file
* `ls`: list files in a directory
* `pwd`: show the current directory

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

To delete a directory use the `-rf` option with the `rm` command. Be very careful with this!

```bash
rm -rf training
```

#### Task

Clone this git repository! You can clone this repository using `git clone git@github.com:moj-analytical-services/intro-to-python.git`<sup>1</sup>. Navigate into your newly cloned repository with the `cd` command. **Tip** Start typing the name of a file or directory and pressing the tab key will autocomplete the name.

Create a new branch to work on, using the command `git checkout -b <your_branch_name>` (name the branch with your name or initials, or something unique!). We'll revisit some other git commands later in the training.

1. Note: you may get a message when you clone the repo "The authenticity of host 'github.com (140.82.121.4)' can't be established. ECDSA key fingerprint is … Are you sure you want to continue connecting (yes/no/fingerprint)?’". This is normal, just type yes and hit return.

<details>
  <summary><h4>Solution</h4></summary>
  
```bash
git clone git@github.com:moj-analytical-services/intro-to-python.git
cd intro-to-python
git checkout -b my_branch
```
    
</details>

### Further reading

If you search for `bash` or `Linux command line` you can find tutorials giving more details about the terminal. The Analytical Platform uses Ubuntu Linux so a good place to start might be [their tutorial](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview).

## Optional: to save time use uv

If this course is time limited we can use [uv](https://docs.astral.sh/uv/) to speed things up so we don't spend half the course waiting for things to install. This is a tool that greatly speeds up Python packaging tasks but is not (yet?) the recommended way of doing things. The recommended way of doing things will also be described.

To install `uv` run
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
and
```bash
source $HOME/.cargo/env
```

## Using virtual environments

Virtual environments keep your projects separate, so you don't have clashes between package versions. You may want to refer to [this guidance](https://user-guidance.services.alpha.mojanalytics.xyz/tools/jupyterlab/#using-a-virtual-environment-in-jupyter) on how to create them and use them in JupyterLab. You will create virtual environments on the command line.

#### Task
To create a virtual environment, within your project directory type

```bash
uv venv venv
```
or
```bash
python -m venv venv
```

This can then be activated with
```bash
source venv/bin/activate
```

The virtual environment can be deactivated with the command
```bash
deactivate
```
but don't do that just yet. 

**Tip** If your `venv` is messed up you can remove it with `rm -rf venv` and start again.

## Packages

Packages make your life easier when coding in python. You can use them to do things that would be very time consuming to do in base python, so it is worth understanding how to install them early on.

Within this repo is an existing file `requirements.txt` which gives details on packages that should be installed so that everyone using the project is using the same environment.

#### Task
Install packages from the requirements file with
```bash
uv pip install -r requirements.txt
```
or
```bash
python -m pip install -r requirements.txt
```

#### Task: Install additional packages

The requirements file included `pandas`, a data analysis package which you are likely to use a lot when coding in python, and `matplotlib`, a graphing package. However to access files on the Analytical Platform we need an additional package, `s3fs`.

We use `pip` via the command line to install package using `(uv) pip install <package_name>`. Install `s3fs` now.

<details>
  <summary><h4>Solution</h4></summary>

```bash
uv pip install s3fs
```  
or 
```bash
pip install s3fs
```

</details>

## The Jupyter kernel

Now we have a virtual environment we have to let Jupyterlab know about it so we can use it in notebooks. To do this we need to install the `ipykernel` package.

#### Task: install ipykernel

Install `ipykernel` now.

<details>
  <summary><h4>Solution</h4></summary>

```bash
uv pip install ipykernel
```
or
```bash
pip install ipykernel
```

</details>


#### Task: register the kernel

We now need to install the kernel with `python -m ipykernel install --name "<short_project_name_without_spaces>" --display-name "<Longer name for display>" --user`. 

<details>
  <summary><h4>Solution</h4></summary>
  
```bash
python -m ipykernel install --name "intro-to-python" --display-name "Python training" --user
```

</details>

You can list your installed kernels with
```bash
jupyter kernelspec list
```

If you're not sure what environment they relate to you can check the `kernel.json` file in the listed directory using the `cat` command, which displays a file's contents. For example
```bash
cat /home/jovyan/.local/share/jupyter/kernels/intro-to-python/kernel.json
```
If any are no longer needed use `jupyter kernelspec uninstall <kernel name>`. 

## Protect your data with nbstripout

**IMPORTANT** Jupyterlab notebooks, unlike for example Rmarkdown or Quarto files, store their results by default. This means that if they're pushed to Github it can cause a security breach as they will be permanently in Github's history even if you remove them from your branch. You do not want this to happen as you'll have to [purge the file from Github's history and report a security incident](https://user-guidance.analytical-platform.service.justice.gov.uk/github/security-in-github.html#accidentally-publishing-data-to-github), neither of which are fun.

`nbstripout` automatically removes results from Jupyter notebooks and should be installed with
```bash
uv pip install nbstripout
```
or
```bash
pip install nbstripout
```

Then run 
```bash
nbstripout --install
```
and
```bash
nbstripout --install --attributes .gitattributes
```

## Record updated packages

Now we have more packages in our environment we can record them with `pip freeze`. Run
```bash
uv pip freeze > requirements.txt
```
or
```bash
pip freeze > requirements.txt
```

## More git commands

Now we have made changes to the packages and the git setup we will want to reflect them in our git branch.

`git status` will show which files have changed or added together with the current branch. `git add <file>` will add the file to the next commit, and `git commit -m "<commit message>"` will create the commit. `git push` then updates Github with the latest changes. The first time you push to a branch you will need to tell Github about it with `git push --set-upstream origin <branch name>`.

#### Task

Add, commit and push the changes to `requirements.txt` and `.gitattributes`.

<details>
  <summary><h4>Solution</h4></summary>
  
```bash
git add requirements.txt .gitattributes
git commit -m "Updated packages, installed nbstripout"
git push --set-upstream origin MY_BRANCH_NAME
```
    
</details>

### Further reading

There are [links to more information about git in the Analytical Platform user guidance](https://user-guidance.analytical-platform.service.justice.gov.uk/github/learning-resources.html).

Using `venv` and `pip` is the standard way to manage Python projects but is not the only option.
* [Poetry](https://python-poetry.org/) is widely used, particularly when developing packages such as [pydbtools](https://github.com/moj-analytical-services/pydbtools).
* [uv](https://docs.astral.sh/uv/) can be used as much more than just a replacement for the built in `pip` and `venv`
* There are many others... 

![Obligatory XKCD cartoon](https://imgs.xkcd.com/comics/python_environment.png)

In JupyterLab, go to the file navigator on the left of screen and click on `intro-to-python` -> `intro-to-python.ipynb`. This should open a jupyter notebook with the rest of this training session's content.

