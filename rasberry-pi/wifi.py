import network

def start_ap(ssid, passwd):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    
    # 修正ポイント: 引数名を省略、または対応した形式に変更
    # 多くの環境では password を指定するだけで自動的に WPA2 になります
    try:
        # まずは一般的な形式で試行
        ap.config(essid=ssid, password=passwd)
    except ValueError:
        # 古い、または特定のファームウェア向けの予備（引数名が異なる場合）
        # 例: ap.config(ssid=ssid, key=passwd) などが必要な機種もあります
        print("Standard config failed, trying alternative...")
        ap.config(ssid=ssid, password=passwd)

    print("AP Mode started!")
    print("IP Address:", ap.ifconfig()[0])
    return ap.ifconfig()[0]

# 実行
