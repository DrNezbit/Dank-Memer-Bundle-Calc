BUNDLES=[] # Placeholder list

# Example bundle:
## To add more simply copy and paste between ### rows
## replacing text in """ with pasted text from /bundle embed

#####################################################
bundle=\
"""

> <a:CollectorBadge:923306151486046239> **Collector Badge**
> <:PB1C:1067896242845270036><:PB2C:1067896253502992484><:PB2HF:1067896246599155752><:PB2E:1067894185597882419><:PB3E:1067894195504820294> ` 54% `

**Level Leviathan** [(not completed)](https://www.youtube.com/watch?v=D6Pf55CjDos)
<:ReplyCont:870764844012412938> <:CX:1071484097957994587> ` 10/35 ` <:jokeBook:1186704670559830086> Joke Book
<:Reply:870665583593660476> <:CX:1071484097957994587> ` 4/25 ` <a:petFeeder:1186720980631031868> Pet Feeder

"""
BUNDLES.append(bundle) # Adds bundle to list of BUNDLES
#####################################################

# Bundle Class
class Bundle:
	def __init__(self, bundle_str):
		self.name,text=self.get_name(bundle_str)
		self.lines=self.calculate(self.build_list(text))
		
	def get_name(self, bundle_text: str):
		text=bundle_text.split(" <:CX:1071484097957994587> ")
		removed=text.pop(0)
		name=removed.split("\n")[-2]
		name="### "+name.split("[")[0]
		return name,text
		
	def build_list(self,text):
		lines=[]
		for line in text:
			line=line.split("\n")[0].split(" ")
			for word in line:
				if word.startswith("<") and word.endswith(">"):
					line.remove(word)
			lines.append(" ".join(line))
		return lines
		
	def calculate(self,lines):
		new_lines=[]
		for line in lines:
			line=line.replace("`","").lstrip()
			nums,item=line.split("  ")
			have,total=nums.split("/")
			have=have.replace(",","") if "," in have else have
			total=total.replace(",","") if "," in total else total
			need=int(total)-int(have)
			need+=1 # To keep one of everything for collector
			line=f"> `{need}` {item}"
			new_lines.append(line)
		return new_lines
		
	def __repr__(self):
		return str("\n".join([self.name]+self.lines)+"\n")

# PRINT ONE
#print(Bundle(bundle))

# PRINT ALL
BUNDLES=[Bundle(b) for b in BUNDLES]
print(*BUNDLES)

# Example Output:
## Shows needed amount (+1 for collector) and item
"""
### **Level Leviathan**
> `26` Joke Book
> `22` Pet Feeder
"""
			
