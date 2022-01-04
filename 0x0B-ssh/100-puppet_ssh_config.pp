# manifest to connect to server and edit configuration file

exec {'echo "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config':
  path => '/bin'
}
