#!/usr/bin/env python

import re, cgi, sys

def prettify(logfilename, ops):
	post_pattern = re.compile(r'(\[\d\d\:\d\d\])\s<(\S+)>\s(.*)')

	with open(logfilename, 'r') as infile:
		lines = infile.readlines()

	outfile = open(logfilename + '_pretty.html', 'w')

	outfile.write(
'''
<html>
<head>
<title>%s</title>
<style>
table {
	border-collapse: collapse;
	font-family: monospace;
}

td {
	background-color: #eaf0f9;
	border-bottom: 1px solid #c0c3c6;
	padding: 05px 10px;
}

.ops {
	color: #075baf;
	font-weight: bold;
}
</style>
</head>

<body>
<table>
''' % logfilename)

	for line in lines:
		outfile.write('<tr>\n')
		
		post_contents = post_pattern.match(line)
		if post_contents:
			outfile.write('<td class="timestamp">')
			outfile.write(post_contents.group(1))
			outfile.write('</td>\n')

			nick = post_contents.group(2)
			outfile.write('<td class="nick')
			outfile.write(' ops' if (nick in ops) else '')
			outfile.write('">')

			outfile.write(nick)
			outfile.write('</td>\n')

			outfile.write('<td class="post">')
			outfile.write(cgi.escape(post_contents.group(3), quote=True))
			outfile.write('</td>\n')
		else:
			outfile.write('<td colspan=3>' + line + '</td>\n')

		outfile.write('</tr>\n')

	outfile.write('''
</table>
</body>
</html>
'''
)
	outfile.close()


chan_ops = ['kushal', 'sayan', 'fhackdroid', 'praveenkumar', 'chandankumar', 
			'rtnpro', 'CuriousLearner', 'siddhesh', 'trishnag', 'mbuf']

if len(sys.argv) == 2:
	prettify(sys.argv[1], chan_ops)
else:
	print 'Usage:', sys.argv[0], '<irc_log_file_name>'
