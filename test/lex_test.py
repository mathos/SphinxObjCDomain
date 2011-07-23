'''
Created on Jul 22, 2011

@author: mathos
'''
from sphinxcontrib.sphinxlex import SphinxLexer

def test_lex():
	test = SphinxLexer()
	test.build()
	test.test("- (void)createModel")
	test.test("- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation")