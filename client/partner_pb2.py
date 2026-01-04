# -*- coding: utf-8 -*-
# Generated-like protobuf module (handwritten to avoid grpc_tools dependency). DO NOT EDIT unless proto changes.
# source: partner.proto
"""Generated protocol buffer code (runtime-built descriptors)."""

from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.descriptor_pb2 import FieldDescriptorProto, FileDescriptorProto
from google.protobuf.internal import builder as _builder

_sym_db = _symbol_database.Default()

_fdp = FileDescriptorProto()
_fdp.name = "partner.proto"
_fdp.package = "partner"
_fdp.syntax = "proto3"

_get_partner_request = _fdp.message_type.add()
_get_partner_request.name = "GetPartnerRequest"
_f = _get_partner_request.field.add()
_f.name = "id"
_f.number = 1
_f.label = FieldDescriptorProto.LABEL_OPTIONAL
_f.type = FieldDescriptorProto.TYPE_STRING

_get_partner_response = _fdp.message_type.add()
_get_partner_response.name = "GetPartnerResponse"

_fields = [
    ("id", FieldDescriptorProto.TYPE_STRING, 1),
    ("userId", FieldDescriptorProto.TYPE_STRING, 2),
    ("naziv", FieldDescriptorProto.TYPE_STRING, 3),
    ("ulica", FieldDescriptorProto.TYPE_STRING, 4),
    ("kraj", FieldDescriptorProto.TYPE_STRING, 5),
    ("postnaSt", FieldDescriptorProto.TYPE_STRING, 6),
    ("poljubenNaslov", FieldDescriptorProto.TYPE_STRING, 7),
    ("ddvZavezanec", FieldDescriptorProto.TYPE_BOOL, 8),
    ("davcnaSt", FieldDescriptorProto.TYPE_STRING, 9),
    ("rokPlacila", FieldDescriptorProto.TYPE_INT32, 10),
    ("telefon", FieldDescriptorProto.TYPE_STRING, 11),
    ("ePosta", FieldDescriptorProto.TYPE_STRING, 12),
    ("spletnastran", FieldDescriptorProto.TYPE_STRING, 13),
    ("opombe", FieldDescriptorProto.TYPE_STRING, 14),
    ("eRacunNaslov", FieldDescriptorProto.TYPE_STRING, 15),
    ("eRacunId", FieldDescriptorProto.TYPE_STRING, 16),
    ("createdAt", FieldDescriptorProto.TYPE_STRING, 17),
    ("updatedAt", FieldDescriptorProto.TYPE_STRING, 18),
]

for _name, _type, _num in _fields:
    _f = _get_partner_response.field.add()
    _f.name = _name
    _f.number = _num
    _f.label = FieldDescriptorProto.LABEL_OPTIONAL
    _f.type = _type

_svc = _fdp.service.add()
_svc.name = "PartnerService"
_m = _svc.method.add()
_m.name = "GetPartner"
_m.input_type = ".partner.GetPartnerRequest"
_m.output_type = ".partner.GetPartnerResponse"

DESCRIPTOR = _descriptor_pool.Default().Add(_fdp)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "partner_pb2", _globals)


