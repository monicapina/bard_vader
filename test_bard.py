'''
This is a test file to ensure that Bard API works properly
'''
import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard
from BardInterface import BardInterface

token_1PSID = 'cwhB4VVoardujruiFz8jnaxHWaYKv1A1F6Zjc-8NwQ10nDJLfR6xw9KuqZ1Xn3t-wEXyCA.'
token_1PSIDTS = 'sidts-CjIBNiGH7oE7zL0z-BDi2yTotN-3ZBmK5dG1QposwXsaL-Z-0hnn9l7IzOz4RnM3xe0bGBAA'

bard_interface = BardInterface(token_1PSID, token_1PSIDTS)

question = "How many races has Fernando Alonso won?"
answer = bard_interface.ask(question)

print(answer)