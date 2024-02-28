from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html>
<head>
<title>Example Page</title>
</head>
<body>
<h1>Example Heading</h1>
<h2>Hello World!</h2>
<p>This is an example paragraph.</p>
<p class="example_class">This is an example paragraph with a class.</p>
<p id="example_id">This is an example paragraph with an ID.</p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
print("-----")
print(soup.find('p'))
print("-----")
print(soup.find('p', id='example_id'))
print("-----")
print(soup.find_all('p'))
print("-----")

