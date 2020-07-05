#python menu to create a html and css and java document.
#can be  used to save time creating allot of code based on yes or no answers
#e.g do you want a header? answer 'yes' or 'no'
#print code to file and save with relatable tag

#file has to be created before it can be edited!

import sys

html = input("Name html file: ")
html = html.replace('.html', '')
css = input("\nName css file: ")
css = css.replace('.css', '')
original_stdout = sys.stdout

mode = int(input("Do you want to 1: create 2: edit?\n"))
if mode == 1:
#create html ready to be edited
    file = open(html + '.html', 'w')
    with file as fw:
        sys.stdout = fw # direct the standard output to the file
        print('''<!DOCTYPE HTML>
        <HTML>
        <HEAD>
        <link rel="stylesheet" type="text/css" href="'''+css +'''.css">
        </HEAD>
    
        <BODY>
     
        ''')
        sys.stdout = original_stdout #redirects output to python
        print("completed html")
    
    #create css ready to be edited
    file = open(css + '.css', 'w')
    with file as fw:
        sys.stdout = fw # direct the standard output to the file
        print('''
        ''')
        sys.stdout = original_stdout #redirects output to python
        print("completed css\n")
    
       

elif mode == 2:        
#question 1
#start of my if loops
    loop = 1
    while loop ==1:
        print("Hello, would you like to create a header with space for a logo and title. Answer with 1 or 2?\n")
        answer = int(input("1) YES\n2) NO\n"))
    
        if answer == 1:
            title = input("What would you like to write in the header: ")
#creation of html file
            file = open(html + '.html', 'a')
            with file as fw:
                sys.stdout = fw # direct the standard output to the file
                print('''
        <div class="header">
        <h1 style="color:white">''',title,'''</h1>
        </div>

        ''')
            sys.stdout = original_stdout #redirects output to python
            print("completed html")

            image = input("Enter name of jpg logo: ")
            bg = input("What color background do you want the header: ")
            
        
#creation of css file
            file = open(css + '.css', 'a')
            with file as fw:
                sys.stdout = fw # direct the standard output to the file
                print('''h1{
            color-white;
            }
            .header{S
                border-radius: 0px 0px 30px 30px;
                background-color: ''',bg,''';
                text-align: center;
                padding: 20px;
                /*Testing 2 backgrounds positioning*/
                background-image: url(''',image +'''.jpg), url(headerbg.jpg);
            background-position: right bottom, left top;
            background-repeat: no-repeat, repeat;
        }

    
        ''')
            sys.stdout = original_stdout #redirects output to python
            print("completed css\n")
            loop = 0
    
        elif answer == 2:
            print("You have selected NO\n")
            loop = 0
#error check
        else:
            print("Invalid answer. Enter 1 for yes or 2 for no.\n")
            loop = 1



