f = open("raw_html.txt", "r")
text = f.read().splitlines()
parsed = [] # [[paragraph1, paragraph2, ...{pg1}], [paragraph1, paragraph2, ...{pg2}], ...]

START1 = '<div style="position:absolute;left:50%'
START2 = '<div style="position:absolute;left:0px'

last_indent = ''
paragraph = ''
page = []
for line in text:
    if START1 in line or START2 in line or '<img' in line:
        continue
    if line == '</div>':
        page.append(paragraph)
        parsed.append(page)
        page = []
        paragraph = ''
    else:
        start = line.find('span') + 21
        end = line.find('</span>')
        indent = float(line[35:line.find('px')])
        if not last_indent or last_indent == indent or last_indent + 9 == indent:
            paragraph += line[start:end]
        else:
            page.append(paragraph)
            paragraph = line[start:end]

        last_indent = indent
        line = line[end + 7:]
        if 'HREF' in line:
            link = line[line.find('<A'):line.find('</A>') + 4]
            paragraph += link
            line = line[line.find('</A>') + 4:]
        if 'span' in line:
            paragraph += line[line.find('span') + 21:line.find('<A')]
            line = line[line.find('<A'):]
        if 'HREF' in line:
            link = line[line.find('<A'):line.find('</A>') + 4]
            paragraph += link
            line = line[line.find('</A>') + 4:]
        paragraph += line[:line.find('</div>')] + ' '

o = open("parsed_html.txt", "w")
for page in parsed:
    for paragraph in page:
        o.write(paragraph + "\n\n")
    o.write("\n\n\n\n")
o.close()
