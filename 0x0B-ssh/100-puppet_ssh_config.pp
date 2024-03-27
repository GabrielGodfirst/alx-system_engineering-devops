file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "
    Host ubuntu
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
