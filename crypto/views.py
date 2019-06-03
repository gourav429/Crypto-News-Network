from django.shortcuts import render

def home(request):
    import requests
    import json

    #grab proce data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,USDT,MIOTA,TRX&tsyms=BTC,USD,EUR&api_key=ed12ad990e872f476af0101ea85244955c060cfc0b8ac9529dce74a342488c05")
    price = json.loads(price_request.content)

    #grab news data
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request,'home.html',{'api':api,'price':price})


