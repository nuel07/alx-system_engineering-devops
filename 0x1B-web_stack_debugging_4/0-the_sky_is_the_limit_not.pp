# increase traffic handling capacity of Nginx

exec {'extend limit':
     onlyif => 'test -e /etc/default/nginx',
     command => 'sudo sed -i "s/15/4096/" /etc/default/nginx/: sudo service nginx restart',
     provider => shell,
}
