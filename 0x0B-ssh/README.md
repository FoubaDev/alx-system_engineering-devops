# 0x0B. SSH

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using #!/usr/bin/env bash instead of /bin/bash


## Files:


| File                    	 | 
| ------------------------------- 
| `0-use_a_private_key`   	|
| `2-ssh_config`    	  	| 
| `3-is_kind_of_class.py` 	| 
| `100-puppet_ssh_config.pp`    | 


## Tasks :page_with_curl:

* **0. Use a private key**
  * [0-use_a_private_key](./0-use_a_private_key): Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

* **1. Create an SSH key pair**
  * [1-create_ssh_key_pair](./1-create_ssh_key_pair): Write a Bash script that creates an RSA key pair.

* **2. Client configuration file**
  * [2-ssh_config](./2-ssh_config): Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

* **3. Let me in!**
  * [3-is_kind_of_class.py](./3-is_kind_of_class.py): Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.

* **4. Client configuration file (w/ Puppet)**
  * [100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp):Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.
