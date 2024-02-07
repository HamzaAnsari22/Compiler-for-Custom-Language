from graphviz import Digraph
import string

class parseTreeMaker:
	def __init__(self):
		self.edge_list = []
		self.dot = Digraph(comment="")
		self.alpha = []
		for s in string.ascii_uppercase:
			self.alpha.append(s)
	def generate(self, orig_tup, count):
		self.dot = Digraph(comment=str(orig_tup))
		self.treefy(orig_tup)
		self.dot.edges(self.edge_list)
		self.fig_title = r"\n\nParse tree for line\n"+str(orig_tup)
		self.dot.attr(label=self.fig_title)
		self.dot.format = "png"
		self.dot.render('output/'+str(count)+'_parse.gv', view=True)
	def treefy(self, tup):
		n_p = self.alpha.pop()
		op = tup[0]
		parse_type = 'factor'
		if op == ' * ' or op == ' / ':
			parse_type = 'term'
		elif op == ' + ' or op == ' - ':
			parse_type = 'expression'
		elif op == ' = ':
			parse_type = 'assign'
		n_op = self.alpha.pop()
		lc = tup[1]
		rc = tup[2]
		self.dot.node(n_p, parse_type)
		if type(lc) == tuple:
			call_tup = self.treefy(lc)
			lcn = call_tup[0]
			n_lcn = call_tup[1]
			self.dot.node(n_lcn,str(lcn))
			self.edge_list.append(n_p+n_lcn)
		else:
			n_lc = self.alpha.pop()
			n_lc_t = self.alpha.pop()
			self.dot.node(n_lc,"factor")
			self.dot.node(n_lc_t,str(lc))
			self.edge_list.append(n_p+n_lc)
			self.edge_list.append(n_lc+n_lc_t)
		self.dot.node(n_op, str(op))
		self.edge_list.append(n_p+n_op)
		if type(rc) == tuple:
			call_tup = self.treefy(rc)
			rcn = call_tup[0]
			n_rcn = call_tup[1]
			self.dot.node(n_rcn,str(rcn))
			self.edge_list.append(n_p+n_rcn)
		else:
			n_rc = self.alpha.pop()
			n_rc_t = self.alpha.pop()
			self.dot.node(n_rc,"factor")
			self.dot.node(n_rc_t,str(rc))
			self.edge_list.append(n_p+n_rc)
			self.edge_list.append(n_rc+n_rc_t)
		return (parse_type, n_p)

