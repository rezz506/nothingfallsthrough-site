# Rebuild index.html from fragment.html. Run: python3 build.py
import re
frag=open('fragment.html').read().replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
cur=open('index.html').read()
head_fixed=cur[:cur.index('<title>')]
i=frag.index('<div class="wrap">')
head_part=frag[:i].replace('<title>Nothing Falls Through</title>','<title>Nothing Falls Through | Managed AI assistant for small business owners</title>')
open('index.html','w').write(head_fixed+head_part+'</head>\n<body>\n'+frag[i:]+'</body>\n</html>\n')
print('rebuilt')
