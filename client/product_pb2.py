# -*- coding: utf-8 -*-
# Generated-like protobuf module (handwritten to avoid grpc_tools dependency). DO NOT EDIT unless proto changes.
# source: product.proto
"""Generated protocol buffer code (runtime-built descriptors)."""

from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.descriptor_pb2 import FieldDescriptorProto, FileDescriptorProto
from google.protobuf.internal import builder as _builder

_sym_db = _symbol_database.Default()

_fdp = FileDescriptorProto()
_fdp.name = "product.proto"
_fdp.package = "product"
_fdp.syntax = "proto3"

_get_product_request = _fdp.message_type.add()
_get_product_request.name = "GetProductRequest"
_f = _get_product_request.field.add()
_f.name = "id"
_f.number = 1
_f.label = FieldDescriptorProto.LABEL_OPTIONAL
_f.type = FieldDescriptorProto.TYPE_STRING

_get_product_response = _fdp.message_type.add()
_get_product_response.name = "GetProductResponse"
for _idx, _name in enumerate(
    [
        "id",
        "companyId",
        "name",
        "cost",
        "measuringUnit",
        "ddvPercentage",
        "createdAt",
        "updatedAt",
    ],
    start=1,
):
    _f = _get_product_response.field.add()
    _f.name = _name
    _f.number = _idx
    _f.label = FieldDescriptorProto.LABEL_OPTIONAL
    _f.type = FieldDescriptorProto.TYPE_STRING

_svc = _fdp.service.add()
_svc.name = "ProductService"
_m = _svc.method.add()
_m.name = "GetProduct"
_m.input_type = ".product.GetProductRequest"
_m.output_type = ".product.GetProductResponse"

DESCRIPTOR = _descriptor_pool.Default().Add(_fdp)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "product_pb2", _globals)


