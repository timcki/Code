let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <C-Space> 
imap <Nul> <C-Space>
inoremap <expr> <Up> pumvisible() ? "\" : "\<Up>"
inoremap <expr> <S-Tab> pumvisible() ? "\" : "\<S-Tab>"
inoremap <expr> <Down> pumvisible() ? "\" : "\<Down>"
inoremap <D-BS> 
inoremap <M-BS> 
inoremap <M-Down> }
inoremap <D-Down> <C-End>
inoremap <M-Up> {
inoremap <D-Up> <C-Home>
noremap! <M-Right> <C-Right>
noremap! <D-Right> <End>
noremap! <M-Left> <C-Left>
noremap! <D-Left> <Home>
map  h
map <NL> j
map  k
map  l
nnoremap ,d :YcmShowDetailedDiagnostic
nnoremap ,c :NERDTreeClose
nnoremap ,n :NERDTreeToggle
nnoremap ,  :nohlsearch
nnoremap ,s :mksession
nnoremap ; :
vmap [% [%m'gv``
vmap ]% ]%m'gv``
vmap a% [%v]%
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
nnoremap gV `[v`]
nnoremap j gj
nnoremap k gk
noremap <M-Down> }
noremap <D-Down> <C-End>
noremap <M-Up> {
noremap <D-Up> <C-Home>
noremap <M-Right> <C-Right>
noremap <D-Right> <End>
noremap <M-Left> <C-Left>
noremap <D-Left> <Home>
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(expand((exists("g:netrw_gx")? g:netrw_gx : '<cfile>')),netrw#CheckIfRemote())
map <Left> <Nop>
map <Right> <Nop>
map <Down> <Nop>
map <Up> <Nop>
map <C-;> 
vmap <BS> "-d
inoremap <expr> 	 pumvisible() ? "\" : "\	"
let &cpo=s:cpo_save
unlet s:cpo_save
set background=dark
set backspace=indent,eol,start
set backup
set backupdir=~/.vim-tmp,~/.tmp,~/tmp,~/var/tmp,/tmp
set backupskip=/tmp/*,/private/tmp/*
set completefunc=youcompleteme#Complete
set completeopt=preview,menuone
set cpoptions=aAceFsB
set directory=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set foldlevelstart=10
set guitablabel=%M%t
set helplang=en
set hidden
set history=1000
set hlsearch
set ignorecase
set incsearch
set langmenu=none
set laststatus=2
set lazyredraw
set matchpairs=(:),{:},[:],<:>
set mouse=a
set omnifunc=youcompleteme#OmniComplete
set pastetoggle=<F2>
set printexpr=system('open\ -a\ Preview\ '.v:fname_in)\ +\ v:shell_error
set pythondll=/usr/local/Frameworks/Python.framework/Versions/2.7/Python
set pythonhome=/usr/local/Frameworks/Python.framework/Versions/2.7
set pyxversion=2
set runtimepath=~/.vim,~/.vim/bundle/Vundle.vim,~/.vim/bundle/rust.vim,~/.vim/bundle/syntastic,~/.vim/bundle/bash-support.vim,~/.vim/bundle/nerdtree,~/.vim/bundle/YouCompleteMe,~/.vim/bundle/vim-flake8,~/.vim/bundle/vim-airline,~/.vim/bundle/vim-airline-themes,~/.vim/bundle/vim-racer,/usr/local/Cellar/macvim/8.0-127/MacVim.app/Contents/Resources/vim/vimfiles,/usr/local/Cellar/macvim/8.0-127/MacVim.app/Contents/Resources/vim/runtime,/usr/local/Cellar/macvim/8.0-127/MacVim.app/Contents/Resources/vim/runtime/pack/dist/opt/matchit,/usr/local/Cellar/macvim/8.0-127/MacVim.app/Contents/Resources/vim/vimfiles/after,~/.vim/after,~/.vim/bundle/Vundle.vim,~/.vim/bundle/Vundle.vim/after,~/.vim/bundle/rust.vim/after,~/.vim/bundle/syntastic/after,~/.vim/bundle/bash-support.vim/after,~/.vim/bundle/nerdtree/after,~/.vim/bundle/YouCompleteMe/after,~/.vim/bundle/vim-flake8/after,~/.vim/bundle/vim-airline/after,~/.vim/bundle/vim-airline-themes/after,~/.vim/bundle/vim-racer/after
set shiftround
set shortmess=filnxtToOc
set showcmd
set showmatch
set smartcase
set softtabstop=4
set tabstop=4
set termencoding=utf-8
set title
set updatetime=2000
set visualbell
set wildmenu
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Dropbox/Programming/Rust/kernel_writing
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +33 Makefile
badd +9 NERD_tree_2
badd +25 src/arch/x86_64/long_mode_init.asm
badd +6 src/lib.rs
badd +11 Cargo.toml
badd +8 src/arch/x86_64/linker.ld
badd +18 src/arch/x86_64/boot.asm
badd +39 src/vga_buffer.rs
argglobal
silent! argdel *
$argadd .
edit src/vga_buffer.rs
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=1 winheight=1 winminwidth=1 winwidth=1
argglobal
onoremap <buffer> <silent> [[ :call rust#Jump('o', 'Back')
xnoremap <buffer> <silent> [[ :call rust#Jump('v', 'Back')
nnoremap <buffer> <silent> [[ :call rust#Jump('n', 'Back')
onoremap <buffer> <silent> ]] :call rust#Jump('o', 'Forward')
xnoremap <buffer> <silent> ]] :call rust#Jump('v', 'Forward')
nnoremap <buffer> <silent> ]] :call rust#Jump('n', 'Forward')
let s:cpo_save=&cpo
set cpo&vim
nnoremap <buffer> <D-R> :RustRun! =join(b:rust_last_rustc_args)erust#AppendCmdLine(' -- ' . join(b:rust_last_args))
nnoremap <buffer> <silent> <D-r> :RustRun
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal cindent
setlocal cinkeys=0{,0},!^F,o,O,0[,0]
setlocal cinoptions=L0,(0,Ws,J1,j1
setlocal cinwords=for,if,else,while,loop,impl,mod,unsafe,trait,struct,enum,fn,extern
setlocal colorcolumn=
setlocal comments=s0:/*!,m:\ ,ex:*/,s1:/*,mb:*,ex:*/,:///,://!,://
setlocal commentstring=//%s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=youcompleteme#Complete
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
set cursorline
setlocal cursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'rust'
setlocal filetype=rust
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=10
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=indent
setlocal foldminlines=1
set foldnestmax=10
setlocal foldnestmax=10
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=croqnlj
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=
setlocal includeexpr=substitute(v:fname,'::','/','g')
setlocal indentexpr=GetRustIndent(v:lnum)
setlocal indentkeys=0{,0},!^F,o,O,0[,0]
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal nomacmeta
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:],<:>
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=youcompleteme#OmniComplete
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal signcolumn=auto
setlocal smartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=%!airline#statusline(1)
setlocal suffixesadd=.rs
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'rust'
setlocal syntax=rust
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tags=
setlocal textwidth=99
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
59
normal! zo
60
normal! zo
61
normal! zo
63
normal! zo
84
normal! zo
85
normal! zo
95
normal! zo
96
normal! zo
105
normal! zo
let s:l = 60 - ((23 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
60
normal! 018|
tabnext 1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOc
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
