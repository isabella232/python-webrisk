# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import abc
import typing

from google import auth
from google.api_core import exceptions  # type: ignore
from google.auth import credentials  # type: ignore

from google.cloud.webrisk_v1beta1.types import webrisk


class WebRiskServiceV1Beta1Transport(abc.ABC):
    """Abstract transport class for WebRiskServiceV1Beta1."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self,
        *,
        host: str = "webrisk.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: typing.Optional[str] = None,
        scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                credentials_file, scopes=scopes
            )
        elif credentials is None:
            credentials, _ = auth.default(scopes=scopes)

        # Save the credentials.
        self._credentials = credentials

    @property
    def compute_threat_list_diff(
        self,
    ) -> typing.Callable[
        [webrisk.ComputeThreatListDiffRequest],
        typing.Union[
            webrisk.ComputeThreatListDiffResponse,
            typing.Awaitable[webrisk.ComputeThreatListDiffResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_uris(
        self,
    ) -> typing.Callable[
        [webrisk.SearchUrisRequest],
        typing.Union[
            webrisk.SearchUrisResponse, typing.Awaitable[webrisk.SearchUrisResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_hashes(
        self,
    ) -> typing.Callable[
        [webrisk.SearchHashesRequest],
        typing.Union[
            webrisk.SearchHashesResponse, typing.Awaitable[webrisk.SearchHashesResponse]
        ],
    ]:
        raise NotImplementedError()


__all__ = ("WebRiskServiceV1Beta1Transport",)
