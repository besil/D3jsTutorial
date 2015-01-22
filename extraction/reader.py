class LineFeed(object):
    def __init__(self, header, lines):
        self.header = header
        self.lines  = lines
        self.currentLine = 0
    
    def __getitem__(self, key):
        pos = self.header[key]
        return [ l[pos] for l in self.lines ]
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.currentLine >= len( self.lines ): raise StopIteration()
        
        res = LineFeed( self.header, [ self.lines[self.currentLine] ] )
        self.currentLine += 1
        return res