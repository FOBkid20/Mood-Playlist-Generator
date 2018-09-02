# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/vision_v1/proto/geometry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/vision_v1/proto/geometry.proto',
  package='google.cloud.vision.v1',
  syntax='proto3',
  serialized_pb=_b('\n+google/cloud/vision_v1/proto/geometry.proto\x12\x16google.cloud.vision.v1\"\x1e\n\x06Vertex\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"\x87\x01\n\x0c\x42oundingPoly\x12\x30\n\x08vertices\x18\x01 \x03(\x0b\x32\x1e.google.cloud.vision.v1.Vertex\x12\x45\n\x13normalized_vertices\x18\x02 \x03(\x0b\x32(.google.cloud.vision.v1.NormalizedVertex\"+\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x42u\n\x1a\x63om.google.cloud.vision.v1B\rGeometryProtoP\x01Z<google.golang.org/genproto/googleapis/cloud/vision/v1;vision\xf8\x01\x01\xa2\x02\x04GCVNb\x06proto3')
)




_VERTEX = _descriptor.Descriptor(
  name='Vertex',
  full_name='google.cloud.vision.v1.Vertex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='google.cloud.vision.v1.Vertex.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='google.cloud.vision.v1.Vertex.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=101,
)


_NORMALIZEDVERTEX = _descriptor.Descriptor(
  name='NormalizedVertex',
  full_name='google.cloud.vision.v1.NormalizedVertex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='google.cloud.vision.v1.NormalizedVertex.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='google.cloud.vision.v1.NormalizedVertex.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=143,
)


_BOUNDINGPOLY = _descriptor.Descriptor(
  name='BoundingPoly',
  full_name='google.cloud.vision.v1.BoundingPoly',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertices', full_name='google.cloud.vision.v1.BoundingPoly.vertices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normalized_vertices', full_name='google.cloud.vision.v1.BoundingPoly.normalized_vertices', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=281,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='google.cloud.vision.v1.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='google.cloud.vision.v1.Position.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='google.cloud.vision.v1.Position.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='google.cloud.vision.v1.Position.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=326,
)

_BOUNDINGPOLY.fields_by_name['vertices'].message_type = _VERTEX
_BOUNDINGPOLY.fields_by_name['normalized_vertices'].message_type = _NORMALIZEDVERTEX
DESCRIPTOR.message_types_by_name['Vertex'] = _VERTEX
DESCRIPTOR.message_types_by_name['NormalizedVertex'] = _NORMALIZEDVERTEX
DESCRIPTOR.message_types_by_name['BoundingPoly'] = _BOUNDINGPOLY
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vertex = _reflection.GeneratedProtocolMessageType('Vertex', (_message.Message,), dict(
  DESCRIPTOR = _VERTEX,
  __module__ = 'google.cloud.vision_v1.proto.geometry_pb2'
  ,
  __doc__ = """X coordinate.
  
  
  Attributes:
      y:
          Y coordinate.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.vision.v1.Vertex)
  ))
_sym_db.RegisterMessage(Vertex)

NormalizedVertex = _reflection.GeneratedProtocolMessageType('NormalizedVertex', (_message.Message,), dict(
  DESCRIPTOR = _NORMALIZEDVERTEX,
  __module__ = 'google.cloud.vision_v1.proto.geometry_pb2'
  ,
  __doc__ = """X coordinate.
  
  
  Attributes:
      y:
          Y coordinate.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.vision.v1.NormalizedVertex)
  ))
_sym_db.RegisterMessage(NormalizedVertex)

BoundingPoly = _reflection.GeneratedProtocolMessageType('BoundingPoly', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDINGPOLY,
  __module__ = 'google.cloud.vision_v1.proto.geometry_pb2'
  ,
  __doc__ = """A bounding polygon for the detected image annotation.
  
  
  Attributes:
      vertices:
          The bounding polygon vertices.
      normalized_vertices:
          The bounding polygon normalized vertices.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.vision.v1.BoundingPoly)
  ))
_sym_db.RegisterMessage(BoundingPoly)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'google.cloud.vision_v1.proto.geometry_pb2'
  ,
  __doc__ = """A 3D position in the image, used primarily for Face detection landmarks.
  A valid Position must have both x and y coordinates. The position
  coordinates are in the same scale as the original image.
  
  
  Attributes:
      x:
          X coordinate.
      y:
          Y coordinate.
      z:
          Z coordinate (or depth).
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.vision.v1.Position)
  ))
_sym_db.RegisterMessage(Position)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.google.cloud.vision.v1B\rGeometryProtoP\001Z<google.golang.org/genproto/googleapis/cloud/vision/v1;vision\370\001\001\242\002\004GCVN'))
# @@protoc_insertion_point(module_scope)
