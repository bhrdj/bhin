#!/usr/bin/env python3

import boto3, pandas as pd
from fs import filesize
from tabulate import tabulate

trad_fs = filesize.traditional

s3 = boto3.resource('s3')

bkt_list = list(s3.buckets.all())
bkt_names = [bkt.name for bkt in bkt_list]

objs_in_bkts = [bkt.objects.all() for bkt in bkt_list]
bkt_sizes = [sum(obj.size for obj in bkt) for bkt in objs_in_bkts]
bkt_sizes = {b:trad_fs(s) for b,s in zip(bkt_names, bkt_sizes)}
bkt_sizes = pd.Series(bkt_sizes, name='BucketSize')
bkt_sizes = pd.DataFrame(bkt_sizes)
bkt_sizes.index.name = 'BucketName'

print(tabulate(bkt_sizes, headers='keys', tablefmt='psql'))

