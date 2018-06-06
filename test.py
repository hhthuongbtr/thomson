from thomson import Thomson

tsn = Thomson('172.29.3.189', 'iptv_tool', '123456')

print tsn.get_datetime()
