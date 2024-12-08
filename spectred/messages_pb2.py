# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: messages.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'messages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import rpc_pb2 as rpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\tprotowire\x1a\trpc.proto\"\x9a \n\x0fSpectredRequest\x12\n\n\x02id\x18\x65 \x01(\x04\x12O\n\x18getCurrentNetworkRequest\x18\xe9\x07 \x01(\x0b\x32*.protowire.GetCurrentNetworkRequestMessageH\x00\x12\x43\n\x12submitBlockRequest\x18\xeb\x07 \x01(\x0b\x32$.protowire.SubmitBlockRequestMessageH\x00\x12M\n\x17getBlockTemplateRequest\x18\xed\x07 \x01(\x0b\x32).protowire.GetBlockTemplateRequestMessageH\x00\x12M\n\x17notifyBlockAddedRequest\x18\xef\x07 \x01(\x0b\x32).protowire.NotifyBlockAddedRequestMessageH\x00\x12M\n\x17getPeerAddressesRequest\x18\xf2\x07 \x01(\x0b\x32).protowire.GetPeerAddressesRequestMessageH\x00\x12;\n\x0eGetSinkRequest\x18\xf4\x07 \x01(\x0b\x32 .protowire.GetSinkRequestMessageH\x00\x12K\n\x16getMempoolEntryRequest\x18\xf6\x07 \x01(\x0b\x32(.protowire.GetMempoolEntryRequestMessageH\x00\x12U\n\x1bgetConnectedPeerInfoRequest\x18\xf8\x07 \x01(\x0b\x32-.protowire.GetConnectedPeerInfoRequestMessageH\x00\x12;\n\x0e\x61\x64\x64PeerRequest\x18\xfa\x07 \x01(\x0b\x32 .protowire.AddPeerRequestMessageH\x00\x12O\n\x18submitTransactionRequest\x18\xfc\x07 \x01(\x0b\x32*.protowire.SubmitTransactionRequestMessageH\x00\x12_\n notifyVirtualChainChangedRequest\x18\xfe\x07 \x01(\x0b\x32\x32.protowire.NotifyVirtualChainChangedRequestMessageH\x00\x12=\n\x0fgetBlockRequest\x18\x81\x08 \x01(\x0b\x32!.protowire.GetBlockRequestMessageH\x00\x12G\n\x14getSubnetworkRequest\x18\x83\x08 \x01(\x0b\x32&.protowire.GetSubnetworkRequestMessageH\x00\x12]\n\x1fgetVirtualChainFromBlockRequest\x18\x85\x08 \x01(\x0b\x32\x31.protowire.GetVirtualChainFromBlockRequestMessageH\x00\x12?\n\x10getBlocksRequest\x18\x87\x08 \x01(\x0b\x32\".protowire.GetBlocksRequestMessageH\x00\x12G\n\x14getBlockCountRequest\x18\x89\x08 \x01(\x0b\x32&.protowire.GetBlockCountRequestMessageH\x00\x12K\n\x16getBlockDagInfoRequest\x18\x8b\x08 \x01(\x0b\x32(.protowire.GetBlockDagInfoRequestMessageH\x00\x12[\n\x1eresolveFinalityConflictRequest\x18\x8d\x08 \x01(\x0b\x32\x30.protowire.ResolveFinalityConflictRequestMessageH\x00\x12Y\n\x1dnotifyFinalityConflictRequest\x18\x8f\x08 \x01(\x0b\x32/.protowire.NotifyFinalityConflictRequestMessageH\x00\x12O\n\x18getMempoolEntriesRequest\x18\x93\x08 \x01(\x0b\x32*.protowire.GetMempoolEntriesRequestMessageH\x00\x12=\n\x0fshutdownRequest\x18\x95\x08 \x01(\x0b\x32!.protowire.ShutdownRequestMessageH\x00\x12\x41\n\x11getHeadersRequest\x18\x97\x08 \x01(\x0b\x32#.protowire.GetHeadersRequestMessageH\x00\x12Q\n\x19notifyUtxosChangedRequest\x18\x99\x08 \x01(\x0b\x32+.protowire.NotifyUtxosChangedRequestMessageH\x00\x12S\n\x1agetUtxosByAddressesRequest\x18\x9c\x08 \x01(\x0b\x32,.protowire.GetUtxosByAddressesRequestMessageH\x00\x12M\n\x17getSinkBlueScoreRequest\x18\x9e\x08 \x01(\x0b\x32).protowire.GetSinkBlueScoreRequestMessageH\x00\x12\x61\n!notifySinkBlueScoreChangedRequest\x18\xa0\x08 \x01(\x0b\x32\x33.protowire.NotifySinkBlueScoreChangedRequestMessageH\x00\x12\x33\n\nbanRequest\x18\xa3\x08 \x01(\x0b\x32\x1c.protowire.BanRequestMessageH\x00\x12\x37\n\x0cunbanRequest\x18\xa5\x08 \x01(\x0b\x32\x1e.protowire.UnbanRequestMessageH\x00\x12;\n\x0egetInfoRequest\x18\xa7\x08 \x01(\x0b\x32 .protowire.GetInfoRequestMessageH\x00\x12_\n stopNotifyingUtxosChangedRequest\x18\xa9\x08 \x01(\x0b\x32\x32.protowire.StopNotifyingUtxosChangedRequestMessageH\x00\x12o\n(notifyPruningPointUtxoSetOverrideRequest\x18\xab\x08 \x01(\x0b\x32:.protowire.NotifyPruningPointUtxoSetOverrideRequestMessageH\x00\x12}\n/stopNotifyingPruningPointUtxoSetOverrideRequest\x18\xae\x08 \x01(\x0b\x32\x41.protowire.StopNotifyingPruningPointUtxoSetOverrideRequestMessageH\x00\x12i\n%estimateNetworkHashesPerSecondRequest\x18\xb0\x08 \x01(\x0b\x32\x37.protowire.EstimateNetworkHashesPerSecondRequestMessageH\x00\x12\x65\n#notifyVirtualDaaScoreChangedRequest\x18\xb2\x08 \x01(\x0b\x32\x35.protowire.NotifyVirtualDaaScoreChangedRequestMessageH\x00\x12S\n\x1agetBalanceByAddressRequest\x18\xb5\x08 \x01(\x0b\x32,.protowire.GetBalanceByAddressRequestMessageH\x00\x12Y\n\x1dgetBalancesByAddressesRequest\x18\xb7\x08 \x01(\x0b\x32/.protowire.GetBalancesByAddressesRequestMessageH\x00\x12Y\n\x1dnotifyNewBlockTemplateRequest\x18\xb9\x08 \x01(\x0b\x32/.protowire.NotifyNewBlockTemplateRequestMessageH\x00\x12\x65\n#getMempoolEntriesByAddressesRequest\x18\xbc\x08 \x01(\x0b\x32\x35.protowire.GetMempoolEntriesByAddressesRequestMessageH\x00\x12G\n\x14getCoinSupplyRequest\x18\xbe\x08 \x01(\x0b\x32&.protowire.GetCoinSupplyRequestMessageH\x00\x12\x35\n\x0bpingRequest\x18\xc0\x08 \x01(\x0b\x32\x1d.protowire.PingRequestMessageH\x00\x12\x41\n\x11getMetricsRequest\x18\xc2\x08 \x01(\x0b\x32#.protowire.GetMetricsRequestMessageH\x00\x12G\n\x14getServerInfoRequest\x18\xc4\x08 \x01(\x0b\x32&.protowire.GetServerInfoRequestMessageH\x00\x12G\n\x14getSyncStatusRequest\x18\xc6\x08 \x01(\x0b\x32&.protowire.GetSyncStatusRequestMessageH\x00\x12\x65\n#getDaaScoreTimestampEstimateRequest\x18\xc8\x08 \x01(\x0b\x32\x35.protowire.GetDaaScoreTimestampEstimateRequestMessageH\x00\x12\x65\n#submitTransactionReplacementRequest\x18\xcc\x08 \x01(\x0b\x32\x35.protowire.SubmitTransactionReplacementRequestMessageH\x00\x12I\n\x15getConnectionsRequest\x18\xce\x08 \x01(\x0b\x32\'.protowire.GetConnectionsRequestMessageH\x00\x12G\n\x14getSystemInfoRequest\x18\xd0\x08 \x01(\x0b\x32&.protowire.GetSystemInfoRequestMessageH\x00\x12I\n\x15getFeeEstimateRequest\x18\xd2\x08 \x01(\x0b\x32\'.protowire.GetFeeEstimateRequestMessageH\x00\x12\x61\n!getFeeEstimateExperimentalRequest\x18\xd4\x08 \x01(\x0b\x32\x33.protowire.GetFeeEstimateExperimentalRequestMessageH\x00\x12U\n\x1bgetCurrentBlockColorRequest\x18\xd6\x08 \x01(\x0b\x32-.protowire.GetCurrentBlockColorRequestMessageH\x00\x42\t\n\x07payload\"\xcc\'\n\x10SpectredResponse\x12\n\n\x02id\x18\x65 \x01(\x04\x12Q\n\x19getCurrentNetworkResponse\x18\xea\x07 \x01(\x0b\x32+.protowire.GetCurrentNetworkResponseMessageH\x00\x12\x45\n\x13submitBlockResponse\x18\xec\x07 \x01(\x0b\x32%.protowire.SubmitBlockResponseMessageH\x00\x12O\n\x18getBlockTemplateResponse\x18\xee\x07 \x01(\x0b\x32*.protowire.GetBlockTemplateResponseMessageH\x00\x12O\n\x18notifyBlockAddedResponse\x18\xf0\x07 \x01(\x0b\x32*.protowire.NotifyBlockAddedResponseMessageH\x00\x12K\n\x16\x62lockAddedNotification\x18\xf1\x07 \x01(\x0b\x32(.protowire.BlockAddedNotificationMessageH\x00\x12O\n\x18getPeerAddressesResponse\x18\xf3\x07 \x01(\x0b\x32*.protowire.GetPeerAddressesResponseMessageH\x00\x12=\n\x0fGetSinkResponse\x18\xf5\x07 \x01(\x0b\x32!.protowire.GetSinkResponseMessageH\x00\x12M\n\x17getMempoolEntryResponse\x18\xf7\x07 \x01(\x0b\x32).protowire.GetMempoolEntryResponseMessageH\x00\x12W\n\x1cgetConnectedPeerInfoResponse\x18\xf9\x07 \x01(\x0b\x32..protowire.GetConnectedPeerInfoResponseMessageH\x00\x12=\n\x0f\x61\x64\x64PeerResponse\x18\xfb\x07 \x01(\x0b\x32!.protowire.AddPeerResponseMessageH\x00\x12Q\n\x19submitTransactionResponse\x18\xfd\x07 \x01(\x0b\x32+.protowire.SubmitTransactionResponseMessageH\x00\x12\x61\n!notifyVirtualChainChangedResponse\x18\xff\x07 \x01(\x0b\x32\x33.protowire.NotifyVirtualChainChangedResponseMessageH\x00\x12]\n\x1fvirtualChainChangedNotification\x18\x80\x08 \x01(\x0b\x32\x31.protowire.VirtualChainChangedNotificationMessageH\x00\x12?\n\x10getBlockResponse\x18\x82\x08 \x01(\x0b\x32\".protowire.GetBlockResponseMessageH\x00\x12I\n\x15getSubnetworkResponse\x18\x84\x08 \x01(\x0b\x32\'.protowire.GetSubnetworkResponseMessageH\x00\x12_\n getVirtualChainFromBlockResponse\x18\x86\x08 \x01(\x0b\x32\x32.protowire.GetVirtualChainFromBlockResponseMessageH\x00\x12\x41\n\x11getBlocksResponse\x18\x88\x08 \x01(\x0b\x32#.protowire.GetBlocksResponseMessageH\x00\x12I\n\x15getBlockCountResponse\x18\x8a\x08 \x01(\x0b\x32\'.protowire.GetBlockCountResponseMessageH\x00\x12M\n\x17getBlockDagInfoResponse\x18\x8c\x08 \x01(\x0b\x32).protowire.GetBlockDagInfoResponseMessageH\x00\x12]\n\x1fresolveFinalityConflictResponse\x18\x8e\x08 \x01(\x0b\x32\x31.protowire.ResolveFinalityConflictResponseMessageH\x00\x12[\n\x1enotifyFinalityConflictResponse\x18\x90\x08 \x01(\x0b\x32\x30.protowire.NotifyFinalityConflictResponseMessageH\x00\x12W\n\x1c\x66inalityConflictNotification\x18\x91\x08 \x01(\x0b\x32..protowire.FinalityConflictNotificationMessageH\x00\x12g\n$finalityConflictResolvedNotification\x18\x92\x08 \x01(\x0b\x32\x36.protowire.FinalityConflictResolvedNotificationMessageH\x00\x12Q\n\x19getMempoolEntriesResponse\x18\x94\x08 \x01(\x0b\x32+.protowire.GetMempoolEntriesResponseMessageH\x00\x12?\n\x10shutdownResponse\x18\x96\x08 \x01(\x0b\x32\".protowire.ShutdownResponseMessageH\x00\x12\x43\n\x12getHeadersResponse\x18\x98\x08 \x01(\x0b\x32$.protowire.GetHeadersResponseMessageH\x00\x12S\n\x1anotifyUtxosChangedResponse\x18\x9a\x08 \x01(\x0b\x32,.protowire.NotifyUtxosChangedResponseMessageH\x00\x12O\n\x18utxosChangedNotification\x18\x9b\x08 \x01(\x0b\x32*.protowire.UtxosChangedNotificationMessageH\x00\x12U\n\x1bgetUtxosByAddressesResponse\x18\x9d\x08 \x01(\x0b\x32-.protowire.GetUtxosByAddressesResponseMessageH\x00\x12O\n\x18getSinkBlueScoreResponse\x18\x9f\x08 \x01(\x0b\x32*.protowire.GetSinkBlueScoreResponseMessageH\x00\x12\x63\n\"notifySinkBlueScoreChangedResponse\x18\xa1\x08 \x01(\x0b\x32\x34.protowire.NotifySinkBlueScoreChangedResponseMessageH\x00\x12_\n sinkBlueScoreChangedNotification\x18\xa2\x08 \x01(\x0b\x32\x32.protowire.SinkBlueScoreChangedNotificationMessageH\x00\x12\x35\n\x0b\x62\x61nResponse\x18\xa4\x08 \x01(\x0b\x32\x1d.protowire.BanResponseMessageH\x00\x12\x39\n\runbanResponse\x18\xa6\x08 \x01(\x0b\x32\x1f.protowire.UnbanResponseMessageH\x00\x12=\n\x0fgetInfoResponse\x18\xa8\x08 \x01(\x0b\x32!.protowire.GetInfoResponseMessageH\x00\x12\x61\n!stopNotifyingUtxosChangedResponse\x18\xaa\x08 \x01(\x0b\x32\x33.protowire.StopNotifyingUtxosChangedResponseMessageH\x00\x12q\n)notifyPruningPointUtxoSetOverrideResponse\x18\xac\x08 \x01(\x0b\x32;.protowire.NotifyPruningPointUtxoSetOverrideResponseMessageH\x00\x12m\n\'pruningPointUtxoSetOverrideNotification\x18\xad\x08 \x01(\x0b\x32\x39.protowire.PruningPointUtxoSetOverrideNotificationMessageH\x00\x12\x7f\n0stopNotifyingPruningPointUtxoSetOverrideResponse\x18\xaf\x08 \x01(\x0b\x32\x42.protowire.StopNotifyingPruningPointUtxoSetOverrideResponseMessageH\x00\x12k\n&estimateNetworkHashesPerSecondResponse\x18\xb1\x08 \x01(\x0b\x32\x38.protowire.EstimateNetworkHashesPerSecondResponseMessageH\x00\x12g\n$notifyVirtualDaaScoreChangedResponse\x18\xb3\x08 \x01(\x0b\x32\x36.protowire.NotifyVirtualDaaScoreChangedResponseMessageH\x00\x12\x63\n\"virtualDaaScoreChangedNotification\x18\xb4\x08 \x01(\x0b\x32\x34.protowire.VirtualDaaScoreChangedNotificationMessageH\x00\x12U\n\x1bgetBalanceByAddressResponse\x18\xb6\x08 \x01(\x0b\x32-.protowire.GetBalanceByAddressResponseMessageH\x00\x12[\n\x1egetBalancesByAddressesResponse\x18\xb8\x08 \x01(\x0b\x32\x30.protowire.GetBalancesByAddressesResponseMessageH\x00\x12[\n\x1enotifyNewBlockTemplateResponse\x18\xba\x08 \x01(\x0b\x32\x30.protowire.NotifyNewBlockTemplateResponseMessageH\x00\x12W\n\x1cnewBlockTemplateNotification\x18\xbb\x08 \x01(\x0b\x32..protowire.NewBlockTemplateNotificationMessageH\x00\x12g\n$getMempoolEntriesByAddressesResponse\x18\xbd\x08 \x01(\x0b\x32\x36.protowire.GetMempoolEntriesByAddressesResponseMessageH\x00\x12I\n\x15getCoinSupplyResponse\x18\xbf\x08 \x01(\x0b\x32\'.protowire.GetCoinSupplyResponseMessageH\x00\x12\x37\n\x0cpingResponse\x18\xc1\x08 \x01(\x0b\x32\x1e.protowire.PingResponseMessageH\x00\x12\x43\n\x12getMetricsResponse\x18\xc3\x08 \x01(\x0b\x32$.protowire.GetMetricsResponseMessageH\x00\x12I\n\x15getServerInfoResponse\x18\xc5\x08 \x01(\x0b\x32\'.protowire.GetServerInfoResponseMessageH\x00\x12I\n\x15getSyncStatusResponse\x18\xc7\x08 \x01(\x0b\x32\'.protowire.GetSyncStatusResponseMessageH\x00\x12g\n$getDaaScoreTimestampEstimateResponse\x18\xc9\x08 \x01(\x0b\x32\x36.protowire.GetDaaScoreTimestampEstimateResponseMessageH\x00\x12g\n$submitTransactionReplacementResponse\x18\xcd\x08 \x01(\x0b\x32\x36.protowire.SubmitTransactionReplacementResponseMessageH\x00\x12K\n\x16getConnectionsResponse\x18\xcf\x08 \x01(\x0b\x32(.protowire.GetConnectionsResponseMessageH\x00\x12I\n\x15getSystemInfoResponse\x18\xd1\x08 \x01(\x0b\x32\'.protowire.GetSystemInfoResponseMessageH\x00\x12K\n\x16getFeeEstimateResponse\x18\xd3\x08 \x01(\x0b\x32(.protowire.GetFeeEstimateResponseMessageH\x00\x12\x63\n\"getFeeEstimateExperimentalResponse\x18\xd5\x08 \x01(\x0b\x32\x34.protowire.GetFeeEstimateExperimentalResponseMessageH\x00\x12W\n\x1cgetCurrentBlockColorResponse\x18\xd7\x08 \x01(\x0b\x32..protowire.GetCurrentBlockColorResponseMessageH\x00\x42\t\n\x07payload2U\n\x03RPC\x12N\n\rMessageStream\x12\x1a.protowire.SpectredRequest\x1a\x1b.protowire.SpectredResponse\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SPECTREDREQUEST']._serialized_start=41
  _globals['_SPECTREDREQUEST']._serialized_end=4163
  _globals['_SPECTREDRESPONSE']._serialized_start=4166
  _globals['_SPECTREDRESPONSE']._serialized_end=9234
  _globals['_RPC']._serialized_start=9236
  _globals['_RPC']._serialized_end=9321
# @@protoc_insertion_point(module_scope)
