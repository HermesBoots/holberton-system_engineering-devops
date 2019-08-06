# add configuration lines to simplify connecting to the Holberton server
file_line { 'disable SSH password auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^#?\s*PasswordAuthentication\s+\S+$'
}

file_line { 'use Holberton SSH key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/holberton',
  match  => '^(    |\t)IdentityFile ~/\.ssh/holberton$'
}
