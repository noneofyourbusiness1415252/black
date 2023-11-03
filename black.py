#!/usr/bin/python3
# -*- coding: utf-8 -*-
import click

import sys


class TabStr(str):
  def __len__(self) -> int:
    return super().__len__() + self.count("\t") * tabSurplus


import black as upstream
import black.strings as black_str
import black.linegen as black_line

_orgLineStr = black_line.Line.__str__
_orgFixDocString = black_str.fix_docstring


def lineStrIndent(self):
  original = _orgLineStr(self)
  noLeftSpaces = original.lstrip()
  if not noLeftSpaces:
    return original
  nLeadingSpaces = len(original) - len(noLeftSpaces)
  reindented = "%s%s" % (
    indentStr * int(nLeadingSpaces / divisor),
    noLeftSpaces,
  )
  return TabStr(reindented)

def fixDocString(docstring, prefix):
  return TabStr(_orgFixDocString(docstring, indentStr * int(len(prefix) / divisor)))


# Patch original black formatter function
black_line.Line.__str__ = lineStrIndent
black_line.fix_docstring = fixDocString
black_str.fix_docstring = fixDocString


@click.command(context_settings={"ignore_unknown_options": True})
@click.option("--indent", type=int, default=4)
@click.option("--tabs", is_flag=True)
@click.argument("black", nargs=-1, type=click.UNPROCESSED)
def main(indent, tabs, black):
  global indentStr
  global tabSurplus
  tabSurplus = indent - 1
  indentStr = " "
  if tabs:
    indentStr = "\t"
    indent = 1
  global divisor
  divisor = 4 / indent
  # behabe like normal black code
  sys.argv = ["", *black]
  sys.exit(upstream.main())


if __name__ == "__main__":
  sys.exit(main())
