import boto3
import multiprocessing
import csv
import botocore



def init_copy(b, nb):
    global client
    client = boto3.client('s3')

    global bucket
    bucket = b
    global new_bucket
    new_bucket = nb


def copy_file(k):
    key, new_key = k
    try:
        client.head_object(Bucket=new_bucket, Key=new_key)
    except botocore.exceptions.ClientError:
        client.copy(CopySource={'Bucket': bucket, 'Key': key},
                    Bucket=new_bucket,
                    Key=new_key)


def copy_files(src_list, dest_list):
    try:
        p = multiprocessing.Pool(processes=16, initializer=init_copy,
            initargs=('czbiohub-maca', 'czbiohub-maca'))
        p.map(copy_file, zip(src_list, dest_list))
    finally:
        p.close()
        p.join()


# function to get files
def get_files(bucket='czbiohub-seqbot', prefix=None):
    paginator = client.get_paginator('list_objects')

    response_iterator = paginator.paginate(
            Bucket=bucket, Prefix=prefix
    )

    for result in response_iterator:
        if 'Contents' in result:
            yield from (r['Key'] for r in result['Contents'])



# these are all the TM sequencing folders
S3_FOLDERS = ['170907_A00111_0051_BH2HWLDMXX',
              '170907_A00111_0052_AH2HTCDMXX',
              '170910_A00111_0053_BH2HGKDMXX',
              '170910_A00111_0054_AH2HGWDMXX',
              '170914_A00111_0057_BH3FY7DMXX',
              '170914_A00111_0058_AH3FYKDMXX',
              '170918_A00111_0059_BH3G22DMXX',
              '170918_A00111_0060_AH3FYVDMXX',
              '170921_A00111_0062_BH3FYHDMXX',
              '170921_A00111_0063_AH3G23DMXX',
              '170925_A00111_0066_AH3TKNDMXX',
              '170925_A00111_0067_BH3M5YDMXX',
              '170928_A00111_0068_AH3YKKDMXX',
              '170928_A00111_0069_BH52YMDMXX']

# got the list of all files from czbiohub-maca
all_files = []
for folder in S3_FOLDERS:
    all_files.extend(get_files('czbiohub-maca', os.path.join('data', folder, 'rawdata_remux')))
print(len(all_files))

# had this B cell IDs
filename = '/home/ubuntu/olgabot-aws-scratch/maca_bcell_or_children_ids.csv'
with open(filename) as f:
    rdr = csv.reader(f)
    rows = list(rdr)

cells = {r[0].replace('.', '-') for r in rows}
print(list(cells)[:5])

bcell_files = [fn for fn in all_files if os.path.basename(fn).rsplit('_', 3)[0] in cells]
print(len(bcell_files))
