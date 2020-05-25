export ANSIBLE_HOST_KEY_CHECKING=False
ssh-add ~/.ssh/JimmyLsc.pem
ansible-playbook instance.yaml -i inventory/hosts.txt
