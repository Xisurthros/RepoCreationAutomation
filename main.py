import requests, json
from secrets import TOKEN
from requests.structures import CaseInsensitiveDict

GET_REPOS = 'https://api.github.com/search/repositories?q=user:Xisurthros'
MAKE_REPOS = 'https://api.github.com/user/repos'

def get_repos():
	
	resp = requests.get(GET_REPOS, headers=headers)
	data = resp.json()
	for item in data['items']:
		repo_info = {
			'name': item['name'],
			'owner': item['owner']['login'],
			'url': item['url'],
			'description': item['description'],
			'visibility': item['visibility'],
			'forks': item['forks'],
			'open_issues': item['open_issues'],
			'watchers': item['watchers'],
			'default_branch': item['default_branch'],
			'score': item['score'],
			'topics': item['topics'],
			'created_at': item['created_at'],
			'updated_at': item['updated_at'],
			'pushed_at': item['pushed_at'],
			'allow_forking': item['allow_forking'],
			'fork': item['fork'],
			'license': item['license'],
			'archived': item['archived'],
		}
		print(repo_info, '\n\n')

def make_repo():
	REPO_NAME = input("Repo Name: ")
	data = {"name": f"{REPO_NAME}"}
	data = json.dumps(data)
	response = requests.post(MAKE_REPOS, headers=headers, data=data)
	response = response.json()
	info = {
		'name': response['name'],
		'clone_url': response['clone_url']
	}
	print(info)

def main():
	while True:
		user_input = input('Enter: ').lower()
		if user_input == 'get_repos':
			get_repos()
		elif user_input == 'make_repo':
			make_repo()

if __name__ == '__main__':
	headers = {
		'Authorization': f'token {TOKEN}',
		'Content-Type': 'application/x-www-form-urlencoded',
	}
	main()