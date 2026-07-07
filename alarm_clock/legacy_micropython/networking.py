# networking.py
import machine, network
import config
import time

net_ssid = config.net_ssid
net_pwd = config.net_pwd


def do_connect():
    try:
        wlan = network.WLAN(network.WLAN.IF_STA)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network...')
            wlan.connect(net_ssid, net_pwd)
            # Setting an Timeout for 5 minutes (x) => start + x * 60
            start = time.time()
            end = start + 5 * 60

            while not wlan.isconnected():
                time.sleep_ms(100)
                if time.time() >= end:
                    raise Exception ("network connection can't be established")
                    break


        print('network config:', wlan.ipconfig('addr4'))
        connection_success = True
        return connection_success
    except RuntimeError:
        print("something went wrong with the network connection..")
    except OSError as ex:
        print(f"OSError: {ex}")
    except Exception as ex:
        print(f"Anderer Fehler ({type(ex)}): {ex}")