#================================================================================================================
#question 2
#start of my if loops
    loop = 1
    while loop ==1:
        original_stdout = sys.stdout
        print("Would you like to create a navigation bar at the top, left, right or bottom?\nAnswer with 1 or 2 or 3?\n")
        answer = int(input("1) TOP\n2) LEFT\n3) NONE\n"))

        if answer == 1:
            linkAmount = int(input("How many links would you like to include: "))
            #creation of html file
            file = open(html + '.html', 'a')
            with file as fw:
                sys.stdout = fw # direct the standard output to the file
                print('''<div class="topnav">''')
                sys.stdout = original_stdout #redirects output to python
                i=0         
                while i<linkAmount:
                    link = input("Enter name of other html page you wish to link: ")
                    linkName = input("What will the nav bar say for this link: ")
                    sys.stdout = fw # direct the standard output to the file
                    print("<a href='",link+".html'>",linkName,"</a>")
                    sys.stdout = original_stdout
                    i+=1
                
                sys.stdout = fw
                print("</div>")
                    
                sys.stdout = original_stdout #redirects output to python
                print("completed html")

                color = input("What color would you lke the navigation bar to be: ")
                text = input("What color should the text be: ")
                hover = input("What color should the link appear when the user is hovering over it: ")
                textHover = input("What color should the text turn when user is hovering over it: ")
    #creation of css file
                file = open(css + '.css', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''.topnav{
                overflow: hidden;
                background-color:''',color,''';
                border-style: solid;
                border-width: 1px;
                border-radius: 3px 3px 3px 3px;
        }

        /*nav bar links*/
        .topnav a{
                float: right;
                display: block;
                color: ''',text,''';
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
                border-style: solid;
                border-width: 1px;
        }

        /*nav hover color*/
        .topnav a:hover{
                background-color:''',hover,''';
                color:''',textHover,''';
        }

            
            ''')
                sys.stdout = original_stdout #redirects output to python
                print("completed css")
                loop = 0

        elif answer == 2:
            loop = 0

        elif answer == 3:
            print("You have selected NO\n")
            loop = 0
        #error check
        else:
            print("Invalid answer. Enter 1 for yes or 2 for no.\n")
            loop = 1


        #================================================================================================================
        #question 3
        #start of my if loops
        loop = 1
        while loop ==1:
            original_stdout = sys.stdout
            print("Would you like to create an image at the top?\nAnswer with 1 or 2 or 3 or 4?\n")
            answer = int(input("1) 1 Image\n2) 2 Images\n3) 3 Images\n4) NONE\n"))

            if answer == 1:
                image = input("Enter name of jpg image: ")
                head = input("Enter image header text: ")
                subHead = input("Enter image sub header text: ")
                color = input("What color would you like the text in image: ")
        #creation of html file
                file = open(html + '.html', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''<div class="blog-image">
         <div class="blog-text">
         <h1 style="font-size:50px; color:''',color+'''">''',head+'''</h1>
         <h3 style="color:''',color+'''">''',subHead+'''</h3>
         </div>
        </div>
            ''')
                sys.stdout = original_stdout #redirects output to python
                print("completed html")
                
        #creation of css file
                file = open(css + '.css', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''.blog-image{
                float: center;
        background: url(''',image+'''.jpg) no-repeat center;
        background-size: cover;
        height: 500px;
        width: 90%;
        margin: auto;
        position: relative;
        border-radius: 0px 0px 30px 30px;
        }

        .blog-text{
        text-align: center;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        }
            
            ''')
                sys.stdout = original_stdout #redirects output to python
                print("completed css\n")
                loop = 0

            elif answer == 2:
                image = input("Enter first jpg image name: ")
                image2= input("Enter second jpg image name: ")
                #creation of html file
                file = open(html + '.html', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''<div class="clearfix">
         <div class="img-container">
          <img src="''',image+'''.jpg" alt="sideimg1" >
          </div>
           <div class="img-container">
          <img src="''',image2+'''.jpg" alt="sideimg1" >
          </div>
        </div>
          
            ''')
                sys.stdout = original_stdout #redirects output to python
                print("completed html")
                
                #creation of css file
                file = open(css + '.css', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''.img-container {
          float: left;
          width: 50%;
          padding: 0px;
          
        }

        .clearfix::after {
          content: "";
          clear: both;
          display: table;
        }

            ''')
                    sys.stdout = original_stdout #redirects output to python
                print("completed css\n")
                loop = 0

            elif answer == 3:
                image = input("Enter first jpg image name: ")
                image2= input("Enter second jpg image name: ")
                image3= input("Enter third jpg image name: ")
                
                #creation of html file
                file = open(html + '.html', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''<div class="clearfix">
          <div class="img-container">
          <img src="''',image + '''.jpg" alt="sideimg1" style="width:100%">
          </div>
          
          <div class="img-container">
          <img src="''',image2 + '''.jpg" alt="sideimg2" style="width:100%">
          </div>
          
          <div class="img-container">
          <img src="''',image3 + '''.jpg" alt="sideimg3" style="width:100%">
          </div>
        </div>
        </br>
          
            ''')
                sys.stdout = original_stdout #redirects output to python
                print("completed html")
                
                #creation of css file
                file = open(css + '.css', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''
        .img-container {
          float: left;
          width: 33.33%;
          
        }

        .clearfix::after {
          content: "";
          clear: both;
          display: table;
        }

            ''')
                    sys.stdout = original_stdout #redirects output to python
                print("completed css\n")
                loop = 0
                
            elif answer == 4:
                print("You have selected NO\n")
                loop = 0
        #error check
            else:
                print("Invalid answer. Enter 1 for yes or 2 for no.\n")
                loop = 1


        #================================================================================================================
        #question 4
        #start of my if loops
        loop = 1
        while loop ==1:
            original_stdout = sys.stdout
            print("Would you like to create 1, 2 or 3 columns?\nAnswer with 1 or 2 or 3?\n")
            answer = int(input("1) \n2) \n3) \n4) NONE\n"))

            if answer == 1:
                header = input("Enter header for column: ")
                para = input("Enter text for the column: ")
                color = input("What background color would you like for columns: ")
        #creation of html file
                file = open(html + '.html', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print(''' <div class="column middle" style="background-color:''',color+''';">
            <h2>''',header+'''</h2>
            <p>''',para+'''</p></div>
            ''')
                sys.stdout = original_stdout #redirects output to python
                print("completed html")
                borderImg = input("If you have a border image enter directory and name: ")
        #creation of css file
                file = open(css + '.css', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''/* Create one main article */
        .column {
          float: center;
          padding: 4px;
          height: 500px;
          }

        .middle {
        float: center;
          text-align: center;
          width: 99%;
          border: 10px solid transparent;
                border-image: url(''',borderImg+'''.jpg) 30% round;
          
        }


        /*Responsive layout columns */
        @media screen and (max-width: 600px) {
          .column.middle {
            width: 100%;
          }
        }
            
            ''')
                sys.stdout = original_stdout #redirects output to python
                print("completed css\n")
                loop = 0

            elif answer == 2:
                header = input("Enter header for the right column: ")
                para = input("Enter text for the right column: ")
                header2 = input("Enter header for the left column: ")
                para2 = input("Enter text for the left column: ")
                color = input("What background color would you like for the right column: ")
                color2 = input("What background color would you like for the left column: ")
                #creation of html file
                file = open(html + '.html', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''<div id="wrapper">
        <div id="right" style="background-color:''',color+''';">
            <h2>''',header+'''</h2>
            <p>''',para+'''</p>
          </div>
          <div id="left" style="background-color:''',color2+''';">
            <h2>''',header2+'''</h2>
            <p>''',para2+'''</p>
          </div>
            ''')
                sys.stdout = original_stdout #redirects output to python
                print("completed html")
                
        #creation of css file
                file = open(css + '.css', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''#wrapper{
        width:100%; margin 0 auto;}


        #left { width: 45%;
        float: left;}

        #right { width: 45%;
        float: right;}

            ''')
                sys.stdout = original_stdout #redirects output to python
                print("completed css\n")
                loop = 0

            elif answer == 3:
                color = input("What background color would you like for the middle column: ")
                #creation of html file
                file = open(html + '.html', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''<div id="wrapper">
          <div id="right">
            <h2>Column right</h2>
            <p>Some text..</p>
          </div>
          <div id="left">
            <h2>Column left</h2>
            <p>Some text..</p>
          </div>
          <div id="middle" style="background-color:''',color+''';">
            <h2>Column middle</h2>
            <p>Some text..</p>
          </div>
        </div>
            ''')
                sys.stdout = original_stdout #redirects output to python
                print("completed html")
                
        #creation of css file
                file = open(css + '.css', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''#wrapper{
        width:100%; margin 0 auto;}

        #middle { width: 33%;
        float: left;
        padding-left: 16px;}

        #left { width: 33%;
        float: left;}

        #right { width: 33%;
        float: right;}
            ''')
                sys.stdout = original_stdout #redirects output to python
                print("completed css\n")
                loop = 0

            elif answer == 4:
                print("You have selected NO\n")
                loop = 0
        #error check
            else:
                print("Invalid answer. Enter 1 for yes or 2 for no.\n")
                loop = 1

#================================================================================================================
        #question 5
        #start of my if loops
        loop = 1
        while loop ==1:
            original_stdout = sys.stdout
            print("Would you like to create a Footer for your page?\nAnswer with 1 or 2\n")
            answer = int(input("1) YES \n2) NO \n"))

            if answer == 1:
                #creation of html file
                file = open(html + '.html', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''<FOOTER>
<div class="footer">
<h1>Footer</h1>
</div>
</FOOTER>
''')
                sys.stdout = original_stdout #redirects output to python
                print("completed html")
                
                #creation of css file
                file = open(css + '.css', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    print('''.footer{
	
	background-color: lightblue;
	text-align: center;
	padding: 10px;
	
	
}
''')
                sys.stdout = original_stdout #redirects output to python
                print("completed css\n")
                loop = 0

            elif answer == 2:
                print("You have selected NO\n")
                loop = 0
        #error check
            else:
                print("Invalid answer. Enter 1 for yes or 2 for no.\n")
                loop = 1
                    
