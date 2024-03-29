#!/bin/bash
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
REQ_DIRS=( "bin" "py" "jq" "aws" "jinja" "lua" "go" "PRIVREPOS" "PUBREPOS" )

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

if [[ -d ~/PRIVREPOS/zsh.priv ]]; then
  cp ~/PRIVREPOS/zsh.priv/.aliaspriv ~/ && chown ${ME}:${MYGRP} ~/.aliaspriv  &> /dev/null
  cp ~/PRIVREPOS/zsh.priv/.funcpriv  ~/ && chown ${ME}:${MYGRP} ~/.funcpriv  &> /dev/null
  cp ~/PRIVREPOS/zsh.priv/.varpriv   ~/ && chown ${ME}:${MYGRP} ~/.varpriv  &> /dev/null
  cp ~/PRIVREPOS/zsh.priv/m          ~/ && chown ${ME}:${MYGRP} ~/m        &> /dev/null
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
  NVIM_INIT=/mnt/c/Users/${WINDOZE_USER}/AppData/Local/nvim

  if [[ -d ${MSHOME} ]]
  then
    cp .vimrc ${MSHOME}/_vimrc
    cp profile.ps1 ${MSHOME}/Documents/WindowsPowerShell/
  fi

  # nvim init file location on windoze
  if [[ -d ${NVIM_INIT} ]]
  then
    cp init.vim ${NVIM_INIT}/
  fi
fi


# CURL=$(which curl)
# if [[ -e $CURL ]]
# then
#   echo "- already have CURL installed .. skip"
# else
#   sudo apt install curl -y
# fi
#
#
#  

# Check whether we've appended here already before doing it again ,.. and AGAIN ...., and AGAIN ....

if [[ -e ~/.bashrc ]]; then
  YESA=$(grep 'rAK0JBaJtWkgV0' ~/.bashrc)
elif [[ -e ~/.bash_profile ]]; then
  YESB=$(grep 'rAK0JBaJtWkgV0' ~/.bash_profile)
fi

if [[ -n $YESA ]]
then
  echo "- already appended to ~/.bashrc previously .. skip"
  echo "  - if you'd like to refresh your .bashrc , remove the last line containing: rAK0JBaJtWkgV0 !"
else
  cat ~/.bashmn >> ~/.bashrc
fi
if [[ -n $YESB ]]
then
  echo "- already appended to ~/.bash_profile previously .. skip"
  echo "  - if you'd like to refresh your .bashrc , remove the last line containing: rAK0JBaJtWkgV0 !"
else
  cat ~/.bashmn >> ~/.bash_profile
fi

TEST=$( echo $SHELL | awk -F/ '{print $NF}' )
if [[ $TEST == zsh ]]; then
  echo ".. not auto sourcing .zshrc "
  # source ~/.zshrc
elif [[ $TEST == bash ]]; then
  echo ".. sourcing .bashrc "
  source ~/.bashrc
else
  echo ".. couldn't determine your shell so not sourcing any .bashrc or .zshrc "
fi

FZF=$( which fzf | awk -F/ '{print $NF}' )
if [[ $FZF ==  fzf ]]; then
  echo ".. fzf already intstalled.. skip"
else
  echo ".. installing fzf , get ready .."
  git clone --depth 1 https://github.com/junegunn/fzf.git ~/PUBREPOS/fzf
  ~/PUBREPOS/fzf/install
fi

UNAME=$(uname)
case $UNAME in
  Darwin)
    echo "Think Different"
    # sudo port install ruby-devel -y

    # REQS=( "colorls" "colorize" )
    # GEMS=($(sudo gem list | awk '{print $1}'))

    # declare -a RESULT

    # for req in ${REQS[@]}; do
    #   for mineral in ${GEMS[@]}; do
    #     if [[ $req == $mineral ]]; then
    #       RESULT+=( "$req" )
    #     fi
    #   done
    # done

    # if [[ ${#RESULT[@]} == 2 ]]; then
    #   echo "looks like we got the diamonds ..◇ ◇ ◇◇◇  "
    # else
    #   sudo gem install colorls
    #   git clone https://github.com/fazibear/colorize.git ~/PUBREPOS/colorize

    #   cd ~/PUBREPOS/colorize
    #   sudo gem build colorize.gemspec
    #   sudo gem install colorize*.gem
    #   cd ~/PUBREPOS/zsh
    # fi
    ;;
  Linux)
    echo "Ah, I see you like penguins ..."
    # colorls too slow! use lsd instead!
    # sudo apt install ruby-dev ruby-colorize -y
    # sudo gem install colorls

    # try lsd, colorls very slow

    if [[ ! -d ~/PUBREPOS/lsd ]]; then

        mkdir ~/PUBREPOS/lsd
        wget https://github.com/Peltoche/lsd/releases/download/0.23.1/lsd_0.23.1_amd64.deb -P ~/PUBREPOS/lsd/
        sudo dpkg -i ~/PUBREPOS/lsd/lsd_0.23.1_amd64.deb 
    fi

    # yanking from nvim to sys clip req's this
    XSEL=$( which xsel | awk -F/ '{print $NF}' )
    if [[ $XSEL ==  xsel ]]; then
      echo ".. xsel already intstalled.. skip"
    else
      echo ".. installing xsel , get ready .."
      sudo aptitude install xsel -y
    fi

    # copy neovim lua config files over
    if [[ -e ~/PUBREPOS/neovim/runtime/lua/ ]]; then
      cp ~/PUBREPOS/zsh/neovim/lua/*lua ~/PUBREPOS/neovim/runtime/lua/
    fi

    ;;
    *)
    echo "no idea what kinda system this is, but it sucks, that much I can tell you.. "
    ;;
esac
# not gonna test for these just run 'em KISS 





