def get_bucket_name_date(data):
    assert type(data) == dict
    return data.get('Buckets', {})
