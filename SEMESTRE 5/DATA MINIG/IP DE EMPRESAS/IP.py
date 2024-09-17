import requests,json

def obteneripdesdedominio(dominio):
    print("------dominio->"+str(dominio+"-----"))
    resultadobusqueda = requests.get("https://networkcalc.com/api/dns/lookup/"+str(dominio))
    if resultadobusqueda.json()['records'] != None:
        for i in range(len(resultadobusqueda.json()['records']['A'])):
            ip = resultadobusqueda.json()['records']['A'][i]['address']
            resultadoregion= requests.get("https://ipinfo.io/"+str(ip)+"/json")
            print("la region de la ip ->"+str(ip)+" es "+str(resultadoregion.json()))
dominios = [
    "apple.com",
    "google.com",
    "microsoft.com",
    "amazon.com",
    "facebook.com",  # Meta (Facebook)
    "netflix.com",
    "samsung.com",
    "tesla.com",
    "ibm.com",
    "intel.com",
    "oracle.com",
    "adobe.com",
    "salesforce.com",
    "uber.com",
    "airbnb.com",
    "spotify.com",
    "twitter.com",
    "linkedin.com",
    "yahoo.com",
    "ebay.com",
    "alibaba.com",
    "tencent.com",
    "baidu.com",
    "zoom.us",
    "shopify.com",
    "paypal.com",
    "square.com",
    "reddit.com",
    "dropbox.com",
    "slack.com",
    "stripe.com",
    "pinterest.com",
    "vmware.com",
    "nvidia.com",
    "sap.com",
    "qualcomm.com",
    "palantir.com",
    "hp.com",
    "dell.com",
    "lenovo.com",
    "asus.com",
    "acer.com",
    "xiaomi.com",
    "huawei.com",
    "sony.com",
    "panasonic.com",
    "toshiba.com",
    "bosch.com",
    "siemens.com",
    "ge.com",
    "honeywell.com",
    "3m.com",
    "jnj.com",
    "pfizer.com",
    "novartis.com",
    "roche.com",
    "merck.com",
    "astrazeneca.com",
    "gsk.com",
    "sanofi.com",
    "abbvie.com",
    "amgen.com",
    "biogen.com",
    "lilly.com",
    "gilead.com",
    "regeneron.com",
    "vrtx.com",
    "texasinst.com",
    "broadcom.com",
    "analog.com",
    "micron.com",
    "qualcomm.com"
]


#for i in dominios:
   # obteneripdesdedominio(i)

def obteneremailsdesdedominio(dominio):
    resultadoemails = requests.get("https://api.hunter.io/v2/domain-search?domain="+str(dominio)+"&api_key=3be4bd56d0e0b0de1b899203b1a98102bede7166")



obteneripdesdedominio()
obteneremailsdesdedominio()




