template1 = '''<html lang="en">
<head>
  <!-- Global site tag (gtag.js) - Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-166953877-2"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'UA-166953877-2');
  </script>
  <meta charset="utf-8">

  <title>Religion and the Absurd</title>
  <meta name="description" content="Religion and the Absurd">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="../styles.css">

</head>

<body>
  <div class="section_header">
    <a href="../index.html" class="left">Back to Table of Contents</a>
    <div class="audio">
      <span class="page_title">'''

template15 = '''</span>
      <button class="btn right_icon"><i class="fa fa-file-audio-o icon"></i></button>
    </div>
  </div>
  <div class="text_body">\n'''

span1 = '    <span class="paragraph">\n'
span2 = '\n    </span>\n'
span3 = '    <span class="end paragraph">\n'

template2 = '''  </div>
  <div class="bottom_nav">\n'''

tag1 = '    <a href="00'
tag2 = '.html" class="left">Previous Section</a>\n'
tag3 = '    <a href="0'
tag4 = '.html" class="right">Next Section</a>\n'

template3 = '''  </div>
</body>
</html>\n'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list(range(9, 21)) + list(range(25, 49)) + list(range(50, 67))

o = open("resources/cleaned_html.txt", "r")
text = o.read().splitlines()

for i in range(1, 9):
    j = list1[i]
    f = open("pages/00" + str(j) + ".html", "w")
    f.write(template1)
    f.write(text[0])
    text = text[1:]
    f.write(template15)
    while '~~~~~~~' not in text[0]:
        line = text[0]
        if line:
            f.write(span1)
            f.write("      " + line)
            f.write(span2)
        text = text[1:]
    if '~~~~~~~' in text[0]:
        f.write(span3)
        f.write("      " + text[0])
        f.write(span2)
        text = text[2:]
    f.write(template2)
    f.write(tag1)
    f.write(str(list1[i-1]))
    f.write(tag2)
    f.write(tag1)
    f.write(str(list1[i+1]))
    f.write(tag4)
    f.write(template3)
    f.close()

for i in range(1, len(list2)-1):
    j = list2[i]
    f = open("pages/0" + str(j) + ".html", "w")
    f.write(template1)
    f.write(text[0])
    text = text[1:]
    f.write(template15)
    while '~~~~~~~' not in text[0]:
        line = text[0]
        if line:
            f.write(span1)
            f.write("      " + line)
            f.write(span2)
        text = text[1:]
    if '~~~~~~~' in text[0]:
        f.write(span3)
        f.write("      " + text[0])
        f.write(span2)
        text = text[2:]
    f.write(template2)
    f.write(tag3)
    f.write(str(list2[i-1]))
    f.write(tag2)
    f.write(tag3)
    f.write(str(list2[i+1]))
    f.write(tag4)
    f.write(template3)
    f.close()
