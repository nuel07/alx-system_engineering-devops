# used strace to fix .phpp extensions to .php in the `wp-settings.php`.

exec { 'fix-extensions':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
