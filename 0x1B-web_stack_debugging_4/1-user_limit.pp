# OS configuration to enable holberton usere to login and access file with no error

exec { 'increase file limit':
command  => 'awk \'$1 == "holberton" { $4=50000 }1\' /etc/security/limits.conf > tmp && mv tmp /etc/security/limits.conf',
path     => ['/usr/bin', '/bin', '/usr/sbin'],
provider => 'shell'
}
