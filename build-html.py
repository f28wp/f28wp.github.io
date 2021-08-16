"""
Helper file to generate the index page 

Search through subdirectories to find/build the homepage
* Help identify files incorrectly named
* Ensure consistency (structure/filenames)

Example:
\> python build-html.py > index.html


"""




import os


import sys
#print "This is the name of the script: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)

showDetails = 0
if ( len(sys.argv)>1 ):
	if ( sys.argv[1] == "details" ):
		showDetails = 1


"""
(Lecture 23 - Web Services in action Prt 2.pptx) 
(Notes 22.pdf) 
(Lab 23 - Web Services in action Prt 2.docx) 
(Revision 22 - Web Services in action Prt 1.docx) 
(Revision 02 Ans - Forms and Tables.docx)
cw
"""

lectures    = []
handouts    = []
notes       = []
labs        = []
quizzes     = []
cws         = []
games       = []

if 0:
	for currentpath, dirs, files in os.walk('.'):
		for file in files:
			if 'images' in currentpath:
				continue
			if 'build' in currentpath:
				continue
			if '.py' in file:
				continue
			if '.txt' in file:
				continue
			if '.html' in file:
				continue
			#print(os.path.join(currentpath, file))
			fn = file 
			pathandfn = os.path.join(currentpath, file)
			print( "(%s) %s" % (fn, pathandfn) )


def finddir( str, str2=0 ):
	for currentpath, dirs, files in os.walk('.'):
		for file in files:
			if 'images' in currentpath:
				continue
			if 'build' in currentpath:
				continue
			if '.py' in file:
				continue
			if '.txt' in file:
				continue
			
			if str in file:
				if str2==0:
					return [file, os.path.join(currentpath, file)]
				else:
					if str2 in file:
						return [file, os.path.join(currentpath, file)]
			#print(os.path.join(currentpath, file))
			#fn = file 
			#pathandfn = os.path.join(currentpath, file)
	return 0

def findNum( fileNameAndPath, subStr ):
	fp = open( fileNameAndPath, 'rt' );
	if ( fp == 0 ):
		return 0;
	txt = fp.read();
	fp.close();
	return txt.count( subStr );
	
	
# print( finddir('Lecture 01') )


str = ''
str += """


<link rel="shortcut icon" type="image/x-icon" href="./material/lectures/images/favicon.ico" />

<br>
<table align="center"><tr><td>

F28WP - <a href='http://www.macs.hw.ac.uk/students/cs/courses/f28wp-web-programming/'>Web Programming</a>
<br>
<br>

<table>
<tr>
<td>Wk      		</td>
<td>No      		</td>
<td>Topic   		</td>
<td>Lecture 		</td>
<td>        		</td>
<td>Notes   		</td>
<td>Tasks       </td>
<td>Quizzes    		</td>
<td>Crossword 		</td>
</tr>
""";

week  = 1
no    = 0
for i in range(0,25):
	s = 'Lecture %02d' % (no)
	val = finddir( s, 'html' )
	if val == 0:
		no = no + 1
		continue
	
	str += '<tr>'
	topic = val[0].split('.')
	topic = topic[0].split(' -')[1]
	topic = topic.strip()
	
	if ( (no+1) % 2 == 0 or no==1) and no>0:
		str += "<td>%2d</td>" % (week)
		week+=1
	else:
		str += "<td> &nbsp; </td>"
		
	if week == 7:
		str += '                         <td colspan="8">-</td></tr>\n'
		str += '<tr><td colspan="1"></td><td colspan="8">-</td></tr>\n'
		continue
	
	
	
	str += "<td>%2d</td>" % (no)
	

	str += "<td>%s</td>"  % (topic)
	if ( showDetails ):
		str += "<td><a href='%s'>Slides (%d)</td>" % (val[1], findNum(val[1], '</section>') )
	else:
		str += "<td><a href='%s'>Slides</td>" % (val[1]) # , findNum(val[1], '</section>') )
	

	str += '<td>      &nbsp;  		</td>';
	
	tmp = finddir( 'Notes %02d' % (no), 'html' )
	if tmp == 0:
		str += "<td> - </td>" 
	else:
		str += "<td><a href='%s'>Notes</td>" % tmp[1]
	
	
	tmp = finddir( 'Task %02d' % (no), 'html' )
	if tmp == 0:
		str += "<td> - </td>" 
	else:
		str += "<td><a href='%s'>Task</td>" % tmp[1]


	tmp = finddir( 'Quiz %02d -' % (i) )
	if tmp == 0:
		str += "<td> - </td>" 
	else:
		if ( showDetails ):
			str += "<td><a href='%s'>Revision (%d)</td>" % (tmp[1], findNum(tmp[1], 'question:') )
		else:
			str += "<td><a href='%s'>Revision</td>" % tmp[1]
			
	tmp = finddir( 'Crossword %02d' % (no), 'html' )
	if tmp == 0:
		str += "<td> - </td>" 
	else:
		str += "<td><a href='%s'>Crossword</td>" % tmp[1]

		
	str += '</tr>\n'
	no = no + 1
	
	#if 'Review' in topic:
	#	str += '<tr><td> &nbsp; </td></tr>'

str += '</table>'


str += '<br>'
str += "Assessment:<br>"
str += "Exam 50% <br>"
# str += "Courseworks 50%<br>"
str += "Coursework (50%) (Composed of Labs/Class Tests - see VLE for details)"
str += "<br>"


#str += '<br><br>'
#str += "Coursework (50%%) <a href='%s'>Link</a> <br>" % ( finddir( 'cw01')[1] )

str += "</td></tr></table>"




print( str )









