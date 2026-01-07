import network

def start_ap(ssid, passwd):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    try:
        ap.config(essid=ssid, password=passwd)
    except ValueError:
        return None

    print("AP Mode started!")
    print("IP Address:", ap.ifconfig()[0])
    return ap.ifconfig()[0]