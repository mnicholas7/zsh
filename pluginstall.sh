#!/bin/bash

sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \                                  
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
                                                                                                      
git clone https://github.com/zsh-users/zsh-autosuggestions \                                        
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions    
  
git clone https://github.com/softmoth/zsh-vim-mode.git \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-vim-mode
  
git clone https://github.com/romkatv/powerlevel10k.git \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k


wget https://github.com/gokcehan/lf/releases/download/r27/lf-linux-amd64.tar.gz
gunzip lf-linux-amd64.tar.gz 
tar -xvf lf-linux-amd64.tar
sudo mv lf /usr/local/bin/

sudo mkdir /etc/lf

sudo cp ./lfrc    /etc/lf/
sudo cp ./lfcd.sh /usr/local/bin/lfcd.sh

cp .zshrc ~/
