# templater.py
import re
import sys
import json
from pathlib import Path

DIRECTIVE_RE = re.compile(
                        r'/\*\*\s*(include|variable|loopover|endloop|loopvar)'
                        r'\s*([^ *]*)\s*\*\*/')
class TemplateEngine:
    
    def __init__(self, infilename, outfilename, contextfilename):
        self.template = open(infilename).read()
        self.working_dir = Path(infilename).absolute().parent
        self.pos = 0
        self.outfile = open(outfilename, 'w')
        with open(contextfilename) as contextfile:
            self.context = json.load(contextfile)
    
    def process(self):
        match = DIRECTIVE_RE.search(self.template, pos=self.pos)
        while match:
            print('match:', match)
            self.outfile.write(self.template[self.pos : match.start()])
            print('match.groups():', match.groups())
            directive, argument = match.groups()
            print('directive:', directive)
            print('argument:', argument)
            method_name = "process_{}".format(directive)
            getattr(self, method_name)(match, argument)
            match = DIRECTIVE_RE.search(self.template, pos=self.pos)
        self.outfile.write(self.template[self.pos :])

    def process_include(self, match, argument):
        with (self.working_dir / argument).open() as includefile:
            self.outfile.write(includefile.read())
            self.pos = match.end()

    def process_variable(self, match, argument):
        self.outfile.write(self.context.get(argument, ""))
        self.pos = match.end()

    def process_loopover(self, match, argument):
        self.loop_index = 0
        self.loop_list = self.context.get(argument, [])
        self.pos = self.loop_pos = match.end()

    def process_loopvar(self, match, argument):
        self.outfile.write(self.loop_list[self.loop_index])
        self.pos = match.end()

    def process_endloop(self, match, argument):
        self.loop_index += 1
        if self.loop_index >= len(self.loop_list):
            self.pos = match.end()
            del self.loop_index
            del self.loop_list
            del self.loop_pos
        else:
            self.pos = self.loop_pos

def main():
    # infilename, outfilename, contextfilename = sys.argv[1:]
    infilename = 'index.html' 
    outfilename = 'outfile.html' 
    contextfilename = 'context.json'
    engine = TemplateEngine(infilename, outfilename, contextfilename)
    engine.process()


if __name__ == '__main__':
    main()