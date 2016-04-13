import os

from .base import BASE_DIR, PROJECT_DIR


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, "dist", "static")
MEDIA_ROOT = os.path.join(PROJECT_DIR, "dist", "media")

PIPELINE = {
    'STYLESHEETS': {
        'vendor': {
            'source_filenames': (
              'css/vendor/*.css',
            ),
            'output_filename': 'css/vendor/vendor.css',
        },
        'style': {
            'source_filenames': (
              'css/*.css',
            ),
            'output_filename': 'css/style.css',
        },
    },
    'JAVASCRIPT': {
        'vendor': {
            'source_filenames': (
                'js/vendor/jquery-2.2.3.min.js',
                'js/vendor/bootstrap.min.js',
                'js/vendor/materialize.min.js',
                'js/vendor/summernote.js',
                'js/vendor/summernote-ko-KR.js',
            ),
            'output_filename': 'js/vendor/vendor.js',
        },
        'but': {
            'source_filenames': (
                'js/module/*.js',
            ),
            'output_filename': 'js/module/but.js',
        },
        'comment': {
            'source_filenames': (
                'js/separate/comment.js',
            ),
            'output_filename': 'js/separate/comment.js',
        },
        'usercheck': {
            'source_filenames': (
                'js/separate/user_check.js',
            ),
            'output_filename': 'js/separate/user_check.js',
        },
    }
}


PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
