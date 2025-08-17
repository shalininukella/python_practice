class Mother:
    def skill(self):
        print("High IQ")

class Father:
    def grateful(self):
        print("Great")

class Me (Father, Mother):
    def quality(self):
        print("Bhagvan ki kripa")

me = Me()
me.quality()
me.skill()
me.grateful()