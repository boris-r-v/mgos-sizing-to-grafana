import json

diag_payload = '{"hall":65447,"temp":71.666667,"uptime":513.941051,"free_ram":206508,"total_ram":285360,"deviceId":"esp32_372528"}'
data_payload = '{"VDC1":-0.021108,"VAC1":0.074074,"VAC1f420":0.031746,"VAC1f480":0.010582,"VAC1f580":0.042328,"VAC1f720":0,"VAC1f780":0,"F1cur":254,"F1mod":3,"VDC2":-0.031740,"VAC2":0.042440,"VAC2f420":0.010582,"VAC2f480":0.010582,"VAC2f580":0.010582,"VAC2f720":0,"VAC2f780":0,"F2cur":230,"F2mod":0,"VDC3":-0.010554,"VAC3":0.010582,"VAC3f420":0,"VAC3f480":0,"VAC3f580":0,"VAC3f720":0,"VAC3f780":0,"F3cur":20,"F3mod":0,"VDC4":0.031746,"VAC4":0.063660,"VAC4f420":0.010582,"VAC4f480":0.010582,"VAC4f580":0.010582,"VAC4f720":0.010610,"VAC4f780":0.010610,"F4cur":71,"F4mod":0,"uns_mode":0,"uns_diag":768,"cntr":2140}'

payload = '{"system":{"time":"15088599000","soc":43,"charge":false,"rssi":-62,"unit":"C"}, "channel":[{"number":1,"name":"Kanal 1","typ":8,"temp":19.90,"min":10.00,"max":25.00,"alarm":false,"color":"#0C4C88"},{"number":2,"name":"Kanal 2","typ":0,"temp":999.00,"min":10.00,"max":35.00,"alarm":false,"color":"#22B14C"}], "pitmaster":[{"id":0,"channel":1,"pid":0,"value":0,"set":20.80,"typ":"off"}]}'


def main():
#    data = json.loads(payload)
#    print(data['channel'])

#    for c in data['channel']:
#        print(c)

    pl = json.loads(data_payload)
    print (pl)
    for c in pl:
        print(c, pl[c])



main()