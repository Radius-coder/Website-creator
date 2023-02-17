#python menu to create a html and css and java document.
#can be  used to save time creating allot of code based on yes or no answers
#e.g do you want a header? answer 'yes' or 'no'
#print code to file and save with relatable tag
#add gui with buttons and pictures to show what it will look like
#file has to be created before it can be edited!

import sys
import subprocess, os, platform

html = input("Name html file: ")
html = html.replace('.html', '')
css = input("\nName css file: ")
css = css.replace('.css', '')
original_stdout = sys.stdout
i = 0


mainloop = 1
while mainloop == 1:
    print("File has to be created before it can be edited.\n")
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
            <script src="'''+css+'''.js" defer></script>

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

          #create javascript ready to be edited
        file = open(css + '.js', 'w')
        with file as fw:
            sys.stdout = fw # direct the standard output to the file
            print('''
            ''')
            sys.stdout = original_stdout #redirects output to python
            print("completed js\n")
        mainloop = 1


    elif mode == 2:

        choice = int(input("Would you like to:\n1. Add Header, logo and title\n2. Add navigation bar\n3. Add Images\n4. Add Text columns\n5. Add Footer\n6. Add video\n7. Add Countdown\n8. Add Collapsable Text Boxes\n9. Add a Modal\n10. Add page tabs\n11. Add Image Slideshow\n12. Add a Timeline\n0. Open html in browser\n"))
        if choice == 1:
        #question 1
        #start of my if loops
            loop = 1
            while loop ==1:
                print("Hello, would you like to create a header with space for a logo and title. Answer with 1 or 2?\n")
                answer = int(input("1) YES\n2) NO\n"))

                if answer == 1:
                    name = input("First, name this header container: ")
                    title = input("What would you like to write in the header: ")
                    text = input("What color would you like the text to be: ")
        #creation of html file
                    file = open(html + '.html', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''
                <div class="'''+name+'''">
                <h1 style="color:'''+text+'''">''',title,'''</h1>
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
                        print('''.'''+name+'''{
                    S
                        border-radius: 0px 0px 30px 30px;
                        background-color: ''',bg,''';
                        text-align: center;
                        padding: 20px;
                        /*Testing 2 backgrounds positioning*/
                        background-image: url(''',image +'''.jpg), url(headerbg.jpg);
                    background-position: right bottom, left top;
                    background-repeat: no-repeat, repeat;
                }''')
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
        elif choice == 2:
#================================================================================================================
    #question 2
    #start of my if loops
        
            loop = 1
            while loop ==1:
                original_stdout = sys.stdout
                print("Would you like to create a navigation bar at the top, left, right or bottom?\nAnswer with 1 or 2 or 3?\n")
                answer = int(input("1) TOP\n2) LEFT\n3) NONE\n"))

                if answer == 1:
                    
                    
                    navName = input("First, name the navigation bar container: ")
                    linkAmount = int(input("How many links would you like to include: "))
                    #creation of html file
                    file = open(html + '.html', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''<div class="''',navName+'''">''')
                        sys.stdout = original_stdout #redirects output to python
                        i = 0
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

                        bgcolor = input("What color would you lke the navigation bar to be: ")
                        text = input("What color should the text be: ")
                        hover = input("What color should the link appear when the user is hovering over it: ")
                        textHover = input("What color should the text turn when user is hovering over it: ")
                        linkPos = ""
                        linkPosCheck = 1
                        while linkPosCheck == 1:
                            linkPos = input("Do you want the links on the:\n1. Left\n2. Center\n3. Right\n")
                            if linkPos == "1":
                                linkPos = "float: left;\npadding: 14px 16px;\ntext-decoration: none;\nfont-size: 17px;\ntext-align: center;"
                                linkPosCheck = 0
                            elif linkPos == "2":
                                linkPos = "text-align: center; float: center; display: inline-block; margin: 0 5px;font-size: 17px;padding: 14px 16px;text-decoration: none;"
                                linkPosCheck = 0
                            elif linkPos == "3":
                                linkPos = "float: right;\ndisplay: block\nfont-size: 17px;\ntext-align: center;\npadding: 14px 16px;\ntext-decoration: none;"
                                linkPosCheck = 0
                            else:
                                print("Invalid Choice!\n")
                                linkPosCheck = 1
                        
                                    
            #creation of css file
                        print("Do you want the nav bar to stay at top when user scrolls down? ")
                        respondChoice = input("1) Yes\n2) No\n")
                        file = open(css + '.css', 'a')
                        with file as fw:
                            sys.stdout = fw # direct the standard output to the file
                            if respondChoice == '1':
                                print('''.'''+navName+'''{
background-color: '''+bgcolor+'''; /* Black background color */
position: fixed; /* Make it stick/fixed */
top: 0px; /* Hide the navbar 50 px outside of the top view */
width: 100%; /* Full width */
transition: top 0.3s; /* Transition effect when sliding down (and up) */
}

/* Style the navbar links */
.'''+navName+''' a {
'''+linkPos+'''
color: '''+text+''';
text-decoration: none;
}

.'''+navName+''' a:hover {
background-color: '''+hover+''';
color: '''+textHover+''';
}''')



                            else:
                                print('''.'''+navName+''' {
                                        text-align: center;
                                        display: block;
                                        overflow: hidden;
                                        background-color: '''+bgcolor+''';
                            
                                        }
                                        /*nav bar links*/
                                        .'''+navName+''' a{
                                                ''', linkPos+'''
                                                color: ''',text+''';
                                                "
                                                    
                                            }
                                            /*nav hover color*/
                                            .'''+navName+''' a:hover{
                                                    background-color: '''+hover+''';
                                                    color: '''+textHover+''';
                                            }

                                        ''')
                        sys.stdout = original_stdout #redirects output to python
                        print("completed css")
                        loop = 0

                elif answer == 2:
                    navName = input("First, name the navigation bar container: ")
                    linkAmount = int(input("How many links would you like to include: "))
                    #creation of html file
                    file = open(html + '.html', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''<div class="''',navName+'''">''')
                        sys.stdout = original_stdout #redirects output to python
                        i = 0
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

                        bgcolor = input("What color would you lke the navigation bar to be: ")
                        text = input("What color should the text be: ")
                        textHover = input("What color should the text turn when user is hovering over it: ")

                        file = open(css + '.css', 'a')
                        with file as fw:
                            sys.stdout = fw # direct the standard output to the file
                            print('''.'''+navName+''' {
  height: 100%;
  width: 160px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: '''+bgcolor+''';
  overflow-x: hidden;
  padding-top: 20px;
}

.'''+navName+''' a {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  font-size: 25px;
  color: '''+text+''';
  display: block;
}

.'''+navName+''' a:hover {
  color: '''+textHover+''';
}

@media screen and (max-height: 450px) {
  .'''+navName+''' {padding-top: 15px;}
  .'''+navName+''' a {font-size: 18px;}
}


''')

                            sys.stdout = original_stdout #redirects output to python
                        print("completed css")

                    loop = 0

                elif answer == 3:
                    print("You have selected NO\n")
                    loop = 0
                #error check
                else:
                    print("Invalid answer. Enter 1 for yes or 2 for no.\n")
                    loop = 1

        elif choice == 3:
            #================================================================================================================
            #question 3
            #start of my if loops
            loop = 1
            while loop ==1:
                original_stdout = sys.stdout
                print("Would you like to create an image at the top?\nAnswer with 1 or 2 or 3 or 4?\n")
                answer = int(input("1) 1 Image\n2) 2 Images\n3) 3 Images\n4) NONE\n"))

                if answer == 1:
                    name = input("First, name the image container: ")
                    image = input("Enter name of jpg image: ")
                    height = input("What height do you want the image to be. e.g.500px,  550px for full page: ")
                    height = height.replace('px', '')
                    width = int(input("What width do you want the image to be.\n1. Full page\n2. Half page\n "))
                    miniloop = 1
                    while miniloop == 1:
                        if width ==1:
                            width = "100%"
                            miniloop = 0
                        elif width == 2:
                            width = "50%"
                            miniloop = 0
                        else:
                            print("Please choose from 1 or 2...\n")
                            miniloop = 1

                    head = input("Enter image header text: ")
                    subHead = input("Enter image sub header text: ")
                    color = input("What color would you like the text in image: ")
                    textPosition = input("Would you like the text to be:\n1. Centered\n2. Bottom left\n3. Bottom right\n4. Top left\n5. Top right\n")
                    textPosLoop = 1
                    while textPosLoop == 1:
                        if textPosition == "1":
                            textPosition = "top: 50%;\nleft: 50%;"
                            textPosLoop = 0
                        elif textPosition == "2":
                            textPosition = "top: 70%;\nleft: 20%;"
                            textPosLoop = 0
                        elif textPosition == "3":
                            textPosition = "top: 70%;\nleft: 70%;"
                            textPosLoop = 0
                        elif textPosition == "4":
                            textPosition = "top: 20%;\nleft: 20%;"
                            textPosLoop = 0
                        elif textPosition == "5":
                            textPosition = "top: 20%;\nleft: 70%;"
                            textPosLoop = 0
                        else:
                            print("Invalid Answer!\n")
                            textPosition = input("Would you like the text to be:\n1. Centered\n2. Bottom left\n3. Bottom right\n4. Top left\n5. Top right\n")
                    
                            textPosLoop = 1
                            
            #creation of html file
                    file = open(html + '.html', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''<div class="'''+name+'''">
             <div class="'''+name+'''-text">
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
                        print('''.'''+name+'''{
                    float: center;
            background: url('''+image+'''.jpg) no-repeat center;
            background-size: cover;
            height:''',height+'''px;
            width: ''',width+''';
            margin: auto;
            position: relative;
            }
            .'''+name+'''-text{
            text-align: center;
            position: absolute;
            
            '''+textPosition+'''
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

        elif choice == 4:
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
                    grad = int(input("Would you like to create a gradient background colour that changes when the user scrolls?\n1)Yes\n2)No\n"))
                    if grad == 1:
                        grad1 = input("There are 3 points in a gradient.\nWhat colour do you want point 1: ")
                        grad2 = input("What colour would you like point 2: ")
                        grad3 = input("What colour would you like point 3: ")
                    else:
                        color = input("What background color would you like for columns: ")

                    text = input("What color do you want the text to be: ")
                    image = int(input("Would you like to add an image to the column?\n1) Yes\n2)No\n"))
                    imgName = ""
                    imgPos = 0
                    if image == 1:
                        imgName = input("Enter name of JPG image: ")
                        imgPos = int(input("Where do you want to position the image?\n1)Left\n2)Right\n3)Top-Centre\n4)Bottom-Centre\n"))
            #creation of html file
                    file = open(html + '.html', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        if imgPos == 1:
                            if grad == 1:
                                 print(''' <div class="column middle" style="background: linear-gradient(141deg, '''+grad1+''' 0%, '''+grad2+''' 51%, '''+grad3+''' 75%);">
                    <h2>''',header+'''</h2>
                    <p><img src="'''+imgName+'''.jpg" alt="'''+imgName+'''">''',para+'''</p></div>
                    ''')

                            else:
                                print(''' <div class="column middle" style="background-color:''',color+''';">
                    <h2>''',header+'''</h2>
                    <p><img src="'''+imgName+'''.jpg" alt="'''+imgName+'''">''',para+'''</p></div>
                    ''')
                        elif imgPos == 2:
                            if grad == 1:
                                print(''' <div class="column middle" style="background: linear-gradient(141deg, '''+grad1+''' 0%, '''+grad2+''' 51%, '''+grad3+''' 75%);">
                    <h2>''',header+'''</h2>
                    <p>''',para+'''<img src="'''+imgName+'''.jpg" alt="'''+imgName+'''" ></p></div>
                    ''')

                            else:
                                print(''' <div class="column middle" style="background-color:''',color+''';">
                    <h2>''',header+'''</h2>
                    <p>''',para+'''<img src="'''+imgName+'''.jpg" alt="'''+imgName+'''" ></p></div>
                    ''')
                        elif imgPos == 3:
                            if grad == 1:
                                print(''' <div class="column middle" style="background: linear-gradient(141deg, '''+grad1+''' 0%, '''+grad2+''' 51%, '''+grad3+''' 75%);">
                    <h2>''',header+'''</h2>
                    <img src="'''+imgName+'''.jpg" alt="'''+imgName+'''" >
                    <p>''',para+'''</p></div>
                    ''')

                            else:
                                print(''' <div class="column middle" style="background-color:''',color+''';">
                    <h2>''',header+'''</h2>
                    <img src="'''+imgName+'''.jpg" alt="'''+imgName+'''" >
                    <p>''',para+'''</p></div>
                    ''')
                        elif imgPos == 4:
                            if grad == 1:
                                print(''' <div class="column middle" style="background: linear-gradient(141deg, '''+grad1+''' 0%, '''+grad2+''' 51%, '''+grad3+''' 75%);">
                    <h2>''',header+'''</h2>
                    <p>''',para+'''</p>
                    <img src="'''+imgName+'''.jpg" alt="'''+imgName+'''" >
                    </div>
                    ''')

                            else:
                                print(''' <div class="column middle" style="background-color:''',color+''';">
                    <h2>''',header+'''</h2>
                    <p>''',para+'''</p>
                    <img src="'''+imgName+'''.jpg" alt="'''+imgName+'''" >
                    </div>
                    ''')
                        else:
                            if grad == 1:
                                print(''' <div class="column middle" style="background: linear-gradient(141deg, '''+grad1+''' 0%, '''+grad2+''' 51%, '''+grad3+''' 75%);">
                    <h2>''',header+'''</h2>
                    <p>''',para+'''</p></div>''')

                            else:
                                print(''' <div class="column middle" style="background-color:''',color+''';">
                    <h2>''',header+'''</h2>
                    <p>''',para+'''</p></div>''')
                                
                    sys.stdout = original_stdout #redirects output to python
                    print("completed html")
                    borderImg = input("If you have a border image enter directory and name: ")
                    
            #creation of css file
                    file = open(css + '.css', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''/* Create one main article */
            .column {
                color: ''',text+''';
              float: center;
              padding: 4px;
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
                    rimage = int(input("Would you like to add an image to the right column?\n1) Yes\n2)No\n"))
                    rimgName = ""
                    rimgPos = 0
                    if rimage == 1:
                        rimgName = input("Enter name of JPG image: ")
                        rimgPos = int(input("Where do you want to position the image?\n1)Left\n2)Right\n3)Top-Centre\n4)Bottom-Centre\n"))
                    header2 = input("Enter header for the left column: ")
                    para2 = input("Enter text for the left column: ")
                    limage = int(input("Would you like to add an image to the right column?\n1) Yes\n2)No\n"))
                    limgName = ""
                    limgPos = 0
                    if limage == 1:
                        limgName = input("Enter name of JPG image: ")
                        limgPos = int(input("Where do you want to position the image?\n1)Left\n2)Right\n3)Top-Centre\n4)Bottom-Centre\n"))
                    color = input("What background color would you like for the right column: ")
                    color2 = input("What background color would you like for the left column: ")
                    #creation of html file
                    file = open(html + '.html', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        if rimgage == 1 :
                            #left and right
                            if limage == 1:
                                if limgPos == 1:
                                    if rimgPos == 1:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p><img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p><img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >''',para2+'''</p>
                          </div>
                            ''')
                                    elif rimgPos == 2:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''<img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" ></p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p><img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >''',para2+'''</p>
                          </div>
                            ''')
                                    elif rimgPos == 3:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                            <p>''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p><img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >''',para2+'''</p>
                          </div>
                            ''')
                                    else:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''</p>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p><img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >''',para2+'''</p>
                          </div>
                            ''')

                                elif limgPos == 2:
                                    if rimgPos == 1:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p><img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''<img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" ></p>
                          </div>
                            ''')
                                    elif rimgPos == 2:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''<img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" ></p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''<img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" ></p>
                          </div>
                            ''')
                                    elif rimgPos == 3:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                            <p>''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''<img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" ></p>
                          </div>
                            ''')
                                    else:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''</p>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''<img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" ></p>
                          </div>
                            ''')

                                elif limgPos == 3:
                                    if rimgPos == 1:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p><img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >''',para+'''</p>
                            
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                            <p>''',para2+'''</p>
                          </div>
                            ''')
                                        
                                    elif rimgPos == 2:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''<img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" ></p>
                            
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                            <p>''',para2+'''</p>
                          </div>
                            ''')
                                    elif rimgPos == 3:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                            <p>''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                            <p>''',para2+'''</p>
                          </div>
                            ''')
                                    else:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''</p>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                            <p>''',para2+'''</p>
                          </div>
                            ''')

                                else:
                                    if rimgPos ==1:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p><img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''</p>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                          </div>
                            ''')
                                    elif rimgPos == 2:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''<img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" ></p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''</p>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                          </div>
                            ''')
                                    elif rimgPos == 3:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                            <p>''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''</p>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                          </div>
                            ''')
                                    else:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''</p>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                          </div>
                            ''')
                            #just right
                            else:
                                if rimgPos == 1:
                                    print('''<div id="wrapper">
                    <div id="right" style="background-color:''',color+''';">
                        <h2>''',header+'''</h2>
                        <p><img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >''',para+'''</p>
                      </div>
                      <div id="left" style="background-color:''',color2+''';">
                        <h2>''',header2+'''</h2>
                        <p>''',para2+'''</p>
                      </div>
                        ''')

                                elif rimgPos == 2:
                                    print('''<div id="wrapper">
                    <div id="right" style="background-color:''',color+''';">
                        <h2>''',header+'''</h2>
                        <p>''',para+'''<img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" ></p>
                      </div>
                      <div id="left" style="background-color:''',color2+''';">
                        <h2>''',header2+'''</h2>
                        <p>''',para2+'''</p>
                      </div>
                        ''')

                                elif rimgPos == 3:
                                    print('''<div id="wrapper">
                    <div id="right" style="background-color:''',color+''';">
                        <h2>''',header+'''</h2>
                        <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                        <p>''',para+'''</p>
                      </div>
                      <div id="left" style="background-color:''',color2+''';">
                        <h2>''',header2+'''</h2>
                        <p>''',para2+'''</p>
                      </div>
                        ''')

                                else:
                                    print('''<div id="wrapper">
                    <div id="right" style="background-color:''',color+''';">
                        <h2>''',header+'''</h2>
                        <p>''',para+'''</p>
                        <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                      </div>
                      <div id="left" style="background-color:''',color2+''';">
                        <h2>''',header2+'''</h2>
                        <p>''',para2+'''</p>
                      </div>
                        ''')
                        #start with left
                        elif limage == 1:
                            if rimage == 1:
                                if limgPos == 1:
                                    if rimgPos == 1:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p><img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p><img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >''',para2+'''</p>
                          </div>
                            ''')

                                    elif rimgPos == 2:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''<img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" ></p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p><img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >''',para2+'''</p>
                          </div>
                            ''')

                                    elif rimgPos == 3:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                            <p>''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p><img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >''',para2+'''</p>
                          </div>
                            ''')

                                    else:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''</p>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p><img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >''',para2+'''</p>
                          </div>
                            ''')

                                elif limgPos == 2:
                                    if rimgPos == 1:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p><img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''<img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" ></p>
                          </div>
                            ''')

                                    elif rimgPos == 2:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''<img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" ></p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''<img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" ></p>
                          </div>
                            ''')

                                    elif rimgPos == 3:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                            <p>''',para+'''</p>
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''<img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" ></p>
                          </div>
                            ''')

                                    else:
                                        print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''</p>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                          </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''<img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" ></p>
                          </div>
                            ''')

                                elif limgPos == 3:
                                    if rimgPos == 1:
                                         print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p><img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >''',para+'''</p>
                            </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                            <p>''',para2+'''</p>
                          </div>
                            ''')

                                    elif rimgPos ==2:
                                         print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''<img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" ></p>
                            </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                            <p>''',para2+'''</p>
                          </div>
                            ''')
                                    elif rimgPos == 3:
                                         print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                            <p>''',para+'''</p>
                            </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                            <p>''',para2+'''</p>
                          </div>
                            ''')
                                    else:
                                         print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''</p>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                            </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                            <p>''',para2+'''</p>
                          </div>
                            ''')
                                else:
                                    if rimgPos == 1:
                                         print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p><img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >''',para+'''</p>
                            </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''</p>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                          </div>
                            ''')
                                    elif rimgPos ==2:
                                         print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''<img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" ></p>
                            </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''</p>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                          </div>
                            ''')
                                    elif rimgPos == 3:
                                         print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                            <p>''',para+'''</p>
                            </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''</p>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                          </div>
                            ''')
                                    else:
                                         print('''<div id="wrapper">
                        <div id="right" style="background-color:''',color+''';">
                            <h2>''',header+'''</h2>
                            <p>''',para+'''</p>
                            <img src="'''+rimgName+'''.jpg" alt="'''+rimgName+'''" >
                            </div>
                          <div id="left" style="background-color:''',color2+''';">
                            <h2>''',header2+'''</h2>
                            <p>''',para2+'''</p>
                            <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                          </div>
                            ''')
                                    
                            #just left
                            else:
                                if limgPos == 1:
                                    print('''<div id="wrapper">
                    <div id="right" style="background-color:''',color+''';">
                        <h2>''',header+'''</h2>
                        <p>''',para+'''</p>
                      </div>
                      <div id="left" style="background-color:''',color2+''';">
                        <h2>''',header2+'''</h2>
                        <p><img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >''',para2+'''</p>
                      </div>
                        ''')

                                elif limgPos == 2:
                                    print('''<div id="wrapper">
                    <div id="right" style="background-color:''',color+''';">
                        <h2>''',header+'''</h2>
                        <p>''',para+'''</p>
                      </div>
                      <div id="left" style="background-color:''',color2+''';">
                        <h2>''',header2+'''</h2>
                        <p>''',para2+'''<img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" ></p>
                      </div>
                        ''')

                                elif limgPos == 3:
                                    print('''<div id="wrapper">
                    <div id="right" style="background-color:''',color+''';">
                        <h2>''',header+'''</h2>
                        <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                        <p>''',para+'''</p>
                      </div>
                      <div id="left" style="background-color:''',color2+''';">
                        <h2>''',header2+'''</h2>
                        <p>''',para2+'''</p>
                      </div>
                        ''')

                                else:
                                    print('''<div id="wrapper">
                    <div id="right" style="background-color:''',color+''';">
                        <h2>''',header+'''</h2>
                        <p>''',para+'''</p>
                      </div>
                      <div id="left" style="background-color:''',color2+''';">
                        <h2>''',header2+'''</h2>
                        <p>''',para2+'''</p>
                        <img src="'''+limgName+'''.jpg" alt="'''+limgName+'''" >
                      </div>
                        ''')

                        #No image
                        else:
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


        elif choice == 5:
    #question 5
            #start of my if loops
            loop = 1
            while loop ==1:
                original_stdout = sys.stdout
                print("Would you like to create a Footer for your page?\nAnswer with 1 or 2\n")
                answer = int(input("1) YES \n2) NO \n"))

                if answer == 1:
                    foot = input("What would you like to write in the footer: ")
                    #creation of html file
                    file = open(html + '.html', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''<FOOTER>
    <div class="footer">
    <h1>''',foot+'''</h1>
    </div>
    </FOOTER>
    ''')
                    sys.stdout = original_stdout #redirects output to python
                    print("completed html")
                    bgColor = input("What background color would you like on the footer: ")
                    #creation of css file
                    file = open(css + '.css', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''.footer{

	    background-color: ''',bgColor+''';
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

        elif choice == 6:
            #question 6######################################################################################################################################
            #start of my if loops
            loop = 1
            while loop ==1:
                original_stdout = sys.stdout
                vidName = input("What is the name of your MP4 file?\n")
                vidAlign = input("Do you want it on the left, centre or right?\n1) Left\n2) Centre\n3) Right\n")
                    #creation of html file

                file = open(html + '.html', 'a')
                with file as fw:
                    sys.stdout = fw # direct the standard output to the file
                    if vidAlign == 1:
                        print('''<video width="100%" height ="50%" controls id="myvideo">
      <source src="'''+vidName+'''.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>''')
                    elif vidAlign == 2:
                        print('''<video class ="center" width="50%" height ="50%" controls id="myvideo">
      <source src="'''+vidName+'''.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>''')
                    elif vidAlign == 3:
                        print('''<video class ="right" width="50%" height ="50%" controls id="myvideo">
      <source src="'''+vidName+'''.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>''')
                    else:
                        print('''<video class ="center" width="50%" height ="50%" controls id="myvideo">
      <source src="'''+vidName+'''.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>''')
                        
                    sys.stdout = original_stdout #redirects output to python
                    print("completed html")
                    #creation of css file
                    file = open(css + '.css', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''.center {
    margin-left: auto;
    margin-right: auto;
    display: block
}

.right {
    float: right
}
    ''')
                    sys.stdout = original_stdout #redirects output to python
                    print("completed css\n")

                    loop = 0
            

        elif choice == 10:
    #question 10
            #start of my if loops
            loop = 1
            while loop ==1:
                original_stdout = sys.stdout
                print("How many tabs do you want?\n")
                answer = int(input("1) 1 \n2)2 \n3) 3\n 4) 4\n"))

                if answer == 1:
                    tabContainer1 = input("FIRST name the container of the tab: ")
                    tabColour1 = input("What colour would you like the tab button to be: ")
                    tabName1 = input("What would you like to title the tab: ")
                    tabContent1 = input("What would you like to write in the tab: ")
                    #creation of html file
                    file = open(html + '.html', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''<button class="'''+tabContainer1+'''" onclick="openPage(\''''+tabName1+'''\', this, \'''',tabColour1+'''\')\">''',tabName1, '''</button>''')
                        print('''<div id =\"'''+tabName1+'''\" class=\"tabcontent\">
<h3>''',tabName1+'''</h3>
<p>''',tabContent1+'''</p>
</div>''')
                        
                    sys.stdout = original_stdout #redirects output to python
                    print("completed html")
                    #creation of css file
                    file = open(css + '.css', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''/* Set height of body and the document to 100% to enable "full page tabs" */
body, html {
  height: 100%;
  margin: 0;
  font-family: Arial;
}

/* Style tab links */
.'''+tabContainer1+'''{
  background-color: #555;
  color: white;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  font-size: 17px;
  width: 100%;
}

.'''+tabContainer1+''':hover {
  background-color: #777;
}

/* Style the tab content (and add height:100% for full page content) */
.tabcontent {
  color: white;
  display: none;
  padding: 100px 20px;
  height: 100%;
}

#'''+tabName1+''' {background-color:''', tabColour1+''';}
    ''')
                    sys.stdout = original_stdout #redirects output to python
                    print("completed css\n")


                    file = open(css + '.js', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''function openPage(pageName, elmnt, color) {
  // Hide all elements with class="tabcontent" by default */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(pageName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
                        ''')
                        sys.stdout = original_stdout #redirects output to python
                        print("completed js\n")
        
                        loop = 0

                elif answer == 2:
                    tabContainer1 = input("FIRST name the container of the tabs: ")
                    tabColour1 = input("What colour would you like the FIRST tab button to be: ")
                    tabName1 = input("What would you like to title the FIRST tab: ")
                    tabContent1 = input("What would you like to write in the FIRST tab: ")
                    tabColour2 = input("What colour would you like the SECOND tab button to be: ")
                    tabName2 = input("What would you like to title the SECOND tab: ")
                    tabContent2 = input("What would you like to write in the SECOND tab: ")

                    #creation of html file
                    file = open(html + '.html', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''<button class="'''+tabContainer1+'''" onclick="openPage(\''''+tabName1+'''\', this, \'''',tabColour1+'''\')\">''',tabName1, '''</button>''')
                        print('''<button class="'''+tabContainer1+'''" onclick="openPage(\''''+tabName2+'''\', this, \'''',tabColour2+'''\')\">''',tabName2, '''</button>''')
                        
                        print('''<div id =\"'''+tabName1+'''\" class=\"tabcontent\">
<h3>''',tabName1+'''</h3>
<p>''',tabContent1+'''</p>
</div>''')
                        print('''<div id =\"'''+tabName2+'''\" class=\"tabcontent\">
<h3>''',tabName2+'''</h3>
<p>''',tabContent2+'''</p>
</div>''')
                        
                    sys.stdout = original_stdout #redirects output to python
                    print("completed html")
                    #creation of css file
                    file = open(css + '.css', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''/* Set height of body and the document to 100% to enable "full page tabs" */
body, html {
  height: 100%;
  margin: 0;
  font-family: Arial;
}

/* Style tab links */
.'''+tabContainer1+''' {
  background-color: #555;
  color: white;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  font-size: 17px;
  width: 50%;
}

.'''+tabContainer1+''':hover {
  background-color: #777;
}

/* Style the tab content (and add height:100% for full page content) */
.tabcontent {
  color: white;
  display: none;
  padding: 100px 20px;
  height: 100%;
}

#'''+tabName1+''' {background-color:''', tabColour1+''';}
#'''+tabName2+''' {background-color:''', tabColour2+''';}
    ''')
                    sys.stdout = original_stdout #redirects output to python
                    print("completed css\n")


                    file = open(css + '.js', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''function openPage(pageName, elmnt, color) {
  // Hide all elements with class="tabcontent" by default */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(pageName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
                        ''')
                        sys.stdout = original_stdout #redirects output to python
                        print("completed js\n")
        
                        loop = 0
                        
                elif answer == 3:
                    tabContainer1 = input("FIRST name the container of the tabs: ")
                    tabColour1 = input("What colour would you like the FIRST tab button to be: ")
                    tabName1 = input("What would you like to title the FIRST tab: ")
                    tabContent1 = input("What would you like to write in the FIRST tab: ")
                    tabColour2 = input("What colour would you like the SECOND tab button to be: ")
                    tabName2 = input("What would you like to title the SECOND tab: ")
                    tabContent2 = input("What would you like to write in the SECOND tab: ")
                    tabColour3 = input("What colour would you like the THIRD tab button to be: ")
                    tabName3 = input("What would you like to title the THIRD tab: ")
                    tabContent3 = input("What would you like to write in the THIRD tab: ")

                    #creation of html file
                    file = open(html + '.html', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''<button class="'''+tabContainer1+'''" onclick="openPage(\''''+tabName1+'''\', this, \'''',tabColour1+'''\')\">''',tabName1, '''</button>''')
                        print('''<button class="'''+tabContainer1+'''" onclick="openPage(\''''+tabName2+'''\', this, \'''',tabColour2+'''\')\">''',tabName2, '''</button>''')
                        print('''<button class="'''+tabContainer1+'''" onclick="openPage(\''''+tabName3+'''\', this, \'''',tabColour3+'''\')\">''',tabName3, '''</button>''')
                        
                        print('''<div id =\"'''+tabName1+'''\" class=\"tabcontent\">
<h3>''',tabName1+'''</h3>
<p>''',tabContent1+'''</p>
</div>''')
                        print('''<div id =\"'''+tabName2+'''\" class=\"tabcontent\">
<h3>''',tabName2+'''</h3>
<p>''',tabContent2+'''</p>
</div>''')
                        print('''<div id =\"'''+tabName3+'''\" class=\"tabcontent\">
<h3>''',tabName3+'''</h3>
<p>''',tabContent3+'''</p>
</div>''')
                    sys.stdout = original_stdout #redirects output to python
                    print("completed html")
                    #creation of css file
                    file = open(css + '.css', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''/* Set height of body and the document to 100% to enable "full page tabs" */
body, html {
  height: 100%;
  margin: 0;
  font-family: Arial;
}

/* Style tab links */
.'''+tabContainer1+''' {
  background-color: #555;
  color: white;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  font-size: 17px;
  width: 33%;
}

.'''+tabContainer1+''':hover {
  background-color: #777;
}

/* Style the tab content (and add height:100% for full page content) */
.tabcontent {
  color: white;
  display: none;
  padding: 100px 20px;
  height: 100%;
}

#'''+tabName1+''' {background-color:''', tabColour1+''';}
#'''+tabName2+''' {background-color:''', tabColour2+''';}
#'''+tabName3+''' {background-color:''', tabColour3+''';}
    ''')
                    sys.stdout = original_stdout #redirects output to python
                    print("completed css\n")


                    file = open(css + '.js', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''function openPage(pageName, elmnt, color) {
  // Hide all elements with class="tabcontent" by default */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(pageName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
                        ''')
                        sys.stdout = original_stdout #redirects output to python
                        print("completed js\n")
        
                        loop = 0

                elif answer == 4:
                    tabContainer1 = input("FIRST name the container of the tabs: ")
                    tabColour1 = input("What colour would you like the FIRST tab button to be: ")
                    tabName1 = input("What would you like to title the FIRST tab: ")
                    tabContent1 = input("What would you like to write in the FIRST tab: ")
                    tabColour2 = input("What colour would you like the SECOND tab button to be: ")
                    tabName2 = input("What would you like to title the SECOND tab: ")
                    tabContent2 = input("What would you like to write in the SECOND tab: ")
                    tabColour3 = input("What colour would you like the THIRD tab button to be: ")
                    tabName3 = input("What would you like to title the THIRD tab: ")
                    tabContent3 = input("What would you like to write in the THIRD tab: ")
                    tabColour4 = input("What colour would you like the THIRD tab button to be: ")
                    tabName4 = input("What would you like to title the THIRD tab: ")
                    tabContent4 = input("What would you like to write in the THIRD tab: ")

                    #creation of html file
                    file = open(html + '.html', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''<button class="'''+tabContainer1+'''" onclick="openPage(\''''+tabName1+'''\', this, \'''',tabColour1+'''\')\">''',tabName1, '''</button>''')
                        print('''<button class="'''+tabContainer1+'''" onclick="openPage(\''''+tabName2+'''\', this, \'''',tabColour2+'''\')\">''',tabName2, '''</button>''')
                        print('''<button class="'''+tabContainer1+'''" onclick="openPage(\''''+tabName3+'''\', this, \'''',tabColour3+'''\')\">''',tabName3, '''</button>''')
                        print('''<button class="'''+tabContainer1+'''" onclick="openPage(\''''+tabName4+'''\', this, \'''',tabColour4+'''\')\">''',tabName4, '''</button>''')

                        print('''<div id =\"'''+tabName1+'''\" class=\"tabcontent\">
<h3>''',tabName1+'''</h3>
<p>''',tabContent1+'''</p>
</div>''')
                        print('''<div id =\"'''+tabName2+'''\" class=\"tabcontent\">
<h3>''',tabName2+'''</h3>
<p>''',tabContent2+'''</p>
</div>''')
                        print('''<div id =\"'''+tabName3+'''\" class=\"tabcontent\">
<h3>''',tabName3+'''</h3>
<p>''',tabContent3+'''</p>
</div>''')

                        print('''<div id =\"'''+tabName4+'''\" class=\"tabcontent\">
<h3>''',tabName4+'''</h3>
<p>''',tabContent4+'''</p>
</div>''')
                    sys.stdout = original_stdout #redirects output to python
                    print("completed html")
                    #creation of css file
                    file = open(css + '.css', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''/* Set height of body and the document to 100% to enable "full page tabs" */
body, html {
  height: 100%;
  margin: 0;
  font-family: Arial;
}

/* Style tab links */
.'''+tabContainer1+''' {
  background-color: #555;
  color: white;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  font-size: 17px;
  width: 25%;
}

.'''+tabContainer1+''':hover {
  background-color: #777;
}

/* Style the tab content (and add height:100% for full page content) */
.tabcontent {
  color: white;
  display: none;
  padding: 100px 20px;
  height: 100%;
}

#'''+tabName1+''' {background-color:''', tabColour1+''';}
#'''+tabName2+''' {background-color:''', tabColour2+''';}
#'''+tabName3+''' {background-color:''', tabColour3+''';}
#'''+tabName4+''' {background-color:''', tabColour4+''';}
    ''')
                    sys.stdout = original_stdout #redirects output to python
                    print("completed css\n")


                    file = open(css + '.js', 'a')
                    with file as fw:
                        sys.stdout = fw # direct the standard output to the file
                        print('''function openPage(pageName, elmnt, color) {
  // Hide all elements with class="tabcontent" by default */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(pageName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
                        ''')
                        sys.stdout = original_stdout #redirects output to python
                        print("completed js\n")
        
                        loop = 0


#question 11
        elif choice == 11:
                    #start of my if loops
                    loop = 1
                    while loop ==1:
                        original_stdout = sys.stdout
                        print("How many images do you want?\n")
                        answer = int(input("1) 1 \n2) 2 \n3) 3\n 4) 4\n"))
                        if answer == 1:
                            imageFile1 = input("What is the name of the JPG file? ")
                            imageText1 = input("What would you like to write for the caption: ")
                                    
                            #creation of html file
                            file = open(html + '.html', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <img src="'''+imageFile1+'''.jpg" style="width:100%">
    <div class="text">'''+imageText1+'''</div></div>
  </div>''')
                                        
                            sys.stdout = original_stdout #redirects output to python
                            print("completed html")
                            #creation of css file
                            file = open(css + '.css', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Hide the images by default */
.mySlides {
  display: none;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}
                    ''')
                            sys.stdout = original_stdout #redirects output to python
                            print("completed css\n")


                            file = open(css + '.js', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
                                        ''')
                                sys.stdout = original_stdout #redirects output to python
                                print("completed js\n")
                        
                                loop = 0
                        if answer == 2:
                            imageFile1 = input("What is the name of the FIRST JPG file? ")
                            imageText1 = input("What would you like to write for the caption: ")
                            imageFile2 = input("What is the name of the SECOND JPG file? ")
                            imageText2 = input("What would you like to write for the caption: ")
                                
                            #creation of html file
                            file = open(html + '.html', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <div class="numbertext">1 / 2</div>
    <img src="'''+imageFile1+'''.jpg" style="width:100%">
    <div class="text">'''+imageText1+'''</div>
  </div>
  <div class="mySlides fade">
    <div class="numbertext">2 / 2</div>
    <img src="'''+imageFile2+'''.jpg" style="width:100%">
    <div class="text">'''+imageText2+'''</div>
  </div>
<!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
<br>

<!-- The dots/circles -->
<div style="text-align:center">
  <span class="dot" onclick="currentSlide(1)"></span>
  <span class="dot" onclick="currentSlide(2)"></span>
</div></div>''')                                
                                        
                            sys.stdout = original_stdout #redirects output to python
                            print("completed html")
                            #creation of css file
                            file = open(css + '.css', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Hide the images by default */
.mySlides {
  display: none;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}

@keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}
                    ''')
                            sys.stdout = original_stdout #redirects output to python
                            print("completed css\n")


                            file = open(css + '.js', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
                                        ''')
                                sys.stdout = original_stdout #redirects output to python
                                print("completed js\n")
                        
                                loop = 0

                        if answer == 3:
                            imageFile1 = input("What is the name of the FIRST JPG file? ")
                            imageText1 = input("What would you like to write for the caption: ")
                            imageFile2 = input("What is the name of the SECOND JPG file? ")
                            imageText2 = input("What would you like to write for the caption: ")
                            imageFile3 = input("What is the name of the THIRD JPG file? ")
                            imageText3 = input("What would you like to write for the caption: ")
                                
                            #creation of html file
                            file = open(html + '.html', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <div class="numbertext">1 / 3</div>
    <img src="'''+imageFile1+'''.jpg" style="width:100%">
    <div class="text">'''+imageText1+'''</div>
  </div>
  <div class="mySlides fade">
    <div class="numbertext">2 / 3</div>
    <img src="'''+imageFile2+'''.jpg" style="width:100%">
    <div class="text">'''+imageText2+'''</div>
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 3</div>
    <img src="'''+imageFile3+'''.jpg" style="width:100%">
    <div class="text">'''+imageText3+'''</div>
  </div>
<!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
<br>

<!-- The dots/circles -->
<div style="text-align:center">
  <span class="dot" onclick="currentSlide(1)"></span>
  <span class="dot" onclick="currentSlide(2)"></span>
  <span class="dot" onclick="currentSlide(3)"></span>
</div></div>''')                                
                                        
                            sys.stdout = original_stdout #redirects output to python
                            print("completed html")
                            #creation of css file
                            file = open(css + '.css', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Hide the images by default */
.mySlides {
  display: none;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}

@keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}
                    ''')
                            sys.stdout = original_stdout #redirects output to python
                            print("completed css\n")


                            file = open(css + '.js', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
                                        ''')
                                sys.stdout = original_stdout #redirects output to python
                                print("completed js\n")
                        
                                loop = 0

                        if answer == 4:
                            imageFile1 = input("What is the name of the FIRST JPG file? ")
                            imageText1 = input("What would you like to write for the caption: ")
                            imageFile2 = input("What is the name of the SECOND JPG file? ")
                            imageText2 = input("What would you like to write for the caption: ")
                            imageFile3 = input("What is the name of the THIRD JPG file? ")
                            imageText3 = input("What would you like to write for the caption: ")
                            imageFile4 = input("What is the name of the FOURTH JPG file? ")
                            imageText4 = input("What would you like to write for the caption: ")
                                
                            #creation of html file
                            file = open(html + '.html', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <div class="numbertext">1 / 4</div>
    <img src="'''+imageFile1+'''.jpg" style="width:100%">
    <div class="text">'''+imageText1+'''</div>
  </div>
  <div class="mySlides fade">
    <div class="numbertext">2 / 4</div>
    <img src="'''+imageFile2+'''.jpg" style="width:100%">
    <div class="text">'''+imageText2+'''</div>
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 4</div>
    <img src="'''+imageFile3+'''.jpg" style="width:100%">
    <div class="text">'''+imageText3+'''</div>
  </div>
  <div class="mySlides fade">
    <div class="numbertext">4 / 4</div>
    <img src="'''+imageFile4+'''.jpg" style="width:100%">
    <div class="text">'''+imageText4+'''</div>
  </div>
<!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
<br>

<!-- The dots/circles -->
<div style="text-align:center">
  <span class="dot" onclick="currentSlide(1)"></span>
  <span class="dot" onclick="currentSlide(2)"></span>
  <span class="dot" onclick="currentSlide(3)"></span>
  <span class="dot" onclick="currentSlide(4)"></span>
</div></div>''')                                
                                        
                            sys.stdout = original_stdout #redirects output to python
                            print("completed html")
                            #creation of css file
                            file = open(css + '.css', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''* {box-sizing: border-box}
body {font-family: Verdana, sans-serif; margin:0}
.mySlides {display: none}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -22px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .prev, .next,.text {font-size: 11px}
}
                    ''')
                            sys.stdout = original_stdout #redirects output to python
                            print("completed css\n")


                            file = open(css + '.js', 'a')
                            with file as fw:
                                sys.stdout = fw # direct the standard output to the file
                                print('''let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
                                        ''')
                                sys.stdout = original_stdout #redirects output to python
                                print("completed js\n")
                        
                                loop = 0




            #error check

                        else:
                            print("Invalid answer. Try again.\n")
                            loop = 1



        elif choice == 0:
            if platform.system() == 'Darwin':       # macOS
                subprocess.call(('open', html+'.html'))
            elif platform.system() == 'Windows':    # Windows
                os.startfile(html+'.html')
            else:                                   # linux variants
                subprocess.call(('xdg-open', html+'.html'))
    else:
            loop = 1
