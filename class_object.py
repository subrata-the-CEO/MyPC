#class Education:
#    def __init__(self,school) -> str:
#        self.edu = school
#e = Education(school="Swami Vivekanda Institute of Science and Technology")
#print(e.edu)

class NameOfOwner:
    def __init__(self,owner) -> str:
        self.owner = owner
    def breakdown(self):
        for i in self.owner:
            print(i)
o = NameOfOwner(owner= "EdTech Academy")
print(o.owner)
o.breakdown()