# nodejs reverse shell 3
`nodejssh3.py` is a scritp that creates a nodejs code that runs a reverse shell.
## Install dependencies
Actually, it needs only `python3` to run.
## Run the script
To run the script, you can either add the execute permission or run it with the `python3` command:

    chmod +x nodejssh3.py 
    ./nodejssh3.py
or

    python3 nodejssh3.py
## How and Why?
I was solving a ctf that runs a vulnerabile nodejs code. The thing that I needed to do is to craft a special nodejs function that will be runned by a function that does **not** sanitizes inputs. So, following some links and research, I found a Python 2 script that worked pretty well. But since I wanted to automate everything I can, I invested my time to recreate the script, add some functions and write it in Python 3 just... to let you know that ["Python 2.7 will not be maintained past 2020"](https://pythonclock.org/)

## "Render to Caesar  the things that are Caesar's"
This script is a modified type of the one that [Ajin Abraham](https://github.com/ajinabraham/Node.Js-Security-Course/blob/master/nodejsshell.py) (a Security Engineer) made in python 2. I've just added a few function that allows the script to be imported and used correctly in some ways and written in Python 3.

