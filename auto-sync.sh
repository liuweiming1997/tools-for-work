#!/bin/bash

set -e

echo "sync tools-for-work"
git pull --rebase origin master

function sync_vim() {
  echo "sync_vim......."
  echo "---------------------------------->"
  cd ~/.vim/
  git pull --rebase origin master
  ./send-vimrc.sh
  # git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
  vim +PluginInstall +qall
}

function sync_zsh() {
  echo "sync_zsh......."
  echo "---------------------------------->"
  cd ~/.zsh/
  git pull --rebase origin master
  ./send-zshrc-file.sh
}

function sync_sublime() {
  echo "sync_sublime......."
  echo "---------------------------------->"
  cd ~/.config/sublime-text-3/
  git delworkspace .
  git pull --rebase origin master
}

function sync_tmux() {
  echo "sync_tmux....."
  echo "----------------------------------->"
  cd ~/.tmux/
  git pull --rebase origin master
  ./send-tmux-conf.sh
}

sync_vim
sync_zsh
sync_sublime
sync_tmux
