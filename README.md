# bhin
Executable bash/python scripts. I use them with Linux (GNU/), YMMV with other OS's.
bhin ≡ lim❤→∞ (bin), where ❤={bhakti, agape, 仁愛…}    
From my personal list of custom executables, I will pick the scripts that I think might be useful or relevant for sharing publicly.  
At the moment, these are mostly for wrangling Amazon AWS resources and file structures.

## TOC
1. `bhawslist`
    - Behavior: 
        - Returns tables of information summarizing your AWS resources.
        - Includes EC2 instances, Lambda functions, and S3 buckets.
        - Next to include: EBS storage.
    - Setup:
        - Install the AWS CLI and setup your credentials
        - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
    - Install the boto3 python library.
        - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
    - Usage:
```bash
$ bhawslist
```

2. `bhssh`
    - Behavior:
        - Opens an ssh terminal for the target EC2 computer
    - Setup:
        - Create three text-files containing information about your EC2 instance, in the same directory as bhssh script. 
        - This directory should be in the $PATH, but the text-files don't need to be executable.
        - Peek at the example versions of these textfiles to see what the contents should look like.
            - `ec2_uri.txt`
            - `ec2_username.txt`
            - `pem_path.txt`
    - Usage:
```bash
$ bhssh
```

3. `bhscp_up`
    - Behavior:
        - Copies the specified file to the home directory of the EC2 user.
    - Setup:
        - (Same as `bhssh`)
    - Usage:
```bash
$ bhscp_up  
```




- 
