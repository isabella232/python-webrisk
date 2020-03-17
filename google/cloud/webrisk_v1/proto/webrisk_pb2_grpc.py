# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.webrisk_v1.proto import (
    webrisk_pb2 as google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2,
)


class WebRiskServiceStub(object):
    """Web Risk API defines an interface to detect malicious URLs on your
  website and in client applications.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.ComputeThreatListDiff = channel.unary_unary(
            "/google.cloud.webrisk.v1.WebRiskService/ComputeThreatListDiff",
            request_serializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.ComputeThreatListDiffRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.ComputeThreatListDiffResponse.FromString,
        )
        self.SearchUris = channel.unary_unary(
            "/google.cloud.webrisk.v1.WebRiskService/SearchUris",
            request_serializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.SearchUrisRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.SearchUrisResponse.FromString,
        )
        self.SearchHashes = channel.unary_unary(
            "/google.cloud.webrisk.v1.WebRiskService/SearchHashes",
            request_serializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.SearchHashesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.SearchHashesResponse.FromString,
        )
        self.CreateSubmission = channel.unary_unary(
            "/google.cloud.webrisk.v1.WebRiskService/CreateSubmission",
            request_serializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.CreateSubmissionRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.Submission.FromString,
        )


class WebRiskServiceServicer(object):
    """Web Risk API defines an interface to detect malicious URLs on your
  website and in client applications.
  """

    def ComputeThreatListDiff(self, request, context):
        """Gets the most recent threat list diffs. These diffs should be applied to
    a local database of hashes to keep it up-to-date. If the local database is
    empty or excessively out-of-date, a complete snapshot of the database will
    be returned. This Method only updates a single ThreatList at a time. To
    update multiple ThreatList databases, this method needs to be called once
    for each list.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SearchUris(self, request, context):
        """This method is used to check whether a URI is on a given threatList.
    Multiple threatLists may be searched in a single query.
    The response will list all requested threatLists the URI was found to
    match. If the URI is not found on any of the requested ThreatList an
    empty response will be returned.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SearchHashes(self, request, context):
        """Gets the full hashes that match the requested hash prefix.
    This is used after a hash prefix is looked up in a threatList
    and there is a match. The client side threatList only holds partial hashes
    so the client must query this method to determine if there is a full
    hash match of a threat.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateSubmission(self, request, context):
        """Creates a Submission of a URI suspected of containing phishing content to
    be reviewed. If the result verifies the existence of malicious phishing
    content, the site will be added to the [Google's Social Engineering
    lists](https://support.google.com/webmasters/answer/6350487/) in order to
    protect users that could get exposed to this threat in the future. Only
    projects with CREATE_SUBMISSION_USERS visibility can use this method.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_WebRiskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ComputeThreatListDiff": grpc.unary_unary_rpc_method_handler(
            servicer.ComputeThreatListDiff,
            request_deserializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.ComputeThreatListDiffRequest.FromString,
            response_serializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.ComputeThreatListDiffResponse.SerializeToString,
        ),
        "SearchUris": grpc.unary_unary_rpc_method_handler(
            servicer.SearchUris,
            request_deserializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.SearchUrisRequest.FromString,
            response_serializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.SearchUrisResponse.SerializeToString,
        ),
        "SearchHashes": grpc.unary_unary_rpc_method_handler(
            servicer.SearchHashes,
            request_deserializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.SearchHashesRequest.FromString,
            response_serializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.SearchHashesResponse.SerializeToString,
        ),
        "CreateSubmission": grpc.unary_unary_rpc_method_handler(
            servicer.CreateSubmission,
            request_deserializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.CreateSubmissionRequest.FromString,
            response_serializer=google_dot_cloud_dot_webrisk__v1_dot_proto_dot_webrisk__pb2.Submission.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.webrisk.v1.WebRiskService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))