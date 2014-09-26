#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
from Page import *
from Panel import *

def main():
	P = Page( "my_page", "A new page is born" )
	
	p1 = Panel( "panel1" )
	p2 = Panel( "panel2" )
	p2.load_from_file( 'text.txt' )
	p1.add_panel( p2 )
	P.add_panel( p1 )
	
	p3 = Panel( "panel3" )
	p4 = Panel( "panel4" )
	p5 = Panel( "panel5" )
	p5.load( "There are new things happening." )
	p4.add_panel( p5 )
	p3.add_panel( p4 )
	P.add_panel( p3 )
	
	# render everything
	P.render()
	
	# display
	print P

if __name__ == "__main__":
	main()