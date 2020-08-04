# Installs the puppet linter with the GEM thing
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
