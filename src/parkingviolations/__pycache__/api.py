from sodapy import Socrata
from requests import HTTPError

class Service(object):
	def __init__(self, app_token, domain="data.cityofnewyork.us"):
		# print(f"domain={domain}, app_token={app_token}")
		self.client = Socrata(domain, app_token)

	def __enter__(self):
		return self

	def get_info (self, location="nc67-uf89", limit=10):
		try:
			print(f"location={location}, limit={str(limit)}")
			return self.client.get(location, limit=limit)
		except HTTPError as e:
			print(f"Failed to make API call: {e}")
			raise
		except KeyError as e:
			print(f"Failed to get rates from response: {e}")
			raise
		except Exception as e:
			print(f"Something went wrong: {e}")
			raise

	def get_next_info(self, location="nc67-uf89", limit=10, offset=10):
		print(f"limit={str(limit)}, offset={str(offset)}")
		try:
			return self.client.get(location, limit=limit, offset=offset)
		except HTTPError as e:
			print(f"Failed to make API call: {e}")
			raise
		except KeyError as e:
			print(f"Failed to get rates from response: {e}")
			raise
		except Exception as e:
			print(f"Something went wrong: {e}")
			raise

	def get_size(self, location="nc67-uf89"):
		try:
			ret = self.client.get(location, select='COUNT(*)')
			return int(ret[0]['COUNT'])
		except HTTPError as e:
			print(f"Failed to make API call: {e}")
			raise
		except KeyError as e:
			print(f"Failed to get rates from response: {e}")
			raise
		except Exception as e:
			print(f"Something went wrong: {e}")
			raise

	def close(self):
		self.client.close()

	def __exit__(self, exc_type, exc_value, traceback):
		self.close()