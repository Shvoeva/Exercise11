def responses_creator(item_ids):
    return [dict(item_id=i) for i in item_ids]

if __name__ == '__main__':
    print(responses_creator('abcd'))