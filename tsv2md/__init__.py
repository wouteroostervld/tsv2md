import fileinput
import textwrap
import sys


class Table(object):

    def __init__(self):
        self.lines = []
        self.width = 20 

    def feed(self,line):
        self.lines.append(line.split("\t"))

    def print_sep(self):
        for _ in range(len(self.lines[0])):
            print "-"*self.width,
        print

    def print_begin(self):
        for _ in self.lines[0][0:-1]:
            sys.stdout.write("-"*(self.width+1))
        sys.stdout.write("-"*self.width)
        print

    def print_end(self):
        self.print_begin()

    def print_row(self,line):
        cells = []
        for celldata in line:
            cells.append(textwrap.wrap(celldata,self.width)) 
        max_d = max(map(len,cells))
        for i in range(max_d):
            for cell in cells:
                try:
                    print "%-*s" % (self.width,cell[i]),
                except IndexError:
                    print " "*self.width,
            print

    def print_blank_line(self):
        print

    def dump(self):
        lines = self.lines
        header = lines[0]
        self.print_begin()
        self.print_row(header)
        self.print_sep()
        for line in lines[1:]:
            self.print_row(line)
            self.print_blank_line()
        self.print_end()

def main():
    table = Table()
    for line in fileinput.input():
        table.feed(line.rstrip())
    table.dump()


