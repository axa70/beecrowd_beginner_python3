'''code_input = ""

while True:
    line = input()
    if line == "":
        break
    code_input += line

start_body = code_input.find("<body>")
#print(f"Start = {start_body}")
end_body = code_input.find("</body>")
#print(f"End = {end_body}")

body_content = code_input[start_body + len("<body>") : end_body]
print(body_content)'''

#solved by chatgpt
body = False

while True:
    try:
        string = input()
    except EOFError:
        break

    if "<body>" in string:
        body = True
        continue

    if body and "</body>" in string:
        body = False

    if body:
        print(string)
