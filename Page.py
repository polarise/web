# -*- encoding: utf-8 -*-

class Page( object ):
	def __init__( self, name, title=None ):
		self.name = name
		self.title = title
		self.panels = list()
		self.html_top = """\
<!DOCTYPE html>
<html>
<head>
<title>%s</title>
<meta></meta>
</head>
""" % self.title
		self.html_bottom = """\
</html>"""
		self.body = ""
	
	def __repr__( self ):
		return self.html_top + self.body + self.html_bottom
		
	def add_panel( self, panel ):
		self.panels.append( panel )
	
	def render( self ):
		self.body = "<body>\n"
		for p in self.panels:
			self.body += p.render()
		self.body += "</body>\n"
		return self.body