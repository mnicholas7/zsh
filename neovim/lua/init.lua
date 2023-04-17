-- local set = vim.opt
--
-- This is for nvim-tree - lua based nvim file browser
-- disable netrw at the very start of your init.lua (strongly advised)
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

-- set termguicolors to enable highlight groups
vim.opt.termguicolors = true


vim.opt.clipboard = 'unnamedplus'
vim.opt.mouse = '' 
vim.opt.hlsearch = true
vim.opt.incsearch = true
vim.opt.ruler = true
vim.opt.showcmd = true
vim.opt.expandtab = true
vim.opt.shiftwidth = 2
vim.opt.softtabstop = 2
vim.opt.showcmd = true
vim.opt.foldmethod = 'indent'
vim.opt.foldcolumn = '1'
vim.opt.laststatus = 2
vim.opt.listchars = 'tab:†ⅱ,trail:Ѫ,eol:$,nbsp:ϟ'



-- vim.opt.clipboard = 'unnamedplus'

-- for name,_ in pairs(package.loaded) do  for name,_ in pairs(package.loaded) do
-- function _G.ReloadConfig()
--   for name,_ in pairs(package.loaded) do
--     if name:match('^user') and not name:match('nvim-tree') then
--       package.loaded[name] = nil
--     end
--   end
-- 
--   -- dotfile(vim.env.MYVIMRC)
--   loadfile('init')
--   vim.notify("Nvim configuration reloaded!", vim.log.levels.INFO)
-- end


vim.g.mapleader = " "
--
-- switch back to netrw
vim.keymap.set("n", "<leader>o", vim.cmd.Ex)

-- " " Copy to clipboard

-- vim.api.nvim_set_keymap( 'v', '<leader>y'  , '"+y'   , { vnoremap = true })               
vim.api.nvim_set_keymap( 'n', '<leader>Y'  , '"+yg_' , { noremap = true })         
vim.api.nvim_set_keymap( 'n', '<leader>y'  , '"+y'   , { noremap = true })         
vim.api.nvim_set_keymap( 'n', '<leader>yy' , '"+yy'  , { noremap = true })         

-- " " Paste from clipboard

vim.api.nvim_set_keymap( 'n', '<leader>p', '"+p' , { noremap = true })
vim.api.nvim_set_keymap( 'n', '<leader>P', '"+P' , { noremap = true })
-- vim.api.nvim_set_keymap( 'v', '<leader>p', '"+p' , { vnoremap = true })
-- vim.api.nvim_set_keymap( 'v', '<leader>P', '"+P' , { vnoremap = true })


-- just a test really to see if this file is working still
vim.api.nvim_set_keymap('i', 'jkl', '<ESC>', { noremap = true })

vim.o.relativenumber = true

-- require('statusline')
--  use('eviline')

-- vim.api.nvim_set_keymap("n", "<leader><CR>", "<cmd>lua ReloadConfig()<CR>", { noremap = true, silent = false })







local ensure_packer = function()
  local fn = vim.fn
  local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
  if fn.empty(fn.glob(install_path)) > 0 then
    fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
    vim.cmd [[packadd packer.nvim]]
    return true
  end
  return false
end

local packer_bootstrap = ensure_packer()

return require('packer').startup(function(use)
  use 'wbthomason/packer.nvim'
  -- My plugins here
  use 'nvim-lualine/lualine.nvim'

  -- use 'nvim-lua/lsp_extensions.nvim'
  -- use 'ms-jpq/coq_nvim'

  -- colorscheme
  use 'joshdick/onedark.vim'

  -- fuzzy finder
  use 'junegunn/fzf'

  use 'tpope/vim-surround'
  use 'tpope/vim-sensible'
  use 'tpope/vim-repeat'
  use 'tpope/vim-unimpaired'
  use 'xiyaowong/nvim-transparent'

  -- Post-install/update hook with neovim command
  -- use { 'nvim-treesitter/nvim-treesitter'}
  --
  --
  use {
    'VonHeikemen/lsp-zero.nvim',
    requires = {
      -- LSP Support
      {'neovim/nvim-lspconfig'},
      {'williamboman/mason.nvim'},
      {'williamboman/mason-lspconfig.nvim'},
  
      -- Autocompletion
      {'hrsh7th/nvim-cmp'},
      {'hrsh7th/cmp-buffer'},
      {'hrsh7th/cmp-path'},
      {'saadparwaiz1/cmp_luasnip'},
      {'hrsh7th/cmp-nvim-lsp'},
      {'hrsh7th/cmp-nvim-lua'},
  
      -- Snippets
      {'L3MON4D3/LuaSnip'},
      {'rafamadriz/friendly-snippets'},
    }
  }

  use {
    'nvim-tree/nvim-tree.lua',
    requires = {
      'nvim-tree/nvim-web-devicons', -- optional
    },
    config = function()
      require("nvim-tree").setup {}
    end
  }

  -- Automatically set up your configuration after cloning packer.nvim
  -- Put this at the end after all plugins
  if packer_bootstrap then
    require('packer').sync()
  end

vim.opt.signcolumn = 'yes'
vim.opt.termguicolors = true
pcall(vim.cmd, 'colorscheme onedark')

require("transparent").setup({
  enable = true, -- boolean: enable transparent
  extra_groups = { -- table/string: additional groups that should be cleared
    -- In particular, when you set it to 'all', that means all available groups

    -- example of akinsho/nvim-bufferline.lua
    "BufferLineTabClose",
    "BufferlineBufferSelected",
    "BufferLineFill",
    "BufferLineBackground",
    "BufferLineSeparator",
    "BufferLineIndicatorSelected",
  },
  exclude = {}, -- table: groups you don't want to clear
})

require'lspconfig'.bashls.setup{}
require'lspconfig'.pyright.setup{}
--
-- 'mnlualine' is located here: ~/PUBREPOS/neovim/runtime/lua
require('mnlualine')
-- 'mnauto' is located here: ~/PUBREPOS/neovim/runtime/lua
require('mnauto')
-- 'lualspconfig' is located here: ~/PUBREPOS/neovim/runtime/lua
require('lualspconfig')
--
local lsp = require('lsp-zero')

lsp.preset('recommended')
lsp.nvim_workspace()
lsp.setup()

end)


