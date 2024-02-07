import os
os.environ["PATH"] += os.pathsep + 'C:/ProgramData/Anaconda3/Library/bin/graphviz/'
import lexer as lexer
import pparser as parser

visualise = False
try:
    import treevis as vis
    visualise = True
except ImportError:
    visualise = False

fname = "file.txt"
data = lexer.open_file(fname)
print(data)
toks = lexer.lex(data)
for j in range(len(toks)):
    print('Tokens for input line ',j+1,'\n')
    for i in range(len(toks[j])):    
        print(toks[j][i])
    print('\n')
p = parser.ExpressionTreeBuilder()

for key, line in enumerate(toks):
    print(p.parse(line, key))  
    ptm = vis.parseTreeMaker()
    ptm.generate(p.parse(toks[key], key), key)
