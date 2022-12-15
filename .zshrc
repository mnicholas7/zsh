# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
# if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
#   source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
# fi

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
# if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
#   source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
# fi

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
#ZSH_THEME="powerlevel10k/powerlevel10k"
#ZSH_THEME="fino"
#ZSH_THEME="re5et"
## xiong-chiamiov-plus
#ZSH_THEME="random"
ZSH_THEME="xiong-chiamiov-plus"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git colored-man-pages colorize pip python ansible aws jsontools pass terraform zsh-navigation-tools zsh-autosuggestions zsh-syntax-highlighting zsh-vim-mode)
# vi-mode , tmux 
source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
#
#
zstyle ':completion:*' menu select
zmodload zsh/complist
#use the vi navigation keys in menu completion
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history

LFCD="/usr/local/bin/lfcd.sh"
if [ -f "$LFCD" ]; then
      source "$LFCD"
fi

# 
source "$HOME/.oh-my-zsh/custom/plugins/zsh-vim-mode/zsh-vim-mode.plugin.zsh"

# 
MODE_CURSOR_VIINS="#00ff00 blinking bar"
MODE_CURSOR_REPLACE="$MODE_CURSOR_VIINS #ff0000"
MODE_CURSOR_VICMD="green block"
MODE_CURSOR_SEARCH="#ff00ff steady underline"
MODE_CURSOR_VISUAL="$MODE_CURSOR_VICMD steady bar"
MODE_CURSOR_VLINE="$MODE_CURSOR_VISUAL #00ffff"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh


# MN Personal alias'

alias t="ls -lt"
alias e="exit"
alias tmux="tmux -2"
alias c='rm -rf ./logs/* '
alias sshk="ssh -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc "
export sshk="ssh -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc "
alias  sshk-copy-id="ssh-copy-id -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc "
alias psh="rlwrap ~/bin/pshell"
alias vh="sudo vim /etc/hosts"
# alias scp='noglob scp'


# MN Personal ENV VARS
set -o vi
export EDITOR=vi
export PYTHONPATH=${HOME}/py:/usr/local/bin/
export PYTHONSTARTUP=${HOME}/.pythonrc

# MN Personal func's
function sshl() {
    echo ""
    echo "<dbug func enabled>"
    echo ""
	echo "The number of positional parameter : $#"
    echo "All parameters or arguments passed to the function: '$@'"
    echo ""

	if [ $# != 1 ]; then
		echo -e "\nOnly one ARG please!  Call this script with ${0} <IP/hostname>\n"
	else
		createlogsdir;
		y=`date`
		x=$1 ;
		echo -e "\nNow connecting to host: ${x} at ${y}\n\n" >> ./logs/${x}_interact.txt ;
                #ssh $x echo -e "set -o vi\nalias t=\"ls -lt\"\n" > mn;
                scp ~/m $x: ;
		ssh $x | tee -a ./logs/${x}_interact.txt ;
	fi
}

function createlogsdir() {
	if [ -d ./logs ];
	then
		echo "I see we have a ./logs dir already ... ";
	else
		echo "Creating ./logs dir ... " && mkdir logs;
	fi;
}

function stamp() {
	if [ -d ./logs ];
	then
		echo "I see we have a ./logs dir already ... ";
		echo "rotating ...";
		x=`date "+%Y%m%d_%H%M"`
		mv ./logs ./${x}_logs && echo "moving ./logs => ./${x}_logs"
		echo ""
		mkdir logs
	else
		echo "Creating ./logs dir ... " && mkdir logs;
	fi;


}

# SYS=$(uname)
# if [[ $SYS == Linux ]]
# then
#   #
# elif [[ $SYS == Darwin ]]
#   #
# fi

#PATH=${PATH}:${HOME}/bin/:${HOME}/py/
export OPENER=code
# export PATH=$( ${HOME}/py/path.py )
# ${HOME}/py/path.py 1
alias g='colorls'

