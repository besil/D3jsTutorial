class LineFeed(object):
    def __init__(self, header, lines, key=None):
        self.header = header
        self.lines  = lines
        self.currentLine = 0
        
        if key is not None:
            self.key        = key
            self.keyname    = key[0]
            self.positions  = key[1:]
        else: self.keyname = self.positions = None
        
    def __getitem__(self, key):
        ''' Returns always a list of elements '''
        if key == self.keyname:
            return [ "-".join( l[x] for x in self.positions ) for l in self.lines ]
            
        pos = self.header[key]
        return [ l[pos] for l in self.lines ]
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.currentLine >= len( self.lines ): raise StopIteration()
        
        res = LineFeed( self.header, [ self.lines[self.currentLine] ], self.key )
        self.currentLine += 1
        return res