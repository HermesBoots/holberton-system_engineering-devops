# fix misspelled PHP extension in WordPress file

exec { 'fix broken PHP extension':
  command => '/bin/sed -i \'s/\.phpp\>/\.php/\' wp-settings.php',
  cwd     => '/var/www/html'
}
