import requests
import json

token = 'Bearer {yourKeyHere}'
base_url = 'https://api.twitter.com/1.1/search/tweets.json'
properties_file_name = 'properties.json'

def get_search_properties():
	
	json_data = {}

	with open(properties_file_name) as data_file:
		return json.load(data_file)

def request_tweets():

	search_properties = get_search_properties()
	
	for character in search_properties['characters']:
		account = character['account']
		subject = character['subject']
		since_id = character['sinceId']
		
		query_parameter = account + ' ' + subject
		
		params_map = {'q': query_parameter, 'since_id': since_id}

		headers = {'Authorization': token}
		r = requests.get(base_url, params=params_map, headers=headers)
		
		output_file = 'tweets/' + account + '.json'

		search_result = r.json()

		if search_result['statuses']:
			character['sinceId'] = search_result['statuses'][0]['id']

			with open(output_file, "a") as result_file:
				result_file.write(r.content)

	with open(properties_file_name, 'w') as outfile:
		json.dump(search_properties, outfile)

request_tweets()
