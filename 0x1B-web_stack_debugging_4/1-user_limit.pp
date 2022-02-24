# OS configuration to enable holberton usere to login and access file with no error

exec {'hard-correct':
     command => 'sudo sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
     provider => shell,
}

exec {'soft-correct':
     command => 'sudo sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
     provider => shell,
}
