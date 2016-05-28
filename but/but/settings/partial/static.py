import os

from .base import BASE_DIR, PROJECT_DIR


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
        'jquery': {
            'source_filenames': (
                'js/vendor/ordered/jquery.min.js',
            ),
            'output_filename': 'js/vendor/ordered/jquery.min.js',
        },
        'bootstrap': {
            'source_filenames': (
                'js/vendor/ordered/bootstrap.js',
            ),
            'output_filename': 'js/vendor/ordered/bootstrap.js',
        },
        'mdb': {
            'source_filenames': (
                'js/vendor/ordered/mdb.js',
            ),
            'output_filename': 'js/vendor/ordered/mdb.js',
        },
        'summernote': {
            'source_filenames': (
                'js/vendor/ordered/summernote.js',
            ),
            'output_filename': 'js/vendor/ordered/summnernote.js',
        },

        'vendor': {
            'source_filenames': (
                'js/vendor/not_ordered/*.js',
            ),
            'output_filename': 'js/vendor/not_ordered/vendor.js',
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
        'certificate': {
            'source_filenames': (
                'js/separate/certificate.js',
            ),
            'output_filename': 'js/separate/certificate.js',
        },
        'email': {
            'source_filenames': (
                'js/separate/send_email.js',
            ),
            'output_filename': 'js/separate/send_email.js',
        },

    }
}


PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
# PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
