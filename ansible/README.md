# Ansible

# Team Members:
893060 Shuhua Zhang
935209 Shuai Mou
962546 Yicheng Jin
961002 Shuocheng Li
830789 Ningjing Wang


## How to run

### 1.Copy Openstack Password

```
OWJhYmZlNzY5OGM5ZTk5
```

### 2.Run Group NeCTAR Configuration


1. put the ansible directory as your current folder
2. change the ./instnce/host_vars/instance.yaml variable "workplace_path" to your path
3. copy the JimmyLsc.pem to the ~/.ssh folder
4. terminal command: sh run-nectar.sh, set the openstack password and computer become password

### 3.Start Docker Compose

terminal command: sh run.sh

### 4.Save file into database

terminal command: sh save-old-tweet.sh

