"""A Python Pulumi program"""

import os
import mimetypes
import pulumi
import pulumi_aws as aws

# Programmatically set the file directory for bucket content
config = pulumi.Config()
site_dir = config.require("siteDir")

# create s3 bucket
bucket = aws.s3.BucketV2("my-bucket")


# loop through directory content and populate website
for file in os.listdir(site_dir):
    filepath = os.path.join(site_dir, file)
    mime_type, _ = mimetypes.guess_type(filepath)
    bucketObject = aws.s3.BucketObjectv2(file,
        bucket=bucket.bucket,
        source=pulumi.FileAsset(filepath),
        content_type=mime_type
        )

