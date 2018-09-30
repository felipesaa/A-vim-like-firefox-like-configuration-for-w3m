# A-vim-like-firefox-like-configuration-for-w3m
- This is a configuration for w3m that aims to be compatible with shortcuts of
  vim-like browsers and complements (e.g. dwb, VimFx) and firefox/chrome.
- Vim-like shortcuts are preferable to firefox shortcut, So in a case that I
  can only implement one I will choose vim-like
- Many features of w3m AFAIK are not incorporated in any of these browsers, so
  the complete compatibility is impossible (e.g. BACK = delete current buffer
  and go back in history)

- Some notables features
	- h, j, k, l = Move the screen as a pager.
	- Arrow keys = Move cursor
	- w, b       = Move the cursor a word each time (forward, backward)
	- t, C-t     = Opent new foreground tab with in duckduckgo.com/lite
	- d, C-w     = Close current tab and save it to restore it
	- u, C-T     = Restore last closed tab
	- yy         = Copy current page url to clipboard
	- yf         = Copy url under cursor to clipboard
	- p          = Paste and search url in clipboard in current page
	- P          = Paste and search url in clipboard in new foreground tab
	- q          = Quit w3m with confirmation
	- ZZ         = Quit w3m without confirmation
	- o, C-l     = Focus on address bar.
	- f, enter   = Open url under cursor in current tab
	- F          = Open url under cursor in new foreground tab
	- gg         = Move cursor to the first line
	- G          = Move the cursor to the last line
	- J          = Change focus to left tab
	- K          = Change focus to right tab
	- H          = Go back in history
	- L          = Go forward in history

- This configuration in order to work needs
	- the keymap file in ~/w3m/keymap
	- the cgi scripts in /usr/lib/w3m/cgi-bin
	- the bash scripts in your $PATH
	- the xsel program for the clipboard functionality
