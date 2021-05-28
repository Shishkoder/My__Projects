class NewInt( int ):
        
    def repeat( self, n = 2 ):
    	return int( str( self ) * n )

    def to_bin( self ):
    	return int( bin( self )[ 2 : ] )


a = NewInt(2)
print( a.repeat(5) )
print( a.to_bin() )