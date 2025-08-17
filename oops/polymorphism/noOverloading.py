class Example:
    def hello(self, name):
        print("Hello", name)

    def hello(self, name, age):  # overwrites the first one
        print("Hello", name, "you are", age)

obj = Example()
# obj.hello("Shalini")  # ❌ Error: missing argument
obj.hello("Shalini", 22)  # ✅ Works
