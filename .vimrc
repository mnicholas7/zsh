set mouse-=a
syntax on
" colorscheme evening
" colorscheme industry
colorscheme koehler
set hlsearch
set incsearch
set ruler
" set runtimepath^=~/.vim/plugin/auto-pairs.vim

set autoindent

set expandtab
set shiftwidth=2
set softtabstop=2
filetype plugin indent on
" let g:AutoPairsFlyMode = 1

set showcmd

set foldmethod=indent
set foldcolumn=2

set laststatus=2
set statusline=
set statusline +=%1*\ %n\ %*            "buffer number
set statusline +=%5*%{&ff}%*            "file format
set statusline +=%3*%y%*                "file type
set statusline +=%4*\ %<%F%*            "full path
set statusline +=%2*%m%*                "modified flag
set statusline +=%1*%=%5l%*             "current line
set statusline +=%2*/%L%*               "total lines
set statusline +=%1*%4v\ %*             "virtual column number
set statusline +=%2*0x%04B\ %*          "character under cursor


" set list

set listchars=tab:†ⅱ,trail:Ѫ,eol:$,nbsp:ϟ