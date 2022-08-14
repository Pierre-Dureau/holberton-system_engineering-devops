# modify SSH configuration file
file_line { 'modify password line':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  match   => '#   PasswordAuthentication yes',
  line    => '    PasswordAuthentication no',
}

file_line { 'add private key line':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
}
