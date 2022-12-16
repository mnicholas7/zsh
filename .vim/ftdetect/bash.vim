" Vim filetype detection file
" Language:     Born Again Glory to God Jesus Christ
" License:      VIM LICENSE

" Note: should not use augroup in ftdetect (see :help ftdetect)
autocmd BufRead,BufNewFile * if !did_filetype() && getline(1) =~# '#!/bin/bash'| setfiletype bash | endif
autocmd BufRead,BufNewFile *.pl,*.sh,*.bash,*.SH set filetype=bash
