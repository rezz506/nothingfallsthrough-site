# Rebuild index.html from fragment.html. Run: python3 build.py
frag=open('fragment.html').read().replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
cur=open('index.html').read()
head_fixed=cur[:cur.index('<title>')]
i=frag.index('</style>')+len('</style>')
head_part=frag[:i].replace('<title>Nothing Falls Through</title>','<title>Nothing Falls Through | AI Assistant for Small Business Owners, Set Up and Managed for You</title>')
open('index.html','w').write(head_fixed+head_part+'\n</head>\n<body>\n'+frag[i:].lstrip()+'</body>\n</html>\n')
print('rebuilt')
