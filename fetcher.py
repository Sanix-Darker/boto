import requests
import json
from lxml import html
from os import path as ospath, makedirs as osmakedir


def create_dir(drr):
    if ospath.exists(DIR) == False: osmakedir(DIR)


host_url = "https://www.leboncoin.fr"
fetch_array = [
    {
        "search":"chaussures",
        "category": 53
    }
]

# Create the "data dir if it's not exist"
create_dir("data")

for fetch_elt in fetch_array:
    DIR = "./data/"+fetch_elt["search"].replace(" ","")+str(fetch_elt["category"])+"/"
    create_dir(DIR)

    print("[+] -------------------------------------------------------------------")
    print("[+] Fetch started...")
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8,fr-FR;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "_gcl_au=1.1.1755050895.1574580135; cikneeto_uuid=id:9e5e2d08-9df9-43b1-b772-2784f7af491b; consent_allpurpose=cDE9MjtwMj0yO3AzPTI7cDQ9MjtwNT0y; cookieBanner=0; oas_ab=b; datadome=Pw6_M.n43cSMa2q9sdOlv_hW7BYiDqSLQZWQwOoFEjy8tHgbRXt5TmeYktWdghy6GROTbB.UT~64qCAnVBiThSL~EPhhKx3q1.XlX7iUCy; xtvrn=$562498$; xtan562498=-undefined; xtant562498=1; utag_main=v_id:016e9c4a475500168f9f1e855e9b03069003306100bd0$_sn:1$_ss:1$_pn:1%3Bexp-session$_st:1574581954344$ses_id:1574580143957%3Bexp-session; cikneeto=date:1574580154407; _fbp=fb.1.1574580156385.805606168; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5XzE2RDg5NjhCLUQ3RTUtNDAzOS04OTY4LTg2M0Y3ODUzM0MzOCIsImNpZCI6bnVsbCwiZXhwIjoxNjA2MTE2MTU2NDcxLCJjcyI6bnVsbH0%3D; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5XzE2RDg5NjhCLUQ3RTUtNDAzOS04OTY4LTg2M0Y3ODUzM0MzOCIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; _pulse2data=197ee388-7be3-41ee-8812-467802ec41cd%2Cv%2C%2C1574581060380%2CeyJpc3N1ZWRBdCI6IjIwMTktMTEtMjRUMDc6MjI6NDBaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..3zi1SYgFXZbEja3IE4EPww.yTMV1hfas_p_vfRVbY090PnACgoiTUmr7n-iTdMNaPJ9SbGeyugKlQed4hnnJYtjS7NxCQfqQpKEQJyIQli8QTXYxS6Yy-fkktGwMO_hUIeP7fPt0fUhlda5m_FUzWl_gaRZIijeQtq5izigXyCfx17HUHuKCso2IOYA0fVu1wrxq3C3dXqO1eBaFr05yvdGtHldj4pYk9dVRek76S0pEA.hSI_xU_2rtLwbtOMbtc-NQ%2C%2C0%2CTrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..kO3WkPK4DfKszgKdGnO7-ojL3v8NUljKFNqHlbyi4vw",
        "Pragma": "no-cache",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    CAT = ""
    if fetch_elt["category"] != 0 :
        CAT = "&category="+str(fetch_elt["category"])

    fetch_url = host_url+"/recherche/?text="+fetch_elt["search"]+CAT
    r = requests.get(fetch_url, headers=headers)
    result = r.content.decode("utf-8")
    with open(DIR+"result.html", "w+") as frr:
        frr.write(result)

    result_json = json.loads(result.split("window.__REDIAL_PROPS__ = ")[1].split("</script>")[0])
    data_list = {}
    for rr in result_json:
        try:
            if rr["data"] != None:
                data_list = rr["data"]
                break
        except: pass
    with open(DIR+"result.json", "w+") as frr:
        frr.write(json.dumps(data_list, indent=4, sort_keys=True))


    category_json =  json.loads(result.split("window.FLUX_STATE = ")[1].split("</script>")[0])
    mega_data = category_json["lbcData"]
    with open(DIR+"mega_data.json", "w+") as frr:
        frr.write(json.dumps(mega_data, indent=4, sort_keys=True))

    print("[+] Fetch End, check files in ./data")
    print("[+] -------------------------------------------------------------------")
