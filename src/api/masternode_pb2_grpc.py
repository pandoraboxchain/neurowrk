# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import masternode_pb2 as masternode__pb2


class WorkerServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CogniteBatch = channel.unary_unary(
        '/WorkerService/CogniteBatch',
        request_serializer=masternode__pb2.CognitionRequest.SerializeToString,
        response_deserializer=masternode__pb2.CognitionResponse.FromString,
        )


class WorkerServiceServicer(object):

  def CogniteBatch(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WorkerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CogniteBatch': grpc.unary_unary_rpc_method_handler(
          servicer.CogniteBatch,
          request_deserializer=masternode__pb2.CognitionRequest.FromString,
          response_serializer=masternode__pb2.CognitionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'WorkerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class MasternodeSerivceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.cognitionComplete = channel.unary_unary(
        '/MasternodeSerivce/cognitionComplete',
        request_serializer=masternode__pb2.CognitionResult.SerializeToString,
        response_deserializer=masternode__pb2.CognitionStatus.FromString,
        )


class MasternodeSerivceServicer(object):

  def cognitionComplete(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MasternodeSerivceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'cognitionComplete': grpc.unary_unary_rpc_method_handler(
          servicer.cognitionComplete,
          request_deserializer=masternode__pb2.CognitionResult.FromString,
          response_serializer=masternode__pb2.CognitionStatus.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MasternodeSerivce', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))