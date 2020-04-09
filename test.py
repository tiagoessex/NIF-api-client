
import nifservice

print (nifservice.__version__)

try:
	result = nifservice.getNifInfo(nif='xxxxxxxxxx', key='xxxxxxxxxxxxxxxxxxxx')
	print (result)
except Exception as e:
	print (str(e))


