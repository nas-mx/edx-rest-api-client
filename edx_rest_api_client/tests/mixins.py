import responses


class AuthenticationTestMixin(object):
    """ Mixin for testing authentication. """

    def _mock_auth_api(self, url, status, body=None):
        body = body or {}
        responses.add(
            responses.POST,
            url,
            status=status,
            json=body,
            content_type='application/json'
        )
