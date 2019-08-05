# execute a command
exec { 'kill an infinite loop process':
  command => '/usr/bin/pkill --exact killmenow'
}
