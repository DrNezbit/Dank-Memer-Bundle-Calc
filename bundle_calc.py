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
		self.name,b_list=self.get_name(bundle_str)
		self.lines=self.calculate(self.build_list(b_list))
		
	def get_name(self,text:str):
		split=text.split("**")
		name="**"+split[-2]+"**"
		contents=split[-1]
		b_list=contents.split(" <:CX:1071484097957994587> ")
		b_list.pop(0)
		return name,b_list
		
	def build_list(self,b_list:list):
		lines=[]
		for line in b_list:
			line=line.split("\n")[0].split(" ")
			for word in line:
				if word.startswith("<") and word.endswith(">"):
					line.remove(word)
			lines.append(" ".join(line))
		return lines
		
	def calculate(self,lines,extras=False):
		new_lines=[]
		for line in lines:
			line=line.replace("`","").lstrip()
			nums,item=line.split("  ")
			have,total=nums.split("/")
			have=have.replace(",","") if "," in have else have
			total=total.replace(",","") if "," in total else total
			need=int(total)-int(have)
			if not extras:
				need+=1 # To keep one of everything for collector
			else: need=need*-1-1
			if need >0:
				line=f"> `{need}` {item}"
				new_lines.append(line)
		return new_lines
		
	def get_extras(self,bundle_str):
		extra_list=bundle_str.split(" <:CY:1071484103762915348> ")
		extra_list.pop(0)
		if len(extra_list)>0:
			extras=self.build_list(extra_list)
			extra_list=self.calculate(extras,extras=True)
		return extra_list
		
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
			
