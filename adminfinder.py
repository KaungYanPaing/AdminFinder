import requests

def main():
	banner()
	bruteforcer()
	end()
	while True:
		process = input('Do u want to continue (yes/no):: ')
		if (process == 'yes' or process == 'y' or process == 'Yes' or process == 'Y'):
			banner()
			bruteforcer()
			continue
		elif (process == 'no' or process == 'n' or process == 'No' or process == 'N'):
			break
		else:
			print('Enter either [yes] or [no]:: ')
	end()
			
def banner():
	print('\n')
	print('\t ==--==--==--==--==--==--==--==--==--==')
	print('\t ==--==--==--==--==--==--==--==--==--==')
	print('\t ==--   Admin Login Finder V 1.0   --==')
	print('\t ==--  Author : k4ung_k4ung (H3x)  --==')
	print('\t ==--==--==--==--==--==--==--==--==--==')
	print('\t ==--==--==--==--==--==--==--==--==--==')
	print('\n')
	print('\t eg - Enter your target site :: https://www.target.com/')
	print('\n')

	
def bruteforcer():

	target = input(' Enter your target site :: ')

	adminlist = open('admin_wordlist.txt')

	for x in adminlist:
		r = requests.get(target+x.strip())

		if (r.status_code == 200):
			print('[*] Found >>'+target+str(x))
			print('******Login Found!!******')
			print()
		else:
			print('[-]'+target+str(x)+'//----Admin Login Not Found----//' )
	print('\n')

def end():
	print('---------------------------------------------------------------------------')


if __name__ == '__main__':main()
