"""
Helper file to generate the index page 

Search through subdirectories to find/build the homepage
* Help identify files incorrectly named
* Ensure consistency (structure/filenames)

Example:
\> python build-html.py > index.html


"""


# list of videos that correlate with the lectures - play through the commentary (sit and watch)
videos = { "Introduction"                 : "https://www.youtube.com/embed/V5jkHVk1fXE?start=5&autoplay=1", 
           "Internet and Web"             : "https://www.youtube.com/embed/8CBhwckd9eo?start=5&autoplay=1",
		   "Fundamentals of HTML and CSS" : "https://www.youtube.com/embed/bFhOCKI4eUI?start=5&autoplay=1",
		   "Productive Web Programming"   : "https://www.youtube.com/embed/9V2e_V1hl_c?start=5&autoplay=1"
		 }
		 


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
<td>Video 			</td>
<td>        		</td>
<td>Notes   		</td>
<td>Labs    		</td>
<td>Quiz    		</td>
<td>Crossword 		</td>
<td>Demos    	    </td>
</tr>
""";

week = 1
for i in range(0,25):
	
	s = 'Lecture %02d' % (i)
	val = finddir( s, 'html' )
	if val == 0:
		continue
	
	str += '<tr>'
	topic = val[0].split('.')
	topic = topic[0].split(' -')[1]
	topic = topic.strip()

	if ( (i+1) % 2 == 0 or i==1) and i>0:
		str += "<td>%2d</td>" % (week)
		week+=1
	else:
		str += "<td> &nbsp; </td>"
	
	str += "<td>%2d</td>" % (i)
	

	str += "<td>%s</td>"  % (topic)
	if ( showDetails ):
		str += "<td><a href='%s'>Slides (%d)</td>" % (val[1], findNum(val[1], '</section>') )
	else:
		str += "<td><a href='%s'>Slides</td>" % (val[1]) # , findNum(val[1], '</section>') )
	
	
	str += '<td>      &nbsp;  		</td>';
		
	#tmp = finddir( 'Lecture %02d' % (i), 'pdf' )
	#if tmp == 0:
	#	str += "<td>   </td>" 
	#else:
	#	str += "<td><a href='%s'> pdf </td>" % tmp[1]
		
	tmp = topic in videos; # 'Lecture %02d' % (i), 'pdf' )
	if tmp == 0:
		str += "<td> - </td>" 
	else:
		str += "<td><a href='%s'> Video </td>" % videos[ topic ]
	
	str += '<td>      &nbsp;  		</td>';
	
	tmp = finddir( 'Notes %02d' % (i), 'html' )
	if tmp == 0:
		str += "<td> - </td>" 
	else:
		str += "<td><a href='%s'>Notes</td>" % tmp[1]
	
	
	tmp = finddir( 'Lab %02d' % (i), 'pdf' )
	if tmp == 0:
		str += "<td> - </td>" 
	else:
		str += "<td><a href='%s'>Lab</td>" % tmp[1]


	tmp = finddir( 'Quiz %02d -' % (i) )
	if tmp == 0:
		str += "<td> - </td>" 
	else:
		if ( showDetails ):
			str += "<td><a href='%s'>Revision (%d)</td>" % (tmp[1], findNum(tmp[1], 'question:') )
		else:
			str += "<td><a href='%s'>Revision</td>" % tmp[1]
			
	tmp = finddir( 'Crossword %02d' % (i), 'html' )
	if tmp == 0:
		str += "<td> - </td>" 
	else:
		str += "<td><a href='%s'>Crossword</td>" % tmp[1]

		
	tmp = finddir( 'Game %02d' % (i), 'html' )
	if tmp == 0:
		tmp = finddir( 'App %02d' % (i), 'html' )
		if tmp == 0:
			str += "<td> - </td>" 
		else:
			str += "<td><a href='%s'>App</td>" % tmp[1]
	else:
		str += "<td><a href='%s'>Game</td>" % tmp[1]
		
	str += '</tr>\n'
	
	#if 'Review' in topic:
	#	str += '<tr><td> &nbsp; </td></tr>'

str += '</table>'


str += '<br>'
str += "Assessment:<br>"
str += "Exam 50% <br>"
# str += "Courseworks 50%<br>"
str += "Coursework (50%%) (<a href='%s'>Document Details</a>) &nbsp;" % ( finddir( 'cw01.pdf')[1] )
str += "(<a href='%s'>Support Sides</a>) &nbsp;" % ( finddir( 'Coursework.html')[1] )
str += "(<a href='%s'>Checksheet</a>)" % ( finddir( 'cw01-checklist.pdf')[1] )
str += "<!-- (<a href='%s'>Demonstration Sheet</a>) --> " % ( finddir( 'sheet.pdf')[1] )
str += "<br>"


#str += '<br><br>'
#str += "Coursework (50%%) <a href='%s'>Link</a> <br>" % ( finddir( 'cw01')[1] )

str += "</td></tr></table>"


str += """
<br>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-148326645-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-148326645-1');
</script>
"""


print( str )









