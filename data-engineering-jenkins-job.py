#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Final Assignment Data Engineering 3
# Katharina Burtscher
# 10.03.2026
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The code below scrapes the ETC prices and extracts the minimum and maximum.
# once it's done that it posts them to the botsbotsbots channel

# load packages
import requests
import pandas as pd
import apprise

# scrape data
url = "https://api.binance.com/api/v3/klines"
params = {"symbol": "ETHUSDT", "interval": "1m", "limit": 60}

response = requests.get(url, params=params)
data = response.json()

# convert to dataframe
df = pd.DataFrame(data, columns=[
    'open_time', 'open', 'high', 'low', 'close', 'volume', 
    'close_time', 'quote_asset_volume', 'trades', 
    'taker_buy_base', 'taker_buy_quote', 'ignore'
])

# convert price columns to float
df[['high', 'low']] = df[['high', 'low']].astype(float)

# calculate min and max
min_price = df['low'].min()
max_price = df['high'].max()

# making sure the objects look alright:
print(min_price)
print(max_price)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print max/min prices to the bots bots bots channel

poster = apprise.Apprise()
#poster.add('https://ceuedu.webhook.office.com/webhookb2/024e3795-77fd-48bf-bb88-bcd9ff32fb63@d9c45913-7653-4be2-920b-bdb038638184/IncomingWebhook/f1f181c9f08d4ce486cf68fde13f1b50/9c2cd7c2-1e29-43c8-981b-6868f4d94231/V2OlgrpEHPajmlIAmuEUzzgdOKCj-ReO_TOuCqHcdqrMk1')
poster.add("https://defaultd9c4591376534be2920bbdb0386381.84.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/5bd5c68074614208861091934b5c138c/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=vIaL0MX17MY3A7fMbYJzgZdC-u9Cciu8JfsmzN2ojys")
poster.notify(
    title=f"--- ETH max/min price of the last 60 Minutes ---",
    body=f"Minimum Price: ${min_price:,.2f};Maximum Price: ${max_price:,.2f}")

