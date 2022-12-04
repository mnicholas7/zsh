#!/bin/bash -x

ME=$(whoami)
MYGRP=$(groups | awk '{print $1}')

# make sure we have curl first!
sudo apt install curl -y

# install oh-my-zsh plugin mgr
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# clone some zsh plugs
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

git clone https://github.com/zsh-users/zsh-autosuggestions \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/softmoth/zsh-vim-mode.git \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-vim-mode

git clone https://github.com/romkatv/powerlevel10k.git \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k


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
  # copy our file so we can use vim when we trigger the open command with 'l'
  sudo cp ./lfrc    /etc/lf/
  # we source this file in our .zshrc so we can triger the lfcd function with ctrl o
  sudo cp ./lfcd.sh /usr/local/bin/lfcd.sh
fi

# move our standard .rc's into place
cp .zshrc ~/ && chown ${ME}:${MYGRP} ~/.zshrc
cp .vimrc ~/ && chown ${ME}:${MYGRP} ~/.vimrc
cp .inputrc ~/ && chown ${ME}:${MYGRP} ~/.inputrc
cp .pythonrc ~/ && chown ${ME}:${MYGRP} ~/.pythonrc
cp .tmux.conf ~/ && chown ${ME}:${MYGRP} ~/.tmux.conf

# mkdir .tmux plugin dir exists
mkdir -p ~/.tmux/plugins/

# tmux prompt
git clone https://github.com/tmux-plugins/tpm.git \
    ${TMUX_CUSTOM:-~/.tmux/plugins}/


	
