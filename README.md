![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)

# Rat

![the cats away](https://github.com/oTropicalista/rat/blob/master/img/img1.png)

## DESCRIPTION
File content viewer like "cat" with syntax highlighting, Markdown previewer and support for all the Pygments themes. Using the Rich library.

- [Syntax highlight](#Syntax-highlight)
- [Markdown Previewer](#Markdown-Previewer)
- [Files attributes](#Files-attributes)
- [Themes](#Themes)

## REQUIREMENTS
os\
sys\
argparse\
rich\
rich.syntax\
rich.console\
rich.markdown\
configparser

```
$ pip install -r requirements.txt
```

## Usage
```
rat.py [-h] [-n] [-t THEME] [-md] [-i] File

positional arguments:
  File                  File name

optional arguments:
  -h, --help            show this help message and exit
  -n, --numbers         Line numbers (default=False)
  -t THEME, --theme THEME
                        Setting theme (default=vim)
  -md, --markdown       Flag for markdown files preview
  -i, --info            Infos about the file

```

## Syntax highlight

## Markdown Previewer
![opa](https://github.com/oTropicalista/rat/blob/master/img/img2.png)

## Files attributes

## Themes