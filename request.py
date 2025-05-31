import requests
import json
import textwrap


class APIRequest:

    def __init__(self, waiting_time=None):
        self._session = requests.Session()
        self._waiting_time = waiting_time

    def _send_request(self, method: str, url: str, **kwargs):
        try:
            response = self._session.request(
                method=method,
                url=url,
                **kwargs
            )
            self._debug_print(response=response)

        except requests.exceptions.RequestException as e:

            response = None

            if debug:
                print(textwrap.dedent(
                    """
                    ---------------- response ----------------
                    Request Error
                    {method} {url}
                    Kwargs: {kwargsstr}
                    Error : {e}
                    Response: {response}
                    """
                ).format(
                    method=method,
                    url=url,
                    e=str(e),
                    kwargsstr=f'{kwargs}',
                    resp=response
                ))

    def _debug_print(self, response: requests.Response):
        request_body = response.request.body

        if request_body:
            request_body = json.loads(request_body)

        try:
            parsed_body = response.json()
            response_body = json.dumps(parsed_body, indent=4, ensure_ascii=False)
        except ValueError:
            response_body = response.text

        format_header = lambda x_item: '\n'.join(f'{k}: {v}' for k, v in x_item.items())

        return print(textwrap.dedent(
            """
            ---------------- request ----------------
            {req.method} {req.url}
            {request_header}
            Request Body :
            {request_body}
             ---------------- response ----------------
            {resp.status_code} {resp.reason} {resp.url}
            {resp_header}
            Duration : {resp_duration}
            Response Context :
            {response_body}
            """
        ).format(
            req=response.request,
            request_body=json.dumps(request_body, indent=4, ensure_ascii=False),
            resp=response,
            response_body=response_body,
            resp_duration=response.elapsed.total_seconds(),
            request_header=format_header(response.request.headers),
            resp_header=format_header(response.headers),
        ))
