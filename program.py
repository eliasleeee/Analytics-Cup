import Node

data = [[]]
f = open('E:\TUM\Lecture\WS2022\Lecture\Business Analytics and Machine Learning\CUP\DT\DecisionTree\src\Validation.csv')
for line in f:
	line = line.strip("\r\n")
	data.append(line.split(','))
data.remove([])
tree = {'Sales_Organization': {'B': {'Document_Type': {'Order': {'Type': {'SOP': {'Business_Unit': {'BU_C': {'Service_Type': {'0': '1', '1': '0'}}, 'BU_A': {'Service_Type': {'0': '1', '1': '1'}}, 'BU_B': {'Service_Type': {'0': '1', '1': '0'}}}}, 'STP': {'Business_Unit': {'BU_C': {'Service_Type': {'0': '0', '1': '0'}}, 'BU_B': {'Service_Type': {'0': '1', '1': '0'}}, 'BU_A': {'Service_Type': {'1': '1', '0': '1'}}}}}}, 'Returns': {'Business_Unit': {'BU_A': {'Type': {'STP': {'Service_Type': {'1': '1', '0': '0'}}, 'SOP': {'Service_Type': {'1': '1', '0': '0'}}}}, 'BU_C': {'Type': {'STP': {'Service_Type': {'0': '0'}}, 'SOP': {'Service_Type': {'0': '0'}}}}, 'BU_B': {'Type': {'STP': {'Service_Type': {'0': '1', '1': '1'}}, 'SOP': {'Service_Type': {'0': '1', '1': '1'}}}}}}, 'Credit memo': {'Service_Type': {'0': {'Business_Unit': {'BU_C': {'Type': {'SOP': '1', 'STP': '0'}}, 'BU_B': {'Type': {'STP': '0', 'SOP': '0'}}, 'BU_A': {'Type': {'SOP': '0', 'STP': '0'}}}}, '1': {'Type': {'SOP': {'Business_Unit': {'BU_B': '1', 'BU_A': '1', 'BU_C': '1'}}, 'STP': {'Business_Unit': {'BU_B': '1', 'BU_A': '1', 'BU_C': '1'}}}}}}, 'Order w/o charge': {'Service_Type': {'0': {'Business_Unit': {'BU_C': {'Type': {'SOP': '1', 'STP': '1'}}, 'BU_B': {'Type': {'SOP': '1'}}, 'BU_A': {'Type': {'SOP': '1', 'STP': '1'}}}}, '1': '1'}}}}, 'A': {'Type': {'SOP': {'Document_Type': {'Order': {'Business_Unit': {'BU_C': {'Service_Type': {'0': '0', '1': '0'}}, 'BU_A': {'Service_Type': {'0': '0', '1': '0'}}, 'BU_B': {'Service_Type': {'0': '0', '1': '0'}}}}, 'Contract': {'Business_Unit': {'BU_A': {'Service_Type': {'1': '1', '0': '0'}}, 'BU_C': {'Service_Type': {'1': '0', '0': '0'}}, 'BU_B': {'Service_Type': {'1': '0', '0': '0'}}}}, 'Returns': {'Business_Unit': {'BU_A': {'Service_Type': {'0': '1'}}, 'BU_C': {'Service_Type': {'0': '0'}}}}, 'Credit memo': {'Business_Unit': {'BU_A': {'Service_Type': {'1': '0', '0': '0'}}, 'BU_C': {'Service_Type': {'0': '0', '1': '0'}}, 'BU_B': {'Service_Type': {'1': '1', '0': '0'}}}}, 'Order w/o charge': {'Business_Unit': {'BU_C': {'Service_Type': {'0': '0'}}, 'BU_A': '0'}}}}, 'STP': {'Document_Type': {'Order': {'Business_Unit': {'BU_C': {'Service_Type': {'0': '0', '1': '0'}}, 'BU_A': {'Service_Type': {'0': '0', '1': '0'}}, 'BU_B': {'Service_Type': {'0': '0', '1': '0'}}}}, 'Contract': {'Business_Unit': {'BU_A': {'Service_Type': {'1': '1', '0': '0'}}, 'BU_C': {'Service_Type': {'1': '0', '0': '0'}}, 'BU_B': {'Service_Type': {'1': '0', '0': '0'}}}}, 'Returns': {'Business_Unit': {'BU_A': {'Service_Type': {'0': '1'}}, 'BU_C': {'Service_Type': {'0': '0'}}, 'BU_B': '0'}}, 'Credit memo': {'Business_Unit': {'BU_A': {'Service_Type': {'1': '0', '0': '0'}}, 'BU_C': {'Service_Type': {'1': '0', '0': '0'}}, 'BU_B': {'Service_Type': {'1': '1', '0': '0'}}}}, 'Order w/o charge': {'Business_Unit': {'BU_C': '1', 'BU_A': '0'}}}}}}, 'NA': {'Business_Unit': {'BU_A': {'Type': {'SOP': {'Document_Type': {'NA': {'Service_Type': {'0': '1'}}}}}}, 'BU_B': '0', 'BU_C': '0'}}}}
attributes = ['Type', 'Sales_Organization', 'Document_Type', 'Business_Unit', 'Service_Type', 'Reseller']
count = 0
for entry in data:
	count += 1
	tempDict = tree.copy()
	result = ""
	while(isinstance(tempDict, dict)):
		List_keys_tempDict = list(tempDict.keys())
		root = Node.Node(List_keys_tempDict[0], tempDict[List_keys_tempDict[0]])
		tempDict = tempDict[List_keys_tempDict[0]]
		index = attributes.index(root.value)
		childen_value = list(root.children)
		value = entry[index]
		if(value in childen_value):
			child = Node.Node(value, tempDict[value])
			result = tempDict[value]
			tempDict = tempDict[value]
		else:
			print( "can't process input %s" % count)
			result = "?"
			break
	print ("entry%s = %s" % (count, result))
