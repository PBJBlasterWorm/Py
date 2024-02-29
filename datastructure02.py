ProgramLanguage = ["C언어","C++","JAVA","Java Script"]
ProgramBook = ["C언어 길라잡이","Do it! JAVA"]

ProgramLanguage += ProgramBook # extend

print(ProgramLanguage)

del ProgramLanguage[2]
print(ProgramLanguage)

del ProgramLanguage[ProgramLanguage.index("C++")]
print(ProgramLanguage)

ProgramLanguage.clear() #ProgramLanguage = []
print(ProgramLanguage)