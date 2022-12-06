# source this file instaed so you can be in zsh or bash and it still mostly works the same!

ME=$(whoami)
MYGRP=$(groups | awk '{print $1}')

# make sure we have curl first!

# do we have CURL already ?
CURL=$(which curl)
if [[ -e $CURL ]]
then
  echo "- already have CURL installed .. skip"
else
  sudo apt install curl -y
fi

# do we have zsh already ?
ZSH=$(which zsh)
if [[ -e $ZSH ]]
then
  echo "- already have ZSH installed .. skip"
else
  sudo apt install zsh -y
fi


# do we have TMUX already ?
TMUX=$(which tmux)
if [[ -e $TMUX ]]
then
  echo "- already have TMUX installed .. skip"
else
  sudo apt install tmux -y
fi

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

if [[ -d ~/bin/ ]]
then
  echo "- already have ~/bin dir .. skip creating!"
else
  # create ~/bin/ before cp
  mkdir ~/bin/
fi

if [[ -d ~/py/ ]]
then
  echo "- already have ~/bin dir .. skip creating!"
else
  # create ~/bin/ before cp
  mkdir ~/py/
fi

# move our standard .rc's into place
cp .zshrc ~/ && chown ${ME}:${MYGRP} ~/.zshrc
cp .vimrc ~/ && chown ${ME}:${MYGRP} ~/.vimrc
cp .inputrc ~/ && chown ${ME}:${MYGRP} ~/.inputrc
cp .pythonrc ~/ && chown ${ME}:${MYGRP} ~/.pythonrc
cp .editrc ~/ && chown ${ME}:${MYGRP} ~/.editrc
cp .tmux.conf ~/ && chown ${ME}:${MYGRP} ~/.tmux.conf
cp bin/* ~/bin/ && chown ${ME}:${MYGRP} ~/bin/*
cp py/* ~/py/ && chown ${ME}:${MYGRP} ~/py/*

# move our standard dir's into place
cp -r .vim ~/ && chown -R ${ME}:${MYGRP} ~/.vim

# mkdir .tmux plugin dir exists
mkdir -p ~/.tmux/plugins/

# tmux prompt - tpm giving me issues on mac, going manual route
#git clone https://github.com/tmux-plugins/tpm.git \
#    ${TMUX_CUSTOM:-~/.tmux/plugins}/

# tmux sensible
git clone https://github.com/tmux-plugins/tmux-sensible.git \
    ${TMUX_CUSTOM:-~/.tmux/plugins}/tmux-sensible

# manual tmux-power plug-in add ( mac os don't work well w/ tpm )
git clone https://github.com/wfxr/tmux-power.git \
    ${TMUX_CUSTOM:-~/.tmux/plugins}/tmux-power

TEST=$( echo $SHELL | awk -F/ '{print $NF}' )
if [[ $TEST == zsh ]]
then
  source ~/.zshrc
fi

