# A-vim-like-firefox-like-configuration-for-w3m
Some points about this configuration

- This is a configuration for w3m that aims to be compatible with shortcuts of
  vim-like browsers, complements (e.g. dwb, VimFx) and firefox/chrome.
- Vim-like shortcuts are preferable to firefox shortcut, So in a case that I
  can only implement one I will choose vim-like
- Many features of w3m AFAIK are not incorporated in any of these browsers, so
  the complete compatibility is not posible (e.g. BACK = delete current buffer
  and go back in history)
- This configuration is work in process
- Some shortcuts
	- h, j, k, l = Move the screen as a pager.
	- Arrow keys = Move cursor
	- w, b       = Move the cursor a word each time (forward, backward)
	- 0, C-a     = Move the cursor to the fist column
	- $, C-e     = Move the cursor to the last column
	- t, C-t     = Opent new foreground tab with in duckduckgo.com/lite
	- yt         = Duplicate current tab
	- d, C-w     = Close current tab and save it to restore it
	- u, C-T     = Restore last closed tab
	- yy         = Copy current page url to clipboard
	- yf         = Copy url under cursor to clipboard
	- p          = Paste and search url in clipboard in current page
	- P          = Paste and search url in clipboard in new foreground tab
	- q          = Quit w3m with confirmation
	- ZZ         = Quit w3m without confirmation
	- o, C-l     = Focus on address bar, open in current tab
	- O          = Focus on addres bar open in new foreground tab
	- M-o        = Open current link with external browser
	- M-p        = Open link under cursor with external browser
	- f, enter   = Open url under cursor in current tab
	- F          = Open url under cursor in new foreground tab
	- gg         = Move cursor to the first line
	- G          = Move the cursor to the last line
	- J          = Change focus to left tab
	- gJ         = Move tab to the right
	- K          = Change focus to right tab
	- gK         = Move tab to the left
	- H          = Go back in history
	- L          = Go forward in history
	- {, }       = Move between links
	- /          = Enter find mode
	- n          = Find next
	- N          = Find previous
	- \*         = OPTIONS
	- \+         = HELP
	- M-r        = Reload keymap configuration
	- C-o        = Load local file
	- C-u        = See source code of the page

- This is just a part of the configuration, see the [keymap](https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m/blob/master/keymap) file to see the
  complete list
- See the [functions.txt](https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m/blob/master/documentation/functions.txt) file to see the list of functions and
  their descriptions

- This configuration in order to work needs
	- Move the [keymap](https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m/blob/master/keymap) file to ~/w3m/keymap
	- Move the cgi scripts in [root-cgi-bin](https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m/tree/master/root-cgi-bin) to /usr/lib/w3m/cgi-bin
	- Move the scripts in [scripts_in_path](https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m/tree/master/scripts_in_path) to your $PATH
	- the xsel program for the clipboard functionality
