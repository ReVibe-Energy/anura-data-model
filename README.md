# ReVibe Anura data model

This repo contains a protobuf based data model.
These data structures describe the raw vibration data, aggregates and events that are sent from the gateway to the broker endpoint.

## Codegen

Code generation is done using buf instead of raw protoc invocations.

- https://buf.build/
- https://docs.buf.build/introduction

To generate, run from root folder:

```shell
buf generate model
```

### Python

The regular python plugin generates code that doesn't allow for any code completion.
That's why this is using an alternative approach with betterproto (https://github.com/danielgtaylor/python-betterproto).

```shell
pip install "betterproto[compiler]==2.0.0b5"
```

To be evaluated / tested for compatibility when more complex structures and protobuf features are used.
