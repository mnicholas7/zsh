set guifont=TerminessTTF\ Nerd\ Font\ Mono:h24
set mouse=nvi
set mousemodel=popup


" set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax enable
set showcmd
set ruler
set cursorline
set encoding=utf-8
set showmatch
set signcolumn=yes
set noexpandtab
set tabstop=4 shiftwidth=4

filetype plugin indent on

set list

set relativenumber
" so ~/.vim/plugins.vim
" so ~/.vim/plugin-config.vim
" so ~/.vim/maps.vim

colorscheme slate
"let g:gruvbox_contrast_dark = "hard"
"highlight Normal ctermbg=NONE
set laststatus=2
set noshowmode

" Javascript
" autocmd BufRead *.js set filetype=javascript.jsx
" autocmd BufRead *.jsx set filetype=javascript.jsx
" augroup filetype javascript syntax=javascript

"" Searching
set hlsearch                    " highlight matches
set incsearch                   " incremental searching
set ignorecase                  " searches are case insensitive...
set smartcase                   " ... unless they contain at least one capital letter
