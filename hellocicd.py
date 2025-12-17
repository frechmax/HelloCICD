import datetime

now = datetime.datetime.now()
html_content = f"""
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>Hello World</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Timestamp: {now}</p>
</body>
</html>
"""

with open('output/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
