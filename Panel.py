# -*- encoding: utf-8 -*-

class Panel( object ):
	def __init__( self, name, data=None ):
		self.name = name
		self.data = None
		self.panels = list()
	
	def is_terminal( self ):
		if len( self.panels ) == 0:
			return True
		else:
			return False
	
	def add_panel( self, panel ):
		self.panels.append( panel )
	
	def load( self, data ):
		self.data = data
	
	def load_from_file( self, filename ):
		with open( filename ) as f:
			self.data = f.readlines()[0]		
	
	def render( self ):
		output = "<div id='%s'>\n" % self.name
		if self.is_terminal():
			output += "%s\n</div>\n" % self.data
		else:
			for p in self.panels:
				output += p.render()
			output += "</div>\n"
		return output