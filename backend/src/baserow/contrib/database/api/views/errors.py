from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND


ERROR_VIEW_DOES_NOT_EXIST = (
    'ERROR_VIEW_DOES_NOT_EXIST',
    HTTP_404_NOT_FOUND,
    'The requested view does not exist.'
)
ERROR_VIEW_FILTER_DOES_NOT_EXIST = (
    'ERROR_VIEW_FILTER_DOES_NOT_EXIST',
    HTTP_404_NOT_FOUND,
    'The view filter does not exist.'
)
ERROR_VIEW_FILTER_NOT_SUPPORTED = (
    'ERROR_VIEW_FILTER_NOT_SUPPORTED',
    HTTP_400_BAD_REQUEST,
    'Filtering is not supported for the view type.'
)
ERROR_VIEW_FILTER_TYPE_NOT_ALLOWED_FOR_FIELD = (
    'ERROR_VIEW_FILTER_TYPE_NOT_ALLOWED_FOR_FIELD',
    HTTP_400_BAD_REQUEST,
    'The chosen filter type is not allowed for the provided field.'
)
