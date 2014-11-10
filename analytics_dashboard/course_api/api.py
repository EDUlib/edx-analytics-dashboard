import requests


class Course(object):
    def __init__(self, url, key):
        self.url = url
        self.api_key = key

    def _get(self, path):
        uri = '{0}/{1}'.format(self.url, path)
        headers = {'X-Edx-Api-Key': self.api_key}

        return requests.get(uri, headers=headers).json()

    def course_detail(self, course_id):
        # TODO Cache this info
        path = 'courses/{0}'.format(course_id)
        return self._get(path)
