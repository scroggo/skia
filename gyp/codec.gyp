# GYP file for codec project.
{
  'targets': [
    {
      'target_name': 'codec',
      'product_name': 'skia_codec',
      'type': 'static_library',
      'standalone_static_library': 1,
      'dependencies': [
        'core.gyp:*',
        'libjpeg.gyp:*',
        'etc1.gyp:libetc1',
        'ktx.gyp:libSkKTX',
        'libwebp.gyp:libwebp',
        'utils.gyp:utils',
      ],
      'include_dirs': [
        '../include/codec',
        '../src/codec',
      ],
      'sources': [
        '../src/codec/SkCodec.cpp',
        '../src/codec/SkCodec_libpng.cpp',
        '../src/codec/SkSwizzler.cpp',
      ],
      'conditions': [
        [ 'skia_os == "mac"', {
          'export_dependent_settings': [
            'libpng.gyp:libpng',
          ],
          'dependencies': [
            'libpng.gyp:libpng',
          ],
        }],
        [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris"]', {
          'export_dependent_settings': [
            'libpng.gyp:libpng',
            'giflib.gyp:giflib'
          ],
          'dependencies': [
            'libpng.gyp:libpng',
            'giflib.gyp:giflib'
          ],
          # end libpng/libgif stuff
        }],
        # FIXME: NaCl should be just like linux, etc, above, but it currently is separated out
        # to remove gif. Once gif is supported by naclports, this can be merged into the above
        # condition.
        [ 'skia_os == "nacl"', {
          'sources!': [
            '../src/images/SkImageDecoder_libgif.cpp',
            '../src/images/SkMovie_gif.cpp',
          ],
        }],
        [ 'skia_os == "android"', {
          'dependencies': [
             'android_deps.gyp:gif',
             'android_deps.gyp:png',
          ],
          'conditions': [
            [ 'skia_android_framework == 0', {
              'export_dependent_settings': [
                'android_deps.gyp:png',
                'libjpeg.gyp:*'
              ],
            }],
          ],
        }],
        [ 'skia_os == "chromeos"', {
          'dependencies': [
             'chromeos_deps.gyp:gif',
             'libpng.gyp:libpng',
          ],
        }],
        [ 'skia_os == "ios"', {
           'include_dirs': [
             '../include/utils/mac',
           ],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../include/codec',
        ],
      },
    },
  ],
}
