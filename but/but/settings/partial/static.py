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
        'jquery': {
            'source_filenames': (
                'js/vendor/jquery-2.2.3.min.js',
            ),
            'output_filename': 'js/vendor/jquery.js',
        },
        'bootstrap': {
            'source_filenames': (
                'js/vendor/bootstrap.min.js',
            ),
            'output_filename': 'js/vendor/bootstrap.js',
        },
        'material': {
            'source_filenames': (
                'js/vendor/materialize.min.js',
            ),
            'output_filename': 'js/vendor/material.js',
        },
        'summernote': {
            'source_filenames': (
                'js/vendor/summernote.js',
            ),
            'output_filename': 'js/vendor/summernote.js',
        },
        'summernote_ko': {
            'source_filenames': (
                'js/vendor/summernote-ko-KR.js',
            ),
            'output_filename': 'js/vendor/summernote_ko.js',
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

    }
}


PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
