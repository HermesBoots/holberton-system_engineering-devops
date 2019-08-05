# install a Ruby gem
package { 'Puppet linter':
  ensure   => '2.1.1',
  name     => 'puppet-lint',
  provider => 'gem'
}
