import json, argparse
from pipedrive.client import Client


pipedrive_api_token = '154feadb5e67a9d66b6d6530fa24a77452ac146d'


def client(api_token):
  client = Client(domain='https://smartlunch.pipedrive.com/')
  client.set_api_token(api_token)

  return client


def deals_from_filter(filter_id):
  deals_from_filter = client.deals.get_all_deals_with_filter(filter_id)['data']

  return deals_from_filter


def write_json_to_file(file_name, obj):
  f = open(file_name, 'a+', encoding='utf-8')
  json.dump(obj, f, ensure_ascii=False)
  f.write('\n')


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--filter-id", default=201, help="PipeDrive filter id.")
	parser.add_argument("--file-name", help="File path to save deals.")
	args = parser.parse_args()

	client = client(pipedrive_api_token)
	deals = deals_from_filter(args.filter_id)

	for deal in deals:
		write_json_to_file(args.file_name, deal)
