import wikipedia

print(wikipedia.search("Github", results = 5, suggestion = True))

print(wikipedia.summary("Sukhoi 30 MKI"))

wikipedia.set_lang('sa') #bn, hi, sa(sanskrit), zh(chinese)
print(wikipedia.summary("Physics"))

print(wikipedia.languages()["sa"])

wikipedia.set_lang('en')
spetsnaz = wikipedia.page("Spetsnaz")
print(f"Title - {spetsnaz.title} | URL - {spetsnaz.url}"+"\n"+f"{spetsnaz.content}"+"\n"+f"{spetsnaz.images}")