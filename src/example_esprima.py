import esprima

program = """
function hello() {
    console.log("Hello World")
}
"""

result = esprima.parseScript(program)
print(result)

