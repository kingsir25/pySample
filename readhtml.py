import re
file_name = 'C:\\Users\\Administrator\\OneDrive\\study\\python\\beantest.jsp'
with open(file_name,'r',encoding='utf-8') as strf:
	str = strf.read()
	res = r'(?<=<bean:write )[^>]*(?=/>)'
	# name_pattern=re.compile('(?<= name\s*\=\" )[^\"]*(?=\")',flags=re.M)
	# match=pattern.findall(str)
	# print(match)
	name_pattern=re.compile(r'\bname="([^"]*)"')
	property_pattern=re.compile(r'\bproperty="([^"]*)"')
	format_pattern=re.compile(r'\bformat="([^"]*)"')
	li = re.findall(res,str)
	with open("new.txt","w") as wstr:
		for s in li:
			print(s)
			name=name_pattern.findall(s)
			# wstr.write(name)
			# wstr.write("\n")
			print(name,'')
			prty=property_pattern.findall(s)
			print(prty,'')
			format=format_pattern.findall(s)
			print(format,'')

