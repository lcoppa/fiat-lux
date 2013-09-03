let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <silent> <S-Tab> =UltiSnips_JumpBackwards()
inoremap <silent> <C-Tab> =UltiSnips_ListSnippets()
nmap  :s/\s\+$//
noremap ru :call RopeUseFunction()
noremap rad :call RopeShowDoc()
noremap rac :call RopeShowCalltip()
noremap rx :call RopeRestructure()
noremap r1r :call RopeRenameCurrentModule()
noremap rr :call RopeRename()
noremap ro :call RopeOrganizeImports()
noremap r1v :call RopeMoveCurrentModule()
noremap rv :call RopeMove()
noremap r1p :call RopeModuleToPackage()
noremap ra? :call RopeLuckyAssist()
noremap raj :call RopeJumpToGlobal()
noremap rf :call RopeIntroduceFactory()
noremap ri :call RopeInline()
noremap rag :call RopeGotoDefinition()
noremap rnv :call RopeGenerateVariable()
noremap rnp :call RopeGeneratePackage()
noremap rnm :call RopeGenerateModule()
noremap rnf :call RopeGenerateFunction()
noremap rnc :call RopeGenerateClass()
noremap raf :call RopeFindOccurrences()
noremap rai :call RopeFindImplementations()
noremap rl :call RopeExtractVariable()
noremap rm :call RopeExtractMethod()
noremap ra/ :call RopeCodeAssist()
noremap rs :call RopeChangeSignature()
noremap ra :call RopeAutoImport()
snoremap <silent>  c
nmap  h
xmap  h
omap  h
xnoremap 	 :call UltiSnips_SaveLastVisualSelection()gvs
snoremap <silent> 	 :call UltiSnips_ExpandSnippetOrJump()
map <NL> k
map  l
xnoremap <silent>  :call multiple_cursors#new("v")
nnoremap <silent>  :call multiple_cursors#new("n")
noremap  :nohl
noremap pu :call RopeUndo()
noremap pr :call RopeRedo()
noremap pc :call RopeProjectConfig()
noremap po :call RopeOpenProject()
noremap pg :call RopeGenerateAutoimportCache()
noremap p4f :call RopeFindFileOtherWindow()
noremap pf :call RopeFindFile()
noremap pnp :call RopeCreatePackage()
noremap pnm :call RopeCreateModule()
noremap pnf :call RopeCreateFile()
noremap pnd :call RopeCreateDirectory()
noremap pk :call RopeCloseProject()
vnoremap \s :sort
nmap \l :set list!
nmap gx <Plug>NetrwBrowseX
nnoremap <silent> <Plug>(n) :call multiple_cursors#new('v')
nnoremap <silent> <Plug>(s) :call multiple_cursors#skip()
nnoremap <silent> <Plug>(p) :call multiple_cursors#prev()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0)
snoremap <silent> <Del> c
snoremap <silent> <BS> c
snoremap <silent> <C-Tab> :call UltiSnips_ListSnippets()
snoremap <silent> <S-Tab> :call UltiSnips_JumpBackwards()
map <F3> :NERDTreeToggle
map <F2> :RopeRename
map <F5> :PyLint
inoremap <silent> 	 =UltiSnips_ExpandSnippetOrJump()
cabbr w!! w !sudo tee "%"
let &cpo=s:cpo_save
unlet s:cpo_save
set autochdir
set autoindent
set backspace=2
set clipboard=unnamed
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set guifont=DejaVu\ Sans\ Mono\ for\ Powerline\ 9
set helplang=en
set history=100
set hlsearch
set ignorecase
set incsearch
set laststatus=2
set listchars=tab:»\ ,eol:¬
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/bundle/nerdtree,~/.vim/bundle/python-mode,~/.vim/bundle/supertab,~/.vim/bundle/ultisnips,~/.vim/bundle/vim-fugitive,~/.vim/bundle/vim-multiple-cursors,/var/lib/vim/addons,/usr/share/vim/vimfiles,/usr/share/vim/vim73,/usr/share/vim/vimfiles/after,/var/lib/vim/addons/after,~/.vim/bundle/python-mode/after,~/.vim/bundle/ultisnips/after,~/.vim/after,~/.vim/bundle/powerline/powerline/bindings/vim
set scrolljump=5
set shiftround
set shiftwidth=4
set smartcase
set softtabstop=4
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set noswapfile
set tabstop=4
set textwidth=79
set updatetime=1000
set wildignore=*.pyc
set nowritebackup
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/picode/fiat-lux
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +113 ~/picode/fiat-lux/fiat-lux.py
args fiat-lux.py
edit ~/picode/fiat-lux/fiat-lux.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 89 + 89) / 178)
exe 'vert 2resize ' . ((&columns * 88 + 89) / 178)
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <silent> <C-Space> =RopeCodeAssistInsertMode()
inoremap <buffer> <silent> <Nul> =RopeCodeAssistInsertMode()
inoremap <buffer> <silent> <S-Tab> =RopeLuckyAssistInsertMode()
noremap <buffer> <silent> m :emenu Rope . 	
noremap <buffer> <silent> f :RopeFindOccurrences
noremap <buffer> <silent> d :RopeShowDoc
noremap <buffer> <silent> g :RopeGotoDefinition
onoremap <buffer> C :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> <silent> K :call pymode#doc#Show(@*)
nnoremap <buffer> <silent> K :call pymode#doc#Show(expand('<cword>'))
onoremap <buffer> M :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> [M :call pymode#motion#vmove('^\s*def\s', 'b')
vnoremap <buffer> [[ :call pymode#motion#vmove('^\(class\|def\)\s', 'b')
onoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
onoremap <buffer> [C :call pymode#motion#move('^\(class\|def\)\s', 'b')
onoremap <buffer> [[ :call pymode#motion#move('^\(class\|def\)\s', 'b')
nnoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
nnoremap <buffer> [C :call pymode#motion#move('^\(class\|def\)\s', 'b')
nnoremap <buffer> [[ :call pymode#motion#move('^\(class\|def\)\s', 'b')
nnoremap <buffer> <silent> \b :call pymode#breakpoint#Set(line('.'))
vnoremap <buffer> <silent> \r :Pyrun
nnoremap <buffer> <silent> \r :Pyrun
vnoremap <buffer> ]M :call pymode#motion#vmove('^\s*def\s', '')
vnoremap <buffer> ]] :call pymode#motion#vmove('^\(class\|def\)\s', '')
onoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
onoremap <buffer> ]C :call pymode#motion#move('^\(class\|def\)\s', '')
onoremap <buffer> ]] :call pymode#motion#move('^\(class\|def\)\s', '')
nnoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
nnoremap <buffer> ]C :call pymode#motion#move('^\(class\|def\)\s', '')
nnoremap <buffer> ]] :call pymode#motion#move('^\(class\|def\)\s', '')
vnoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
onoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
onoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
vnoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
onoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal balloonexpr=
setlocal nobinary
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
set colorcolumn=80
setlocal colorcolumn=80
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:XCOMM,n:>,fb:-
setlocal commentstring=#%s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=pymode#folding#expr(v:lnum)
setlocal foldignore=#
set foldlevel=99
setlocal foldlevel=99
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=expr
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=pymode#folding#text()
setlocal formatexpr=
setlocal formatoptions=cq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=pymode#indent#Indent(v:lnum)
setlocal indentkeys=!^F,o,O,<:>,0),0],0},=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
setlocal nolinebreak
setlocal nolisp
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=RopeOmni
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
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=.py
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tags=~/picode/fiat-lux/.git/python.tags,~/picode/fiat-lux/.git/tags,./tags,./TAGS,tags,TAGS
setlocal textwidth=79
setlocal thesaurus=
setlocal noundofile
setlocal nowinfixheight
setlocal nowinfixwidth
set nowrap
setlocal nowrap
setlocal wrapmargin=0
let s:l = 113 - ((17 * winheight(0) + 17) / 34)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
113
normal! 08l
wincmd w
argglobal
edit ~/picode/fiat-lux/fiat-lux.py
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <silent> <C-Space> =RopeCodeAssistInsertMode()
inoremap <buffer> <silent> <Nul> =RopeCodeAssistInsertMode()
inoremap <buffer> <silent> <S-Tab> =RopeLuckyAssistInsertMode()
noremap <buffer> <silent> m :emenu Rope . 	
noremap <buffer> <silent> f :RopeFindOccurrences
noremap <buffer> <silent> d :RopeShowDoc
noremap <buffer> <silent> g :RopeGotoDefinition
onoremap <buffer> C :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> <silent> K :call pymode#doc#Show(@*)
nnoremap <buffer> <silent> K :call pymode#doc#Show(expand('<cword>'))
onoremap <buffer> M :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> [M :call pymode#motion#vmove('^\s*def\s', 'b')
vnoremap <buffer> [[ :call pymode#motion#vmove('^\(class\|def\)\s', 'b')
onoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
onoremap <buffer> [C :call pymode#motion#move('^\(class\|def\)\s', 'b')
onoremap <buffer> [[ :call pymode#motion#move('^\(class\|def\)\s', 'b')
nnoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
nnoremap <buffer> [C :call pymode#motion#move('^\(class\|def\)\s', 'b')
nnoremap <buffer> [[ :call pymode#motion#move('^\(class\|def\)\s', 'b')
nnoremap <buffer> <silent> \b :call pymode#breakpoint#Set(line('.'))
vnoremap <buffer> <silent> \r :Pyrun
nnoremap <buffer> <silent> \r :Pyrun
vnoremap <buffer> ]M :call pymode#motion#vmove('^\s*def\s', '')
vnoremap <buffer> ]] :call pymode#motion#vmove('^\(class\|def\)\s', '')
onoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
onoremap <buffer> ]C :call pymode#motion#move('^\(class\|def\)\s', '')
onoremap <buffer> ]] :call pymode#motion#move('^\(class\|def\)\s', '')
nnoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
nnoremap <buffer> ]C :call pymode#motion#move('^\(class\|def\)\s', '')
nnoremap <buffer> ]] :call pymode#motion#move('^\(class\|def\)\s', '')
vnoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
onoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
onoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
vnoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
onoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal balloonexpr=
setlocal nobinary
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
set colorcolumn=80
setlocal colorcolumn=80
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:XCOMM,n:>,fb:-
setlocal commentstring=#%s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=pymode#folding#expr(v:lnum)
setlocal foldignore=#
set foldlevel=99
setlocal foldlevel=99
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=expr
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=pymode#folding#text()
setlocal formatexpr=
setlocal formatoptions=cq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=pymode#indent#Indent(v:lnum)
setlocal indentkeys=!^F,o,O,<:>,0),0],0},=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
setlocal nolinebreak
setlocal nolisp
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=RopeOmni
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
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=.py
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tags=~/picode/fiat-lux/.git/python.tags,~/picode/fiat-lux/.git/tags,./tags,./TAGS,tags,TAGS
setlocal textwidth=79
setlocal thesaurus=
setlocal noundofile
setlocal nowinfixheight
setlocal nowinfixwidth
set nowrap
setlocal nowrap
setlocal wrapmargin=0
let s:l = 113 - ((17 * winheight(0) + 17) / 34)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
113
normal! 08l
wincmd w
exe 'vert 1resize ' . ((&columns * 89 + 89) / 178)
exe 'vert 2resize ' . ((&columns * 88 + 89) / 178)
tabnext 1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
