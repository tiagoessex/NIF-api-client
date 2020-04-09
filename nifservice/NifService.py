import requests
import json


def getNifInfo(nif = None, key = None):
	if not nif:
		raise RuntimeError("É necessário um NIF!")
	if not key:
		raise RuntimeError("É necessário uma chave!")
		
	url = "https://www.nif.pt/?json=1&q={}&key={}".format(nif, key)

	results = requests.get(url)

	results = results.json()
	
	data = {'status':'NOT FOUNDED'}
	
	if results.get('result') and results.get('result') != 'success':
		if results.get('result') == 'error':
			return data
		raise RuntimeError(results.get('message'))			
	
	
	if results.get('records') and results.get('records').get(nif):
		results = results.get('records').get(nif)	
		
	
		data['status'] = 'OK'
		
		if results.get('title'):
			data['nome'] = results.get('title')
		if results.get('address'):
			data['morada'] = results.get('address')
		if results.get('pc4'):
			data['cp'] = results.get('pc4')
		if results.get('pc3'):
			data['cp_ext'] = results.get('pc3')
		if results.get('city'):
			data['cidade'] = results.get('city')
		if results.get('start_date'):
			data['data_inicio'] = results.get('start_date')
		
		if results.get('activity'):
			data['actividade'] = results.get('activity')
		if results.get('status'):
			data['estado'] = results.get('status')
		if results.get('cae'):
			data['cae'] = results.get('cae')
		
		if results.get('contacts'):
			if results.get('contacts').get('email'):
				data['email'] = results.get('contacts').get('email')
			if results.get('contacts').get('phone'):
				data['phone'] = results.get('contacts').get('phone')
			if results.get('contacts').get('website'):
				data['website'] = results.get('contacts').get('website')
			if results.get('contacts').get('fax'):
				data['fax'] = results.get('contacts').get('fax')
		
		if results.get('structure'):
			if results.get('structure').get('nature'):
				data['natureza'] = results.get('contacts').get('nature')
			if results.get('structure').get('capital'):
				data['capital'] = results.get('contacts').get('capital')
			if results.get('structure').get('capital_currency'):
				data['denominacao'] = results.get('contacts').get('capital_currency')
		
		
		if results.get('geo'):
			if results.get('geo').get('region'):
				data['distrito'] = results.get('geo').get('region')
			if results.get('geo').get('county'):
				data['concelho'] = results.get('geo').get('county')
			if results.get('geo').get('parish'):
				data['freguesia'] = results.get('geo').get('parish')
		
		if results.get('place'):
			if results.get('place').get('address'):
				data['morada2'] = results.get('place').get('address')
			if results.get('place').get('pc4'):
				data['cp'] = results.get('place').get('pc4')
			if results.get('place').get('pc3'):
				data['cp_ext2'] = results.get('place').get('pc3')
			if results.get('place').get('city'):
				data['cidade2'] = results.get('place').get('city')
		
		if results.get('racius'):
			data['racius'] = results.get('racius')
		if results.get('alias'):
			data['alias'] = results.get('alias')	
		if results.get('portugalio'):
			data['portugalio'] = results.get('portugalio')
		
		
			
	return data
