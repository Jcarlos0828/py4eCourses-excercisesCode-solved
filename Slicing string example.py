#Parsing and Extracting Example

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atPos = data.find('@')
print(atPos)
endPos = data.find(' ', atPos)
print(endPos)
host = data[atPos+1:endPos]
print(host)