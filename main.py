from gingerit.gingerit import GingerIt


text = input("Enter the text for correction:")
parser = GingerIt()
result = parser.parse(text)
print(result)
