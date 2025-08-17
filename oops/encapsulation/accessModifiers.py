class Test:
    def __init__(self):
        self.a = 10      # public
        self._b = 20     # protected
        self.__c = 30    # private

t = Test()
print(t.a)    # ✅ 10
print(t._b)   # ⚠️ Accessible, but by convention should not
# print(t.__c)  # ❌ AttributeError
print(t._Test__c)  # ✅ 30 (name mangling)



 