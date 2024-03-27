#!/usr/bin/env bash
# Puppet manifest to create an SSH configuration file for the client

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
