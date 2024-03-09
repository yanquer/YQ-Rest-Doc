=========================
pandoc
=========================

一个开源的文档转换工具, 支持多种文档格式之间的互相转换.

安装::

  apt install pandoc

使用举例, 将md转换为html::

  pandoc test.md -f markdown -t html -s -o test.html

一些常用选项::

  -f FORMAT, -r FORMAT  --from=FORMAT, --read=FORMAT    输入文件格式
  -t FORMAT, -w FORMAT  --to=FORMAT, --write=FORMAT     输出文件格式, 某些支持自动通过后缀识别.
  -o FILE, --output=FILE                                输出文件位置
  -M <KEY[:VALUE]>, --metadata=KEY[:VALUE], --metadata-file=FILE

--data-dir=DIRECTORY  依赖目录
-d <FILE>             --defaults=FILE
                      --file-scope
                      --sandbox
-s                    --standalone, 独立成一个文件?
                      --template=FILE
-V <KEY[:VALUE]>      --variable=KEY[:VALUE]
                      --wrap=auto|none|preserve
                      --ascii
                      --toc, --table-of-contents
                      --toc-depth=NUMBER
-N                    --number-sections
                      --number-offset=NUMBERS
                      --top-level-division=section|chapter|part
--extract-media=PATH  输出图片目录, 比如将doc转换为rst时
                      --resource-path=SEARCHPATH
-H FILE               --include-in-header=FILE
-B FILE               --include-before-body=FILE
-A FILE               --include-after-body=FILE
                      --no-highlight
                      --highlight-style=STYLE|FILE
                      --syntax-definition=FILE
                      --dpi=NUMBER
                      --eol=crlf|lf|native
                      --columns=NUMBER
-p                    --preserve-tabs
                      --tab-stop=NUMBER
                      --pdf-engine=PROGRAM
                      --pdf-engine-opt=STRING
--reference-doc=FILE  输出doc模版文件，使用模版文件转换可以把标题之类的格式搞得更规范
                      --self-contained
                      --embed-resources
                      --request-header=NAME:VALUE
                      --no-check-certificate
                      --abbreviations=FILE
                      --indented-code-classes=STRING
                      --default-image-extension=extension
-F PROGRAM            --filter=PROGRAM
-L SCRIPTPATH         --lua-filter=SCRIPTPATH
                      --shift-heading-level-by=NUMBER
                      --base-header-level=NUMBER
                      --track-changes=accept|reject|all
                      --strip-comments
                      --reference-links
                      --reference-location=block|section|document
                      --markdown-headings=setext|atx
                      --list-tables
                      --listings
-i                    --incremental
                      --slide-level=NUMBER
                      --section-divs
                      --html-q-tags
                      --email-obfuscation=none|javascript|references
                      --id-prefix=STRING
-T STRING             --title-prefix=STRING
-c URL                --css=URL
                      --epub-subdirectory=DIRNAME
                      --epub-cover-image=FILE
                      --epub-title-page=true|false
                      --epub-metadata=FILE
                      --epub-embed-font=FILE
                      --split-level=NUMBER
                      --chunk-template=PATHTEMPLATE
                      --epub-chapter-level=NUMBER
                      --ipynb-output=all|none|best
-C                    --citeproc
                      --bibliography=FILE
                      --csl=FILE
                      --citation-abbreviations=FILE
                      --natbib
                      --biblatex
                      --mathml
                      --webtex[=URL]
                      --mathjax[=URL]
                      --katex[=URL]
                      --gladtex
                      --trace
                      --dump-args
                      --ignore-args
                      --verbose
                      --quiet
                      --fail-if-warnings
                      --log=FILE
                      --bash-completion
                      --list-input-formats
                      --list-output-formats
                      --list-extensions[=FORMAT]
                      --list-highlight-languages
                      --list-highlight-styles
-D FORMAT             --print-default-template=FORMAT
                      --print-default-data-file=FILE
                      --print-highlight-style=STYLE|FILE
-v                    --version
-h                    --help