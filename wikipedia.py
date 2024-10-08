import pywhatkit
def tell_me_about(domain):
    try:
        res = pywhatkit.info(domain,lines=4)
        return res
    except Exception as e:
        print(e)
        return False
