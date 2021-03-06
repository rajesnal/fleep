import fleep

with open("testfile", "rb") as file:
    info = fleep.get(file.read(128))

assert info.type == ["image"]
assert info.extension == ["png"]
assert info.mime == ["image/png"]

assert info.type_matches("image")
assert info.extension_matches("png")
assert info.mime_matches("image/png")
