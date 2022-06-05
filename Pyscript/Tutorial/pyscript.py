def increase_value(*args):
    element = Element('output').element
    content = int(element.textContent)
    content += 1
    element.innerHTML = content
    # pyscript.write('output', content)