#!/usr/bin/python
#------------------------------------------------------------------+
# Name: rat.py                                                     |
# Repository: https://github.com/oTropicalista/rat                 |
# Data: 18/12/2020                                                 |
#------------------------------------------------------------------+

# TODO
# - modo top e modo tail para ver primeiras ou últimas linhas, padrão 5
# linhas mas pode inserir quantas quiser
# add pager mode - ok


import os
import sys
import argparse
from rich import print
from rich.table import Table
from rich.syntax import Syntax
from rich.console import Console
from rich.markdown import Markdown
from configparser import ConfigParser

class params:
    cfg = ConfigParser()
    cfg.read('config.txt')

    NAME = cfg['app']['NAME']
    VERSION = cfg['app']['VERSION']
    DESCRIPTION = cfg['app']['DESCRIPTION']
    AUTHOR = cfg['app']['AUTHOR']
    GITHUB = cfg['app']['GITHUB']
    TITLE = """
               _
     _ __ __ _| |_
    | '__/ _` | __|
    | | | (_| | |_
    |_|  \__,_|\__| {}
    """.format(VERSION)
    BANNER = "[bold blue] {} [/bold blue]\n{}\n+ Author: {}\n+ Github: {}".format(TITLE, DESCRIPTION, AUTHOR, GITHUB)


def init():
    args = get_args()
    console = Console()

    if args.info:
        get_info(args.File)

    if args.markdown:
        with open(args.File) as md:
            markdown = Markdown(md.read())
            console.print(markdown)
    else:
        view(console, args)

def view(console, args):
    table = Table(show_header=True, header_style="bold white")
    table.add_column("{}".format(args.File))
    table.add_row(showf(console, args))
    

def showf(console, args):
    syn = Syntax.from_path(args.File, theme=args.theme, line_numbers=args.numbers)
    if args.pager:
        with console.pager():
            console.print(syn)
    console.print(syn)

def get_info(file):
    file_stats = os.stat(file)
    file_info = {
        'fname': file,
        'fsize': file_stats.st_size,
        'flines': sum(1 for line in open(file)),
        'flocale': os.path.realpath(file)
    }

    print(params.BANNER)
    print('[blue]================================[/blue]')
    print('[+] Nome: ', file_info['fname'])
    print('[+] Tamanho: ', file_info['fsize'])
    print('[+] Extensão: ')
    print('[+] Número de linhas: ', file_info['flines'])
    #print('[+] Localização absoluta: ', file_info['flocale'])
    print('[+] Localização absoluta: /home/Namekusei/rat/rat.py')

    exit()

def get_args():
    # tratar os argumentos de entrada
    psr = argparse.ArgumentParser(description="")

    # argumentos
    psr.add_argument('-n',
                     '--numbers',
                     action='store_true',
                     help='Line numbers (default=False)')
    psr.add_argument('-t',
                     '--theme',
                     dest='theme',
                     default='vim',
                     help='Setting theme (default=vim)')
    psr.add_argument('-md',
                     '--markdown',
                     action='store_true',
                     help='Flag for markdown files preview')
    psr.add_argument('-i',
                     '--info',
                     action='store_true',
                     help='Infos about the file')
    psr.add_argument('--top',
                     dest='top',
                     default='5',
                     help='View first lines of the file. (Default=5)')
    psr.add_argument('-f',
                     '--footer',
                     dest='footer',
                     default='5',
                     help='View last lines of the file. (Default=5)')
    psr.add_argument('-p',
                     '--pager',
                     action='store_true',
                     help='Flag for pager mode')
    psr.add_argument('File',
                     metavar='File',
                     type=str,
                     #required=True,
                     help='File name')
    
    
    return psr.parse_args()

if __name__ == "__main__":
    init()
