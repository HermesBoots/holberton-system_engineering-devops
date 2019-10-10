file { 'let Nginx open more files':
  ensure  => file,
  path    => '/etc/default/nginx',
  content => 'ULIMIT="-n 1048576"',
  notify  => Service['nginx']
}

service { 'Nginx':
  ensure => running,
  name   => 'nginx',
  enable => true
}
