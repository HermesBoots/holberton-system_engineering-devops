# fix a small open file limit enforced on Nginx
file { 'let Nginx open more files':
  ensure  => file,
  path    => '/etc/default/nginx',
  content => 'ULIMIT="-n 1048576"'
}

service { 'Nginx':
  ensure     => running,
  hasrestart => true,
  name       => 'nginx',
  subscribe  => File['/etc/default/nginx']
}
