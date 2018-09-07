class GrumpyDict(dict):
    def __missing__(self, key):
        print(f"key: {key} is not found")

data = GrumpyDict({"first":1,"second":2})
data["third"] = "4"
print(data["fourth"])
