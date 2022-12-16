# source this file instead of marking exec so you can be in zsh or bash and it still mostly works the same!

ME=$(whoami)
MYGRP=$(groups | awk '{print $1}')


# make sure we have curl first!
declare -a REQUIRE
REQUIRE=( "curl" "zsh" "ruby" "tmux" )

for i in ${REQUIRE[@]}; do
  echo "checking for: $i ..."
  ITEM=$(which $i)
  if [[ -e $ITEM ]]; then
    echo " - already installed $i , skip .."
  else
    sudo apt install $i -y
  fi
done

# not gonna test for these just run 'em KISS 
sudo apt install ruby-dev ruby-colorize -y
sudo gem install colorls

# install oh-my-zsh plugin mgr
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# clone some zsh plugs
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

git clone https://github.com/zsh-users/zsh-autosuggestions \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/softmoth/zsh-vim-mode.git \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-vim-mode

# git clone https://github.com/romkatv/powerlevel10k.git \
#     ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k



# do we have lf already ?
LF=$(which lf)
if [[ -e $LF ]]
then
  echo "- already have lf installed .. skip"
else
  # I love this lf tool
  #wget https://github.com/gokcehan/lf/releases/download/r27/lf-linux-amd64.tar.gz
  gunzip ./lf-linux-amd64.tar.gz
  tar -xvf lf-linux-amd64.tar
  sudo mv lf /usr/local/bin/
fi

if [[ -d /etc/lf ]]
then
  echo "- already have lf etc dir .. skip"
else
  # create global /etc dir for lf
  sudo mkdir /etc/lf
  #
  # we source this file in our .zshrc so we can triger the lfcd function with ctrl o
  sudo cp ./lfcd.sh /usr/local/bin/lfcd.sh
fi

declare -a REQ_DIRS
REQ_DIRS=( "bin" "py" "jq" "aws" "jinja" "PRIVREPOS" "PUBREPOS" )

for i in ${REQ_DIRS[@]}; do
  echo "checking if dir exists: $i ..."
  if [[ -e ${HOME}/$i ]]; then
    echo " - dir exists $i , skip .."
  else
    mkdir ${HOME}/$i 
  fi
done


# move our standard .rc's into place
cp .zshrc ~/ && chown ${ME}:${MYGRP} ~/.zshrc
cp .vimrc ~/ && chown ${ME}:${MYGRP} ~/.vimrc
cp .bashmn ~/ && chown ${ME}:${MYGRP} ~/.bashmn
cp .ctags ~/ && chown ${ME}:${MYGRP} ~/.ctags

cp .alias ~/ && chown ${ME}:${MYGRP} ~/.alias
cp .func  ~/ && chown ${ME}:${MYGRP} ~/.func
cp .var   ~/ && chown ${ME}:${MYGRP} ~/.var

if [[ -d ~/PRIVREPOS/zsh ]]; then
  cp ~/PRIVREPOS/zsh/.aliaspriv ~/ && chown ${ME}:${MYGRP} ~/.aliaspriv
  cp ~/PRIVREPOS/zsh/.funcpriv  ~/ && chown ${ME}:${MYGRP} ~/.funcpriv
  cp ~/PRIVREPOS/zsh/.varpriv   ~/ && chown ${ME}:${MYGRP} ~/.varpriv
  cp ~/PRIVREPOS/zsh/m          ~/ && chown ${ME}:${MYGRP} ~/m
fi


cp .inputrc ~/ && chown ${ME}:${MYGRP} ~/.inputrc
cp .pythonrc ~/ && chown ${ME}:${MYGRP} ~/.pythonrc
cp .editrc ~/ && chown ${ME}:${MYGRP} ~/.editrc
cp .tmux.conf ~/ && chown ${ME}:${MYGRP} ~/.tmux.conf
cp bin/* ~/bin/ && chown ${ME}:${MYGRP} ~/bin/*
cp py/* ~/py/ && chown ${ME}:${MYGRP} ~/py/*

# move our standard vim plug dir's into place
cp -r .vim ~/ && chown -R ${ME}:${MYGRP} ~/.vim

# mkdir .tmux plugin dir exists
mkdir -p ~/.tmux/plugins/

# tmux sensible
git clone https://github.com/tmux-plugins/tmux-sensible.git \
    ${TMUX_CUSTOM:-~/.tmux/plugins}/tmux-sensible

# manual tmux-power plug-in add ( mac os don't work well w/ tpm )
git clone https://github.com/wfxr/tmux-power.git \
    ${TMUX_CUSTOM:-~/.tmux/plugins}/tmux-power


# if we are inside WSL, copy some files to our PS home dir
if [[ -e  /mnt/c/windows/system32/cmd.exe ]]
then
  WINDOZE_USER=$( /mnt/c/windows/system32/cmd.exe /c "echo %USERNAME%" | perl -wpl -e "s/\s+//g;")
   
  MSHOME=/mnt/c/Users/${WINDOZE_USER}

  if [[ -d ${MSHOME} ]]
  then
    cp .vimrc ${MSHOME}/_vimrc
    cp profile.ps1 ${MSHOME}/Documents/WindowsPowerShell/
  fi
fi


source ~/.alias
source ~/.func
source ~/.var
source ~/.aliaspriv
source ~/.funcpriv
source ~/.varpriv

# CURL=$(which curl)
# if [[ -e $CURL ]]
# then
#   echo "- already have CURL installed .. skip"
# else
#   sudo apt install curl -y
# fi
#
#
###  Bash tweak to append instead of overwrite existing
#  └─[$] <git:(main*)> grep 'rAK0JBaJtWkgV0' .bashmn
#  rAK0JBaJtWkgV0
#  ┌─[nicholas@DESKTOP-ST9966E] - [~/PUBREPOS/zsh] - [Thu Dec 15, 15:58]
#  └─[$] <git:(main*)> YES=$(grep 'rAK0JBaJtWkgV0' .bashmn)
#  ┌─[nicholas@DESKTOP-ST9966E] - [~/PUBREPOS/zsh] - [Thu Dec 15, 15:58]
#  └─[$] <git:(main*)> if YES:
#   > then
#   >   echo 'yup'
#   > fi
#  zsh: command not found: YES:
#  ┌─[nicholas@DESKTOP-ST9966E] - [~/PUBREPOS/zsh] - [Thu Dec 15, 15:58]
#  └─[$] <git:(main*)>                                                                                                               <<<
#  

# Check whether we've appended here already before doing it again ,.. and AGAIN ...., and AGAIN ....
YES=$(grep 'rAK0JBaJtWkgV0' ~/.bashrc)
if [[ -e $YES ]]
then
  echo "- already appended to ~/.bashrc previously .. skip"
  echo "  - if you'd like to refresh your .bashrc , remove the last line containing: rAK0JBaJtWkgV0 !"
else
  cat ~/.bashmn >> ~/.bashrc
fi

TEST=$( echo $SHELL | awk -F/ '{print $NF}' )
if [[ $TEST == zsh ]]; then
  echo ".. sourcing .zshrc "
  source ~/.zshrc
elif [[ $TEST == bash ]]; then
  echo ".. sourcing .bashrc "
  source ~/.bashrc
else
  echo ".. couldn't determine your shell so not sourcing any .bashrc or .zshrc "
fi


# save for last
# fuzzy finder
git clone --depth 1 https://github.com/junegunn/fzf.git ~/PUBREPOS/fzf

#
# install fzf
~/PUBREPOS/fzf/install



