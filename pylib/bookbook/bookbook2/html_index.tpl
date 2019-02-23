<!DOCTYPE html>
<html>
<head>
    <title>Table of Contents</title>
<style>
body {
    font-family: sans-serif;
}
</style>
</head>

<body>
<h1>Table of Contents</h1>
<ul>
    {% for entry in index_entries %}
    <li>{{ entry.chapter_no }}: <a href="{{ entry.filename }}">{{ entry.title }}</a></li>
    {% endfor %}
</ul>
</body>
</html>
