import base64
data = open('test_face.jpg','rb').read()
data = base64.b64encode(data).decode("utf8")
print(data)