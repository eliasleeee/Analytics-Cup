import Node

data = [[]]
f = open('E:\TUM\Lecture\WS2022\Lecture\Business Analytics and Machine Learning\CUP\DT\DecisionTree\src\Soybean.csv')
for line in f:
	line = line.strip("\r\n")
	data.append(line.split(','))
data.remove([])
tree = {'leafspot-size': {'dna': {'stem-cankers': {'above-sec-nde': {'fruit-spots': {'dna': 'diaporthe-stem-canker', 'brown-w/blk-specks': 'anthracnose', 'absent': 'anthracnose'}}, 'absent': {'int-discolor': {'black': 'charcoal-rot', 'brown': 'brown-stem-rot', 'none': {'leaves': {'abnorm': 'powdery-mildew', 'norm': 'purple-seed-stain'}}}}, 'below-soil': {'canker-lesion': {'brown': 'rhizoctonia-root-rot', 'dk-brown-blk': 'phytophthora-rot'}}, 'above-soil': {'fruit-pods': {'dna': 'phytophthora-rot', 'norm': 'anthracnose'}}}}, 'gt-1/8': {'canker-lesion': {'tan': {'precip': {'lt-norm': 'brown-stem-rot', 'norm': 'brown-stem-rot', 'gt-norm': 'brown-spot'}}, 'dna': {'date': {'october': {'temp': {'lt-norm': 'downy-mildew', 'gt-norm': 'alternarialeaf-spot', 'norm': {'crop-hist': {'same-lst-two-yrs': {'area-damaged': {'upper-areas': 'alternarialeaf-spot', 'low-areas': 'alternarialeaf-spot', 'whole-field': 'frog-eye-leaf-spot'}}, 'same-lst-sev-yrs': 'alternarialeaf-spot', 'same-lst-yr': 'alternarialeaf-spot', 'diff-lst-year': 'alternarialeaf-spot'}}}}, 'june': {'precip': {'gt-norm': {'leaf-mild': {'lower-surf': 'downy-mildew', 'absent': 'brown-spot'}}, 'norm': {'hail': {'no': 'brown-spot', 'yes': {'plant-stand': {'lt-normal': 'phyllosticta-leaf-spot', 'normal': 'brown-spot'}}}}, 'lt-norm': 'phyllosticta-leaf-spot'}}, 'may': {'precip': {'gt-norm': {'leafspots-halo': {'yellow-halos': 'downy-mildew', 'no-yellow-halos': 'brown-spot'}}, 'norm': {'area-damaged': {'scattered': 'brown-spot', 'upper-areas': 'brown-spot', 'whole-field': 'phyllosticta-leaf-spot'}}, 'lt-norm': 'phyllosticta-leaf-spot'}}, 'august': {'leaf-mild': {'lower-surf': 'downy-mildew', 'absent': {'leaf-malf': {'absent': {'seed-tmt': {'fungicide': {'germination': {'lt-80': {'crop-hist': {'same-lst-yr': 'alternarialeaf-spot', 'same-lst-sev-yrs': {'area-damaged': {'scattered': 'alternarialeaf-spot', 'low-areas': {'plant-stand': {'lt-normal': {'precip': {'gt-norm': {'temp': {'norm': {'hail': {'yes': {'severity': {'pot-severe': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leaf-shread': {'absent': {'stem': {'norm': {'lodging': {'yes': {'stem-cankers': {'absent': {'fruiting-bodies': {'absent': {'external-decay': {'absent': {'mycelium': {'absent': {'int-discolor': {'none': {'sclerotia': {'absent': {'fruit-pods': {'norm': {'fruit-spots': {'absent': {'seed': {'norm': {'mold-growth': {'absent': {'seed-discolor': {'absent': {'seed-size': {'norm': {'shriveling': {'absent': {'roots': {'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}, '80-89': {'precip': {'gt-norm': 'alternarialeaf-spot', 'norm': 'frog-eye-leaf-spot'}}, '90-100': 'frog-eye-leaf-spot'}}, 'none': {'germination': {'80-89': {'area-damaged': {'whole-field': 'alternarialeaf-spot', 'upper-areas': {'crop-hist': {'same-lst-two-yrs': 'alternarialeaf-spot', 'same-lst-yr': 'frog-eye-leaf-spot'}}, 'scattered': 'frog-eye-leaf-spot', 'low-areas': 'frog-eye-leaf-spot'}}, 'lt-80': {'crop-hist': {'same-lst-two-yrs': 'alternarialeaf-spot', 'diff-lst-year': 'alternarialeaf-spot', 'same-lst-yr': 'alternarialeaf-spot', 'same-lst-sev-yrs': {'area-damaged': {'upper-areas': 'alternarialeaf-spot', 'scattered': 'frog-eye-leaf-spot'}}}}, '90-100': 'alternarialeaf-spot'}}, 'other': 'frog-eye-leaf-spot'}}, 'present': 'phyllosticta-leaf-spot'}}}}, 'september': {'leaf-mild': {'lower-surf': 'downy-mildew', 'absent': {'temp': {'gt-norm': 'alternarialeaf-spot', 'norm': {'leaf-shread': {'absent': {'crop-hist': {'diff-lst-year': {'precip': {'gt-norm': 'alternarialeaf-spot', 'norm': 'frog-eye-leaf-spot'}}, 'same-lst-two-yrs': 'alternarialeaf-spot', 'same-lst-sev-yrs': 'frog-eye-leaf-spot', 'same-lst-yr': {'hail': {'yes': 'frog-eye-leaf-spot', 'no': 'alternarialeaf-spot'}}}}, 'present': 'alternarialeaf-spot'}}}}}}, 'april': 'brown-spot', 'july': {'precip': {'gt-norm': {'leaf-mild': {'absent': {'area-damaged': {'low-areas': {'crop-hist': {'same-lst-sev-yrs': 'brown-spot', 'same-lst-two-yrs': 'alternarialeaf-spot'}}, 'scattered': {'germination': {'80-89': {'hail': {'yes': 'alternarialeaf-spot', 'no': 'frog-eye-leaf-spot'}}, '90-100': 'alternarialeaf-spot', 'lt-80': 'frog-eye-leaf-spot'}}, 'upper-areas': 'frog-eye-leaf-spot', 'whole-field': 'brown-spot'}}, 'lower-surf': 'downy-mildew'}}, 'norm': 'phyllosticta-leaf-spot', 'lt-norm': 'phyllosticta-leaf-spot'}}}}, 'brown': {'external-decay': {'absent': {'lodging': {'yes': 'brown-spot', 'no': 'frog-eye-leaf-spot'}}, 'firm-and-dry': 'frog-eye-leaf-spot'}}, 'dk-brown-blk': 'frog-eye-leaf-spot'}}, 'lt-1/8': {'canker-lesion': {'dna': {'leafspots-marg': {'w-s-marg': {'seed-size': {'norm': {'roots': {'norm': 'bacterial-blight', 'rotted': 'bacterial-pustule'}}, 'lt-norm': 'bacterial-pustule'}}, 'no-w-s-marg': 'bacterial-pustule'}}, 'tan': 'purple-seed-stain'}}}}
for i in range(10):
	tree(list(tree.keys())[1])
attributes = ['date', 'plant-stand', 'precip', 'temp', 'hail', 'crop-hist', 'area-damaged', 'severity', 'seed-tmt', 'germination', 'plant-growth', 'leaves', 'leafspots-halo', 'leafspots-marg', 'leafspot-size', 'leaf-shread', 'leaf-malf', 'leaf-mild', 'stem', 'lodging', 'stem-cankers', 'canker-lesion', 'fruiting-bodies', 'external-decay', 'mycelium', 'int-discolor', 'sclerotia', 'fruit-pods', 'fruit-spots', 'seed', 'mold-growth', 'seed-discolor', 'seed-size', 'shriveling', 'roots', 'class']
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
		print(list(root.children))
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
