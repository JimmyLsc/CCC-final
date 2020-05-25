export ANSIBLE_HOST_KEY_CHECKING=False
ssh-add ~/.ssh/JimmyLsc.pem
ansible-playbook save-old-tweet.yaml -i inventory/hosts.txt
