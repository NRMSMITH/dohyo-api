def format_rikishi(rikishi_list):
    format_rikishi_list = []
    for rikishi in rikishi_list:
        rikishi_dict = {}
        rikishi_dict['id'] = rikishi[0]
        rikishi_dict['sumodb_id'] = rikishi[1]
        rikishi_dict['nsk_id'] = rikishi[2]
        rikishi_dict['shikona_en'] = rikishi[3]
        rikishi_dict['shikona_jp'] = rikishi[4]
        rikishi_dict['current_rank'] = rikishi[5]
        rikishi_dict['heya'] = rikishi[6]
        rikishi_dict['birth_date'] = rikishi[7]
        rikishi_dict['shusshin'] = rikishi[8]
        rikishi_dict['height'] = str(rikishi[9])
        rikishi_dict['weight'] = str(rikishi[10])
        rikishi_dict['debut'] = rikishi[11]
        rikishi_dict['sumoapi_id'] = rikishi[12]
        format_rikishi_list.append(rikishi_dict)
    return format_rikishi_list