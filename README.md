# The Math Book

## Setup
- Use MacTex 2024 - https://www.tug.org/mactex/mactex-download.html
- Installation - `brew install mactex-no-gui`
  - Installs the entire ~5.7gb package

## Doom Emacs Config

### The `init.el`
``` emacs-lisp
(latex +cdlatex +lsp +tree-sitter)      ; writing papers in Emacs has never been so fun
```

### The `config.el`
``` emacs-lisp
;; brew install mactex-no-gui
(setenv "PATH" (concat "/Library/TeX/texbin:"
                       (getenv "PATH")))
(add-to-list 'exec-path "/Library/TeX/texbin")
(setq +latex-viewers '(pdf-tools))
(map! :map cdlatex-mode-map :i "TAB" #'cdlatex-tab)
(setq lsp-tex-server 'digestif)
```

## References
- For diagrams
  - https://ctan.org/pkg/tkz-euclide
    - The `tkz-euclide` includes `tikz` package by default
  - https://tikz.dev/
  - Math symbols - https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf
  - Drawing waves - https://www.mathsisfun.com/algebra/amplitude-period-frequency-phase-shift.html
  - Emacs Setup - https://michaelneuper.com/posts/efficient-latex-editing-with-emacs/
