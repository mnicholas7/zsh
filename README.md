# Zsh + Tmux turn-key env!

This repo assumes you are running Ubuntu , but also works with MacOS assuming you installed zsh + tmux on your own.  Everything is included to get a very nice environment up and running very quickly.

Here's what's included:
- zsh plug-ins + working .zshrc file to get you up and running fast!
- tmux plug-ins + working .tmux.conf file to get you up and running fast!
- vim plug-ins + working .vimrc file to get you up and running fast!
- .inputrc , .pythonrc , .editrc - all tweaked to give you the most authentic vim experience everywhere!
- A couple handy general purpose bash / perl / python functions, scripts
- Everything you need to spin up a python virtual environment with the included modules defined in requirements.txt

# Integrated zsh plug-ins:
-	[https://github.com/ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)
-	[https://github.com/zsh-users/zsh-syntax-highlighting.git](https://github.com/zsh-users/zsh-syntax-highlighting.git)
-	[https://github.com/zsh-users/zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
-	[https://github.com/softmoth/zsh-vim-mode.git](https://github.com/softmoth/zsh-vim-mode.git)
-	[https://github.com/romkatv/powerlevel10k.git](https://github.com/romkatv/powerlevel10k.git)

# This lf (as in "list files") tool is a terminal file manager written in Go:
- [https://github.com/gokcehan/lf/](https://github.com/gokcehan/lf/)
- The lfcd.sh script is also included in the repo and sourced in your .zshrc , this script runs lf but then changes your directory to the last directory you were in before you exited out of lf.
	- You can trigger this script and thus lf by pressing 'control + o'

# Tmux plug-ins:
- [https://github.com/wfxr/tmux-power.git](https://github.com/wfxr/tmux-power.git)  
- [https://github.com/tmux-plugins/tmux-sensible.git](https://github.com/tmux-plugins/tmux-sensible.git)

# Vim plug-ins:
- [https://github.com/tpope/vim-surround](https://github.com/tpope/vim-surround)
- [https://github.com/tpope/vim-repeat](https://github.com/tpope/vim-repeat)
- [https://github.com/tpope/vim-unimpaired](https://github.com/tpope/vim-unimpaired)



# ~/bin scripts:

- rmv_ctrl.pl
	- Removes control characters
- paragrep.pl
	- A multi-line type grep that uses blank lines as record separators, instead of newlines
- fg_cfg_splitter.pl
	- Splits fortigate configuration files into paragraphs to be searched with paragrep.pl
- clean_ctrl_chars.pl
	-	Another more elaborate control character remover
- pcap_summary.sh
	- Generates a text based output of the popular wireshark summary feature given a .pcap file
- pshell
	- A REPL ( read eval print loop ) for perl 

# ~/py scripts:
- MN_API.py
	- many handy general purpose functions
- rand.py
	- generate random strings of characters in very controlled ways
- CREDS.py
	- pull secrets into your scripts from the unix 'pass' utility


## Get started fast:
```
$ git clone https://github.com/mnicholas7/zsh.git                                                                                                                                                                                                                                                                                                ─╯ 
Cloning into 'zsh'...
remote: Enumerating objects: 144, done.
remote: Counting objects: 100% (144/144), done.
remote: Compressing objects: 100% (107/107), done.
remote: Total 144 (delta 66), reused 103 (delta 28), pack-reused 0
Receiving objects: 100% (144/144), 1.38 MiB | 4.01 MiB/s, done.
Resolving deltas: 100% (66/66), done.
$ 
```
```
$ ls
zsh
```
```
$ cd zsh
```
```
$ ls -la
total 3492
drwxrwxr-x 1 zoomer zoomer     512 Dec  5 22:18 .
drwxr-xr-x 1 zoomer zoomer     512 Dec  5 22:18 ..
-rw-rw-r-- 1 zoomer zoomer      29 Dec  5 22:18 .editrc
drwxrwxr-x 1 zoomer zoomer     512 Dec  5 22:18 .git
-rw-rw-r-- 1 zoomer zoomer      20 Dec  5 22:18 .gitignore        
-rw-rw-r-- 1 zoomer zoomer      20 Dec  5 22:18 .inputrc
-rw-rw-r-- 1 zoomer zoomer      71 Dec  5 22:18 .pythonrc
-rw-rw-r-- 1 zoomer zoomer    5948 Dec  5 22:18 .tmux.conf        
-rw-rw-r-- 1 zoomer zoomer    4763 Dec  5 22:18 .tmux.conf.basic  
drwxrwxr-x 1 zoomer zoomer     512 Dec  5 22:18 .vim
-rw-rw-r-- 1 zoomer zoomer     942 Dec  5 22:18 .vimrc
-rw-rw-r-- 1 zoomer zoomer    7220 Dec  5 22:18 .zshrc
-rw-rw-r-- 1 zoomer zoomer      63 Dec  5 22:18 README.md
drwxrwxr-x 1 zoomer zoomer     512 Dec  5 22:18 bin
-rw-rw-r-- 1 zoomer zoomer     279 Dec  5 22:18 deploy_venv.sh    
-rw-rw-r-- 1 zoomer zoomer 3409920 Dec  5 22:18 lf-linux-amd64.tar
-rwxrwxr-x 1 zoomer zoomer     707 Dec  5 22:18 lfcd.sh
-rw-rw-r-- 1 zoomer zoomer      17 Dec  5 22:18 lfrc
-rwxrwxr-x 1 zoomer zoomer    3177 Dec  5 22:18 pluginstall.sh    
drwxrwxr-x 1 zoomer zoomer     512 Dec  5 22:18 py
-rw-rw-r-- 1 zoomer zoomer     201 Dec  5 22:18 requirements.txt  
$
```
## Then just SOURCE this pluginstall.sh script:
### better to SOURCE it so you can be in either zsh or bash and you get mostly the same result!
```
$ source pluginstall.sh 
- already have CURL installed .. skip
- already have ZSH installed .. skip
- already have TMUX installed .. skip
The $ZSH folder already exists (/home/zoomer/.oh-my-zsh).
You'll need to remove it if you want to reinstall.
Cloning into '/home/zoomer/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting'...
remote: Enumerating objects: 7029, done.
remote: Counting objects: 100% (116/116), done.
remote: Compressing objects: 100% (61/61), done.
remote: Total 7029 (delta 57), reused 86 (delta 49), pack-reused 6913
Receiving objects: 100% (7029/7029), 1.52 MiB | 4.32 MiB/s, done.
Resolving deltas: 100% (4732/4732), done.
Cloning into '/home/zoomer/.oh-my-zsh/custom/plugins/zsh-autosuggestions'...
remote: Enumerating objects: 2435, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (39/39), done.
remote: Total 2435 (delta 22), reused 29 (delta 10), pack-reused 2385
Receiving objects: 100% (2435/2435), 564.00 KiB | 3.62 MiB/s, done.
Resolving deltas: 100% (1553/1553), done.
Cloning into '/home/zoomer/.oh-my-zsh/custom/plugins/zsh-vim-mode'...
remote: Enumerating objects: 314, done.
remote: Total 314 (delta 0), reused 0 (delta 0), pack-reused 314
Receiving objects: 100% (314/314), 99.35 KiB | 1.42 MiB/s, done.
Resolving deltas: 100% (168/168), done.
Cloning into '/home/zoomer/.oh-my-zsh/custom/themes/powerlevel10k'...
remote: Enumerating objects: 15879, done.
remote: Total 15879 (delta 0), reused 0 (delta 0), pack-reused 15879
Receiving objects: 100% (15879/15879), 73.00 MiB | 5.08 MiB/s, done.
Resolving deltas: 100% (10327/10327), done.
- already have lf installed .. skip
- already have lf etc dir .. skip
Cloning into '/home/zoomer/.tmux/plugins/tmux-sensible'...
remote: Enumerating objects: 193, done.
remote: Counting objects: 100% (24/24), done.
remote: Compressing objects: 100% (22/22), done.
remote: Total 193 (delta 12), reused 6 (delta 2), pack-reused 169
Receiving objects: 100% (193/193), 56.53 KiB | 2.17 MiB/s, done.
Resolving deltas: 100% (101/101), done.
Cloning into '/home/zoomer/.tmux/plugins/tmux-power'...
remote: Enumerating objects: 139, done.
remote: Counting objects: 100% (51/51), done.
remote: Compressing objects: 100% (30/30), done.
remote: Total 139 (delta 40), reused 24 (delta 21), pack-reused 88
Receiving objects: 100% (139/139), 27.49 KiB | 1.19 MiB/s, done.
Resolving deltas: 100% (54/54), done.
$ 
```
## Switch to your zsh if not already:
```
$ zsh
```
## You may see this screen at that point:
### If you do, just make the choices to set up your new prompt!
```
   This is Powerlevel10k configuration wizard. You are seeing it because you haven't  
  defined any Powerlevel10k configuration options. It will ask you a few questions and
                                 configure your prompt.

                    Does this look like a diamond (rotated square)?
                      reference: https://graphemica.com/%E2%97%86

                                     --->    <---

(y)  Yes.

(n)  No.

(q)  Quit and do nothing.

Choice [ynq]: 


```
## After that you can source your new ~/.zshrc
```
❯ . ~/.zshrc
❯
```

## If you want to change your shell to zsh:
```
which zsh
chsh -s /usr/bin/zsh
```
## Fire up tmux
### NOTE: It is highly recommended you re-map your caps-lock key to control, since control + q is the tmux escape sequence you need to hit everytime in order to get into 'tmux mode' where you can control tmux with the vi-like keybindings in the included .tmux.conf file!
```
tmux
```
## Be sure to review the .tmux.conf file:
```
# means CTRL q followed by k moves your cursor to pane above ( k goes up like vi )
bind-key -r      k select-pane -U

# means CTRL q followed by j moves your cursor to pane below ( j goes down like vi )
bind-key -r      j select-pane -D

# means CTRL q followed by h moves your cursor to pane left ( h goes left like vi )
bind-key -r      h select-pane -L

# means CTRL q followed by l moves your cursor to pane right ( l goes right like vi )
bind-key -r      l select-pane -R

# semicolon goes to previous window ( tab )
bind-key -r      \; last-window


# I use alt as Meta so when I hit CTRL q followed by CTRL k I resize in the direction you would expect ( vi like )
bind-key -r    M-k resize-pane -U 5
bind-key -r  M-j resize-pane -D 5
bind-key -r  M-h resize-pane -L 5
bind-key -r M-l resize-pane -R 5

# works same way even when I use CTRL
bind-key -r    C-k resize-pane -U
bind-key -r  C-j resize-pane -D
bind-key -r  C-h resize-pane -L
bind-key -r C-l resize-pane -R

```

## Next you can create a python virtual environment by sourcing this script:
```
❯ source deploy_venv.sh
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.8-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/home/zoomer/zsh/.venv/bin/python', '-Im', 'ensurepip', '--upgrade', '--default-pip']

~/zsh main ⇡                                                                                                 
❯
```

## You might need to install that package though first like this:
```
❯ sudo apt install python3.8-venv -y
[sudo] password for zoomer:
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
  python3.8-venv
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 5444 B of archives.
After this operation, 27.6 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 python3.8-venv amd64 3.8.10-0ubuntu1~20.04.5 [5444 B]
Fetched 5444 B in 0s (11.5 kB/s)
Selecting previously unselected package python3.8-venv.
dpkg: warning: files list file for package 'libc-bin' missing; assuming package has no files currently installed
(Reading database ... 73269 files and directories currently installed.)
Preparing to unpack .../python3.8-venv_3.8.10-0ubuntu1~20.04.5_amd64.deb ...
Unpacking python3.8-venv (3.8.10-0ubuntu1~20.04.5) ...
Setting up python3.8-venv (3.8.10-0ubuntu1~20.04.5) ...
```

## Then try again:
```
❯ source deploy_venv.sh
Requirement already satisfied: fire==0.4.0 in ./.venv/lib/python3.8/site-packages (from -r requirements.txt (line 1)) (0.4.0)
Requirement already satisfied: Jinja2==3.1.2 in ./.venv/lib/python3.8/site-packages (from -r requirements.txt (line 2)) (3.1.2) 
Requirement already satisfied: netaddr==0.8.0 in ./.venv/lib/python3.8/site-packages (from -r requirements.txt (line 3)) (0.8.0)
Requirement already satisfied: pexpect==4.8.0 in ./.venv/lib/python3.8/site-packages (from -r requirements.txt (line 4)) (4.8.0)   
Requirement already satisfied: pyjq==2.6.0 in ./.venv/lib/python3.8/site-packages (from -r requirements.txt (line 5)) (2.6.0)      
Requirement already satisfied: requests==2.28.1 in ./.venv/lib/python3.8/site-packages (from -r requirements.txt (line 6)) (2.28.1)
Requirement already satisfied: requests-oauthlib==1.3.1 in ./.venv/lib/python3.8/site-packages (from -r requirements.txt (line 7)) (1.3.1)
Requirement already satisfied: tabulate==0.9.0 in ./.venv/lib/python3.8/site-packages (from -r requirements.txt (line 8)) (0.9.0)
Requirement already satisfied: traceback-with-variables==2.0.4 in ./.venv/lib/python3.8/site-packages (from -r requirements.txt (line 9)) (2.0.4)
Requirement already satisfied: PyYAML==5.4.1 in ./.venv/lib/python3.8/site-packages (from -r requirements.txt (line 10)) (5.4.1)   
Requirement already satisfied: black==21.10b0 in ./.venv/lib/python3.8/site-packages (from -r requirements.txt (line 11)) (21.10b0)
Collecting pandas==1.5.1
  Using cached pandas-1.5.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.2 MB)
Requirement already satisfied: six in ./.venv/lib/python3.8/site-packages (from fire==0.4.0->-r requirements.txt (line 1)) (1.16.0)
Requirement already satisfied: termcolor in ./.venv/lib/python3.8/site-packages (from fire==0.4.0->-r requirements.txt (line 1)) (2.1.1)
Requirement already satisfied: MarkupSafe>=2.0 in ./.venv/lib/python3.8/site-packages (from Jinja2==3.1.2->-r requirements.txt (line 2)) (2.1.1)
Requirement already satisfied: ptyprocess>=0.5 in ./.venv/lib/python3.8/site-packages (from pexpect==4.8.0->-r requirements.txt (line 4)) (0.7.0)
Requirement already satisfied: charset-normalizer<3,>=2 in ./.venv/lib/python3.8/site-packages (from requests==2.28.1->-r requirements.txt (line 6)) (2.1.1)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in ./.venv/lib/python3.8/site-packages (from requests==2.28.1->-r requirements.txt (line 6)) (1.26.13)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.8/site-packages (from requests==2.28.1->-r requirements.txt (line 6)) (2022.9.24)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.8/site-packages (from requests==2.28.1->-r requirements.txt (line 6)) (3.4)
Requirement already satisfied: oauthlib>=3.0.0 in ./.venv/lib/python3.8/site-packages (from requests-oauthlib==1.3.1->-r requirements.txt (line 7)) (3.2.2)
Requirement already satisfied: regex>=2020.1.8 in ./.venv/lib/python3.8/site-packages (from black==21.10b0->-r requirements.txt (line 11)) (2022.10.31)
Requirement already satisfied: click>=7.1.2 in ./.venv/lib/python3.8/site-packages (from black==21.10b0->-r requirements.txt (line 11)) (8.1.3)
Requirement already satisfied: platformdirs>=2 in ./.venv/lib/python3.8/site-packages (from black==21.10b0->-r requirements.txt (line 11)) (2.5.4)
Requirement already satisfied: pathspec<1,>=0.9.0 in ./.venv/lib/python3.8/site-packages (from black==21.10b0->-r requirements.txt (line 11)) (0.10.2)
Requirement already satisfied: typing-extensions>=3.10.0.0 in ./.venv/lib/python3.8/site-packages (from black==21.10b0->-r requirements.txt (line 11)) (4.4.0)
Requirement already satisfied: tomli<2.0.0,>=0.2.6 in ./.venv/lib/python3.8/site-packages (from black==21.10b0->-r requirements.txt (line 11)) (1.2.3)
Requirement already satisfied: mypy-extensions>=0.4.3 in ./.venv/lib/python3.8/site-packages (from black==21.10b0->-r requirements.txt (line 11)) (0.4.3)
Requirement already satisfied: numpy>=1.20.3; python_version < "3.10" in ./.venv/lib/python3.8/site-packages (from pandas==1.5.1->-r requirements.txt (line 12)) (1.23.5)
Requirement already satisfied: python-dateutil>=2.8.1 in ./.venv/lib/python3.8/site-packages (from pandas==1.5.1->-r requirements.txt (line 12)) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in ./.venv/lib/python3.8/site-packages (from pandas==1.5.1->-r requirements.txt (line 12)) (2022.6)
Installing collected packages: pandas
Successfully installed pandas-1.5.1
```

## That will drop you in the virtual environment.
### Notice if you do 'pip3 list' you will likely see far fewer packages than you would if you were using your system's default installation:
```
❯ pip3 list | wc -l
36
```

## To exit the virtual environment, just type deactivate:
```
❯ deactivate
❯ pip3 list | wc -l
163
```

## So I've got about 160 python packages in my system default install and only 36 in my virtual environment,
- it's a good habit to _not_ modify the system's python packages, if possible
