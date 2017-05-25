from urllib2 import Request, urlopen, URLError
import json
exp = raw_input('Enter the expression')
oper = raw_input('Enter the operation you want to perform:\n1. Simplify\n2. Factor\n3. Derive\n4. Integrate\n5. zeroes\n6. Find Tangent(tangent)\n7. Area Under Curve(area)\n8. Cosine(cos)\n9. Sine(sin)\n10. Tangent(tan)\n11. Inverse Cosine(arccos)\n12. Inverse Sine(arcsin)\n13. Inverse Tangent(arctan)\n14. Absolute Value(Abs)\n15. Logarithm(log)')
url='https://newton.now.sh/'+oper+'/'+exp
request = Request(url)

try:
	response = urlopen(request)
	reply = json.load(response)
	print reply['result']
except URLError, e:
    print 'No operation. Got an error code:', e
