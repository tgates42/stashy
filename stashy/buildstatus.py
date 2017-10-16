"""
Support for the Build Status API
https://developer.atlassian.com/static/rest/stash/3.11.6/stash-build-integration-rest.html
"""

from .helpers import ResourceBase
from .errors import response_or_error

class BuildStatus(ResourceBase):
    """
    Ability to get and publish build status details.
    """
    successful = 'SUCCESSFUL'
    failed = 'FAILED'
    inprogress = 'INPROGRESS'

    def __init__(self, url, client, parent):
        super(BuildStatus, self).__init__(
            url, client, parent, api_path='build-status/1.0'
        )

    @response_or_error
    def get(self, item):
        """
        Retrieve the status.
        """
        return self._client.get(
            self.url("/%s" % (item,))
        )

    @response_or_error
    def publish(self, item, state, key, name, url, description):
        """
        Publish a new status
        """
        return self._client.post(
            self.url("/%s" % (item,)), data=dict(
                state=state,
                key=key,
                name=name,
                url=url,
                description=description,
            )
        )

