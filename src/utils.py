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

def format_stables(stable_list):
    format_stables_list = [{"stable_name": stable_name, "stable_id": stable_id, "ranking": ranking, "rikishi": rikishi} for stable_name, stable_id, ranking, rikishi in stable_list]
    return format_stables_list

def format_owned_stable(columns, stable):
    format_stables_dict = {columns[0]: stable[0], columns[1]: stable[1], columns[2]: stable[2], columns[3]: stable[3], columns[4]: stable[4], columns[5]: stable[5], columns[6]: stable[6]}
    return format_stables_dict
