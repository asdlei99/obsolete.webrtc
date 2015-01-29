solutions = [{
  'name': 'src',
  'url': 'https://dpeted.visualstudio.com/DefaultCollection/TED%20Consumer/_git/RTC_chromium',
  'deps_file': '.DEPS.git',
  'managed': False,
  'custom_deps': {
    # Skip syncing some large dependencies WebRTC will never need.
    'src/chrome/tools/test/reference_build/chrome_linux': None,
    'src/chrome/tools/test/reference_build/chrome_mac': None,
    'src/chrome/tools/test/reference_build/chrome_win': None,
    'src/native_client': None,
    'src/third_party/ffmpeg': None,
    'src/third_party/junit/src': None,
    'src/third_party/WebKit': None,
    'src/v8': None,
  },
  'safesync_url': ''
}]

cache_dir = None
