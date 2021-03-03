# Below code delete all the snapshots older than 15 days.

from datetime import datetime, timedelta, timezone

import boto3
ec2 = boto3.resourse('ec2')

# list(ec2.Snapshot)
snapshots = ec2.snapshots.filter(OwnersIds=['self'])

for snapshot in snapshots:
    start_time = snapshot.start_time
    delete_time =datetime.now(tz=timezone.utc) - timdelta(days=15)
    if delete_time > start_time:
        print('fmt_start_time = {} And delet_time = {}'.format(snapshot.snapshot_id))
        snapshot.delete()
        print ('Snapshot with ID = {} is deleted'.format(snapshot.snapshot_id))

