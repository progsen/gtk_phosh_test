configure_file(
  input: 'com.example.title_bar.desktop',
  output: 'com.example.title_bar.desktop',
  copy: true,
  install: true,
  install_dir: join_paths(get_option('datadir'), 'applications')
)

install_data('com.example.title_bar.svg',
  install_dir: join_paths(get_option('datadir'), 'icons', 'hicolor', 'scalable', 'apps'))
