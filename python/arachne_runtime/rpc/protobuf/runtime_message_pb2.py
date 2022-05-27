# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: runtime_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import stream_data_pb2 as stream__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15runtime_message.proto\x1a\x11stream_data.proto\"1\n\x0bInitRequest\x12\x0f\n\x07runtime\x18\x01 \x01(\t\x12\x11\n\targs_json\x18\x02 \x01(\t\"6\n\x05Index\x12\x11\n\x07index_i\x18\x01 \x01(\x05H\x00\x12\x11\n\x07index_s\x18\x02 \x01(\tH\x00\x42\x07\n\x05index\"R\n\x0fSetInputRequest\x12\x17\n\x05index\x18\x01 \x01(\x0b\x32\x06.IndexH\x00\x12\x1e\n\x0cnp_arr_chunk\x18\x02 \x01(\x0b\x32\x06.ChunkH\x00\x42\x06\n\x04\x64\x61ta\"B\n\x10\x42\x65nchmarkRequest\x12\x0e\n\x06warmup\x18\x01 \x01(\x05\x12\x0e\n\x06repeat\x18\x02 \x01(\x05\x12\x0e\n\x06number\x18\x03 \x01(\x05\"T\n\x11\x42\x65nchmarkResponse\x12\x0f\n\x07mean_ts\x18\x01 \x01(\x02\x12\x0e\n\x06std_ts\x18\x02 \x01(\x02\x12\x0e\n\x06max_ts\x18\x03 \x01(\x02\x12\x0e\n\x06min_ts\x18\x04 \x01(\x02\"!\n\x10GetOutputRequest\x12\r\n\x05index\x18\x01 \x01(\x05\"$\n\x11GetOutputResponse\x12\x0f\n\x07np_data\x18\x01 \x01(\x0c\"\x07\n\x05\x45mpty\"\x1f\n\x0f\x44\x65tailsResponse\x12\x0c\n\x04json\x18\x01 \x01(\tb\x06proto3')



_INITREQUEST = DESCRIPTOR.message_types_by_name['InitRequest']
_INDEX = DESCRIPTOR.message_types_by_name['Index']
_SETINPUTREQUEST = DESCRIPTOR.message_types_by_name['SetInputRequest']
_BENCHMARKREQUEST = DESCRIPTOR.message_types_by_name['BenchmarkRequest']
_BENCHMARKRESPONSE = DESCRIPTOR.message_types_by_name['BenchmarkResponse']
_GETOUTPUTREQUEST = DESCRIPTOR.message_types_by_name['GetOutputRequest']
_GETOUTPUTRESPONSE = DESCRIPTOR.message_types_by_name['GetOutputResponse']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_DETAILSRESPONSE = DESCRIPTOR.message_types_by_name['DetailsResponse']
InitRequest = _reflection.GeneratedProtocolMessageType('InitRequest', (_message.Message,), {
  'DESCRIPTOR' : _INITREQUEST,
  '__module__' : 'runtime_message_pb2'
  # @@protoc_insertion_point(class_scope:InitRequest)
  })
_sym_db.RegisterMessage(InitRequest)

Index = _reflection.GeneratedProtocolMessageType('Index', (_message.Message,), {
  'DESCRIPTOR' : _INDEX,
  '__module__' : 'runtime_message_pb2'
  # @@protoc_insertion_point(class_scope:Index)
  })
_sym_db.RegisterMessage(Index)

SetInputRequest = _reflection.GeneratedProtocolMessageType('SetInputRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETINPUTREQUEST,
  '__module__' : 'runtime_message_pb2'
  # @@protoc_insertion_point(class_scope:SetInputRequest)
  })
_sym_db.RegisterMessage(SetInputRequest)

BenchmarkRequest = _reflection.GeneratedProtocolMessageType('BenchmarkRequest', (_message.Message,), {
  'DESCRIPTOR' : _BENCHMARKREQUEST,
  '__module__' : 'runtime_message_pb2'
  # @@protoc_insertion_point(class_scope:BenchmarkRequest)
  })
_sym_db.RegisterMessage(BenchmarkRequest)

BenchmarkResponse = _reflection.GeneratedProtocolMessageType('BenchmarkResponse', (_message.Message,), {
  'DESCRIPTOR' : _BENCHMARKRESPONSE,
  '__module__' : 'runtime_message_pb2'
  # @@protoc_insertion_point(class_scope:BenchmarkResponse)
  })
_sym_db.RegisterMessage(BenchmarkResponse)

GetOutputRequest = _reflection.GeneratedProtocolMessageType('GetOutputRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOUTPUTREQUEST,
  '__module__' : 'runtime_message_pb2'
  # @@protoc_insertion_point(class_scope:GetOutputRequest)
  })
_sym_db.RegisterMessage(GetOutputRequest)

GetOutputResponse = _reflection.GeneratedProtocolMessageType('GetOutputResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETOUTPUTRESPONSE,
  '__module__' : 'runtime_message_pb2'
  # @@protoc_insertion_point(class_scope:GetOutputResponse)
  })
_sym_db.RegisterMessage(GetOutputResponse)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'runtime_message_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

DetailsResponse = _reflection.GeneratedProtocolMessageType('DetailsResponse', (_message.Message,), {
  'DESCRIPTOR' : _DETAILSRESPONSE,
  '__module__' : 'runtime_message_pb2'
  # @@protoc_insertion_point(class_scope:DetailsResponse)
  })
_sym_db.RegisterMessage(DetailsResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INITREQUEST._serialized_start=44
  _INITREQUEST._serialized_end=93
  _INDEX._serialized_start=95
  _INDEX._serialized_end=149
  _SETINPUTREQUEST._serialized_start=151
  _SETINPUTREQUEST._serialized_end=233
  _BENCHMARKREQUEST._serialized_start=235
  _BENCHMARKREQUEST._serialized_end=301
  _BENCHMARKRESPONSE._serialized_start=303
  _BENCHMARKRESPONSE._serialized_end=387
  _GETOUTPUTREQUEST._serialized_start=389
  _GETOUTPUTREQUEST._serialized_end=422
  _GETOUTPUTRESPONSE._serialized_start=424
  _GETOUTPUTRESPONSE._serialized_end=460
  _EMPTY._serialized_start=462
  _EMPTY._serialized_end=469
  _DETAILSRESPONSE._serialized_start=471
  _DETAILSRESPONSE._serialized_end=502
# @@protoc_insertion_point(module_scope)
