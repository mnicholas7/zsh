local api = vim.api

-- Highlight on yank
local yankGrp = api.nvim_create_augroup("YankHighlight", { clear = true })
api.nvim_create_autocmd("TextYankPost", {
  command = "silent! lua vim.highlight.on_yank()",
  group = yankGrp,
})


-- lua exec file
api.nvim_create_autocmd(
  "FileType",
  { pattern = { "lua" }, command = [[noremap  <buffer><F3>      :w<CR>:exec 'terminal lua -i' shellescape(@%, 1)<CR>]] }
)

api.nvim_create_autocmd(
  "FileType",
  { pattern = { "lua" }, command = [[inoremap <buffer><F3> <esc>:w<CR>:exec 'terminal lua -i' shellescape(@%, 1)<CR>]] }
)
--
--
-- perl exec file
api.nvim_create_autocmd(
  "FileType",
  { pattern = { "perl" }, command = [[noremap  <buffer><F4>      :w<CR>:exec 'terminal perl -d' shellescape(@%, 1)<CR>]] }
)

api.nvim_create_autocmd(
  "FileType",
  { pattern = { "perl" }, command = [[inoremap <buffer><F4> <esc>:w<CR>:exec 'terminal perl -d' shellescape(@%, 1)<CR>]] }
)
--
-- zsh exec file
api.nvim_create_autocmd(
  "FileType",
  { pattern = { "zsh" }, command = [[noremap  <buffer><F5>      :w<CR>:exec 'terminal zsh -x -o shwordsplit' shellescape(@%, 1)<CR>]] }
)

api.nvim_create_autocmd(
  "FileType",
  { pattern = { "zsh" }, command = [[inoremap <buffer><F5> <esc>:w<CR>:exec 'terminal zsh -x -o shwordsplit' shellescape(@%, 1)<CR>]] }
)
-- bash exec file 
api.nvim_create_autocmd(
  "FileType",
  { pattern = { "bash" }, command = [[noremap  <buffer><F6>        :w<CR>:exec 'terminal bash -x' shellescape(@%, 1)<CR>]] }
)

api.nvim_create_autocmd(
  "FileType",
  { pattern = { "bash" }, command = [[inoremap <buffer><F6>   <esc>:w<CR>:exec 'terminal bash -x' shellescape(@%, 1)<CR>]] }
)
-- python exec file 
api.nvim_create_autocmd(
  "FileType",
  { pattern = { "python" }, command = [[noremap  <buffer><F7>      :w<CR>:exec 'terminal python3' shellescape(@%, 1)<CR>]] }
)

api.nvim_create_autocmd(
  "FileType",
  { pattern = { "python" }, command = [[inoremap <buffer><F7> <esc>:w<CR>:exec 'terminal python3' shellescape(@%, 1)<CR>]] }
)

-- python -m pdb
api.nvim_create_autocmd(
  "FileType",
  { pattern = { "python" }, command = [[noremap  <buffer><F8>      :w<CR>:exec 'terminal python3 -m pdb' shellescape(@%, 1)<CR>]] }
)

api.nvim_create_autocmd(
  "FileType",
  { pattern = { "python" }, command = [[inoremap <buffer><F8> <esc>:w<CR>:exec 'terminal python3 -m pdb' shellescape(@%, 1)<CR>]] }
)

-- python interact
api.nvim_create_autocmd(
  "FileType",
  { pattern = { "python" }, command = [[noremap  <buffer><F8>      :w<CR>:exec 'terminal python3 -i' shellescape(@%, 1)<CR>]] }
)

api.nvim_create_autocmd(
  "FileType",
  { pattern = { "python" }, command = [[inoremap <buffer><F8> <esc>:w<CR>:exec 'terminal python3 -i' shellescape(@%, 1)<CR>]] }
)


