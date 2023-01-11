set nocompatible
set mouse-=a
set guifont=Hurmit\ Nerd\ Font\ Mono 24
syntax on
" colorscheme evening
" colorscheme industry
colorscheme koehler
set hlsearch
set incsearch
set ruler
" set runtimepath^=~/.vim/plugin/auto-pairs.vim
"

set autoindent

set expandtab
set shiftwidth=2
set softtabstop=2
filetype on
filetype plugin on
filetype indent on
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

autocmd FileType bash    map <buffer> <F3>      :w<CR>:exec '!perl -d' shellescape(@%, 1)<CR>
autocmd FileType bash   imap <buffer> <F3> <esc>:w<CR>:exec '!perl -d' shellescape(@%, 1)<CR>

autocmd FileType bash    map <buffer> <F4>      :w<CR>:exec '!zsh -x -o shwordsplit' shellescape(@%, 1)<CR>
autocmd FileType bash   imap <buffer> <F4> <esc>:w<CR>:exec '!zsh -x -o shwordsplit' shellescape(@%, 1)<CR>

autocmd FileType bash    map <buffer> <F5>      :w<CR>:exec '!bash' shellescape(@%, 1)<CR>
autocmd FileType bash   imap <buffer> <F5> <esc>:w<CR>:exec '!bash' shellescape(@%, 1)<CR>

autocmd FileType bash    map <buffer> <F6>      :w<CR>:exec '!bash -x' shellescape(@%, 1)<CR>
autocmd FileType bash   imap <buffer> <F6> <esc>:w<CR>:exec '!bash -x' shellescape(@%, 1)<CR>

autocmd FileType python  map <buffer> <F7>      :w<CR>:exec '!python3' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <F7> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>

autocmd FileType python  map <buffer> <F8>      :w<CR>:exec '!python3 -m pdb' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <F8> <esc>:w<CR>:exec '!python3 -m pdb' shellescape(@%, 1)<CR>

autocmd FileType python  map <buffer> <F9>      :w<CR>:exec '!python3 -i' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <F9> <esc>:w<CR>:exec '!python3 -i' shellescape(@%, 1)<CR>



