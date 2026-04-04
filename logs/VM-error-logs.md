From https://github.com/AetharaAI/Aether_Runner
   e1bfd65..9068efa  main       -> origin/main
Updating e1bfd65..9068efa
Fast-forward
 config/runner.yaml         | 4 ++--
 pyproject.toml             | 3 ++-
 requirements-inference.txt | 1 +
 3 files changed, 5 insertions(+), 3 deletions(-)
WARN[0000] Warning: No resource found to remove for project "aether_runner". 
[+] Building 108.3s (14/14) FINISHED                                                                                                                                  
 => [internal] load local bake definitions                                                                                                                       0.0s
 => => reading from stdin 677B                                                                                                                                   0.0s
 => [internal] load build definition from Dockerfile                                                                                                             0.0s
 => => transferring dockerfile: 593B                                                                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                              0.5s
 => [internal] load .dockerignore                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                  0.0s
 => [1/7] FROM docker.io/library/python:3.11-slim@sha256:9358444059ed78e2975ada2c189f1c1a3144a5dab6f35bff8c981afb38946634                                        0.0s
 => [internal] load build context                                                                                                                                0.0s
 => => transferring context: 21.89kB                                                                                                                             0.0s
 => CACHED [2/7] WORKDIR /app                                                                                                                                    0.0s
 => [3/7] RUN apt-get update && apt-get install -y --no-install-recommends     ffmpeg     && rm -rf /var/lib/apt/lists/*                                        22.4s
 => [4/7] COPY requirements.txt requirements-inference.txt ./                                                                                                    0.0s 
 => [5/7] RUN pip install --no-cache-dir -r requirements.txt                                                                                                     7.7s 
 => [6/7] RUN if [ "true" = "true" ]; then pip install --no-cache-dir -r requirements-inference.txt; fi                                                         67.7s 
 => [7/7] COPY . .                                                                                                                                               0.0s 
 => exporting to image                                                                                                                                           9.9s 
 => => exporting layers                                                                                                                                          9.9s 
 => => writing image sha256:154cb669abd7d605a59c846dcf3b29a6627c7a03f1b028f4327abba1fc914ec1                                                                     0.0s 
 => => naming to docker.io/library/aether-runner:latest                                                                                                          0.0s 
 => resolving provenance for metadata file                                                                                                                       0.0s 
[+] build 1/1
 ✔ Image aether-runner:latest Built                                                                                                                             108.4s
[+] up 1/1
 ✔ Container gemma-4-31b-it Started                                                                                                                               0.6s
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 36, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma.py", line 120, in __init__
gemma-4-31b-it  |     self.sp_model.Load(vocab_file)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 961, in Load
gemma-4-31b-it  |     return self.LoadFromFile(model_file)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 316, in LoadFromFile
gemma-4-31b-it  |     return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | TypeError: not a string
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 43, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2360, in _from_pretrained
gemma-4-31b-it  |     except import_protobuf_decode_error():
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 88, in import_protobuf_decode_error
gemma-4-31b-it  |     raise ImportError(PROTOBUF_IMPORT_ERROR.format(error_message))
gemma-4-31b-it  | ImportError: 
gemma-4-31b-it  |  requires the protobuf library but it was not found in your environment. Check out the instructions on the
gemma-4-31b-it  | installation page of its repo: https://github.com/protocolbuffers/protobuf/tree/master/python#installation and follow the ones
gemma-4-31b-it  | that match your environment. Please note that you may need to restart your runtime after installation.
gemma-4-31b-it  | 
gemma-4-31b-it exited with code 1 (restarting)
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 36, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma.py", line 120, in __init__
gemma-4-31b-it  |     self.sp_model.Load(vocab_file)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 961, in Load
gemma-4-31b-it  |     return self.LoadFromFile(model_file)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 316, in LoadFromFile
gemma-4-31b-it  |     return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | TypeError: not a string
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 43, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2360, in _from_pretrained
gemma-4-31b-it  |     except import_protobuf_decode_error():
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 88, in import_protobuf_decode_error
gemma-4-31b-it  |     raise ImportError(PROTOBUF_IMPORT_ERROR.format(error_message))
gemma-4-31b-it  | ImportError: 
gemma-4-31b-it  |  requires the protobuf library but it was not found in your environment. Check out the instructions on the
gemma-4-31b-it  | installation page of its repo: https://github.com/protocolbuffers/protobuf/tree/master/python#installation and follow the ones
gemma-4-31b-it  | that match your environment. Please note that you may need to restart your runtime after installation.
gemma-4-31b-it  | 
gemma-4-31b-it exited with code 1 (restarting)
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 36, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma.py", line 120, in __init__
gemma-4-31b-it  |     self.sp_model.Load(vocab_file)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 961, in Load
gemma-4-31b-it  |     return self.LoadFromFile(model_file)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 316, in LoadFromFile
gemma-4-31b-it  |     return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | TypeError: not a string
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 43, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2360, in _from_pretrained
gemma-4-31b-it  |     except import_protobuf_decode_error():
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 88, in import_protobuf_decode_error
gemma-4-31b-it  |     raise ImportError(PROTOBUF_IMPORT_ERROR.format(error_message))
gemma-4-31b-it  | ImportError: 
gemma-4-31b-it  |  requires the protobuf library but it was not found in your environment. Check out the instructions on the
gemma-4-31b-it  | installation page of its repo: https://github.com/protocolbuffers/protobuf/tree/master/python#installation and follow the ones
gemma-4-31b-it  | that match your environment. Please note that you may need to restart your runtime after installation.
gemma-4-31b-it  | 
gemma-4-31b-it exited with code 1 (restarting)
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 36, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma.py", line 120, in __init__
gemma-4-31b-it  |     self.sp_model.Load(vocab_file)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 961, in Load
gemma-4-31b-it  |     return self.LoadFromFile(model_file)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 316, in LoadFromFile
gemma-4-31b-it  |     return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | TypeError: not a string
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 43, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2360, in _from_pretrained
gemma-4-31b-it  |     except import_protobuf_decode_error():
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 88, in import_protobuf_decode_error
gemma-4-31b-it  |     raise ImportError(PROTOBUF_IMPORT_ERROR.format(error_message))
gemma-4-31b-it  | ImportError: 
gemma-4-31b-it  |  requires the protobuf library but it was not found in your environment. Check out the instructions on the
gemma-4-31b-it  | installation page of its repo: https://github.com/protocolbuffers/protobuf/tree/master/python#installation and follow the ones
gemma-4-31b-it  | that match your environment. Please note that you may need to restart your runtime after installation.
gemma-4-31b-it  | 
gemma-4-31b-it exited with code 1 (restarting)
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 36, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma.py", line 120, in __init__
gemma-4-31b-it  |     self.sp_model.Load(vocab_file)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 961, in Load
gemma-4-31b-it  |     return self.LoadFromFile(model_file)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 316, in LoadFromFile
gemma-4-31b-it  |     return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | TypeError: not a string
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 43, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2360, in _from_pretrained
gemma-4-31b-it  |     except import_protobuf_decode_error():
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 88, in import_protobuf_decode_error
gemma-4-31b-it  |     raise ImportError(PROTOBUF_IMPORT_ERROR.format(error_message))
gemma-4-31b-it  | ImportError: 
gemma-4-31b-it  |  requires the protobuf library but it was not found in your environment. Check out the instructions on the
gemma-4-31b-it  | installation page of its repo: https://github.com/protocolbuffers/protobuf/tree/master/python#installation and follow the ones
gemma-4-31b-it  | that match your environment. Please note that you may need to restart your runtime after installation.
gemma-4-31b-it  | 
gemma-4-31b-it exited with code 1
ubuntu@l40s-180-us-west-or-1:~/aether-model-node/control/Aether_Runner$ git pull
docker compose down
docker compose build --no-cache
docker compose up -d
docker compose logs -f
remote: Enumerating objects: 13, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 7 (delta 6), reused 7 (delta 6), pack-reused 0 (from 0)
Unpacking objects: 100% (7/7), 710 bytes | 710.00 KiB/s, done.
From https://github.com/AetharaAI/Aether_Runner
   9068efa..9a596ae  main       -> origin/main
Updating 9068efa..9a596ae
Fast-forward
 aether_runner/backends/transformers_backend.py | 19 ++++++++++++++-----
 pyproject.toml                                 |  3 ++-
 requirements-inference.txt                     |  1 +
 3 files changed, 17 insertions(+), 6 deletions(-)
WARN[0000] Warning: No resource found to remove for project "aether_runner". 
[+] Building 103.5s (14/14) FINISHED                                                                                                                                  
 => [internal] load local bake definitions                                                                                                                       0.0s
 => => reading from stdin 677B                                                                                                                                   0.0s
 => [internal] load build definition from Dockerfile                                                                                                             0.0s
 => => transferring dockerfile: 593B                                                                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                              0.3s
 => [internal] load .dockerignore                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                  0.0s
 => [1/7] FROM docker.io/library/python:3.11-slim@sha256:9358444059ed78e2975ada2c189f1c1a3144a5dab6f35bff8c981afb38946634                                        0.0s
 => [internal] load build context                                                                                                                                0.0s
 => => transferring context: 26.02kB                                                                                                                             0.0s
 => CACHED [2/7] WORKDIR /app                                                                                                                                    0.0s
 => [3/7] RUN apt-get update && apt-get install -y --no-install-recommends     ffmpeg     && rm -rf /var/lib/apt/lists/*                                        23.1s
 => [4/7] COPY requirements.txt requirements-inference.txt ./                                                                                                    0.0s 
 => [5/7] RUN pip install --no-cache-dir -r requirements.txt                                                                                                     7.7s 
 => [6/7] RUN if [ "true" = "true" ]; then pip install --no-cache-dir -r requirements-inference.txt; fi                                                         62.4s 
 => [7/7] COPY . .                                                                                                                                               0.0s 
 => exporting to image                                                                                                                                           9.9s 
 => => exporting layers                                                                                                                                          9.9s 
 => => writing image sha256:808c1b57625284a8f7cffb52256d818c827f3651f60f0e6b4abf24d92236aec5                                                                     0.0s 
 => => naming to docker.io/library/aether-runner:latest                                                                                                          0.0s 
 => resolving provenance for metadata file                                                                                                                       0.0s 
[+] build 1/1
 ✔ Image aether-runner:latest Built                                                                                                                             103.5s
[+] up 1/1
 ✔ Container gemma-4-31b-it Started                                                                                                                               0.6s
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 36, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 45, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma_fast.py", line 100, in __init__
gemma-4-31b-it  |     super().__init__(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_fast.py", line 178, in __init__
gemma-4-31b-it  |     super().__init__(**kwargs)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1472, in __init__
gemma-4-31b-it  |     self._set_model_specific_special_tokens(special_tokens=self.extra_special_tokens)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1210, in _set_model_specific_special_tokens
gemma-4-31b-it  |     self.SPECIAL_TOKENS_ATTRIBUTES = self.SPECIAL_TOKENS_ATTRIBUTES + list(special_tokens.keys())
gemma-4-31b-it  |                                                                            ^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | AttributeError: 'list' object has no attribute 'keys'
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 52, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma.py", line 120, in __init__
gemma-4-31b-it  |     self.sp_model.Load(vocab_file)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 961, in Load
gemma-4-31b-it  |     return self.LoadFromFile(model_file)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 316, in LoadFromFile
gemma-4-31b-it  |     return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | TypeError: not a string
gemma-4-31b-it exited with code 1 (restarting)
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 36, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 45, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma_fast.py", line 100, in __init__
gemma-4-31b-it  |     super().__init__(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_fast.py", line 178, in __init__
gemma-4-31b-it  |     super().__init__(**kwargs)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1472, in __init__
gemma-4-31b-it  |     self._set_model_specific_special_tokens(special_tokens=self.extra_special_tokens)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1210, in _set_model_specific_special_tokens
gemma-4-31b-it  |     self.SPECIAL_TOKENS_ATTRIBUTES = self.SPECIAL_TOKENS_ATTRIBUTES + list(special_tokens.keys())
gemma-4-31b-it  |                                                                            ^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | AttributeError: 'list' object has no attribute 'keys'
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 52, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma.py", line 120, in __init__
gemma-4-31b-it  |     self.sp_model.Load(vocab_file)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 961, in Load
gemma-4-31b-it  |     return self.LoadFromFile(model_file)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 316, in LoadFromFile
gemma-4-31b-it  |     return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | TypeError: not a string
gemma-4-31b-it exited with code 1 (restarting)
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 36, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 45, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma_fast.py", line 100, in __init__
gemma-4-31b-it  |     super().__init__(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_fast.py", line 178, in __init__
gemma-4-31b-it  |     super().__init__(**kwargs)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1472, in __init__
gemma-4-31b-it  |     self._set_model_specific_special_tokens(special_tokens=self.extra_special_tokens)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1210, in _set_model_specific_special_tokens
gemma-4-31b-it  |     self.SPECIAL_TOKENS_ATTRIBUTES = self.SPECIAL_TOKENS_ATTRIBUTES + list(special_tokens.keys())
gemma-4-31b-it  |                                                                            ^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | AttributeError: 'list' object has no attribute 'keys'
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 52, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma.py", line 120, in __init__
gemma-4-31b-it  |     self.sp_model.Load(vocab_file)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 961, in Load
gemma-4-31b-it  |     return self.LoadFromFile(model_file)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 316, in LoadFromFile
gemma-4-31b-it  |     return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | TypeError: not a string
gemma-4-31b-it exited with code 1 (restarting)
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 36, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 45, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma_fast.py", line 100, in __init__
gemma-4-31b-it  |     super().__init__(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_fast.py", line 178, in __init__
gemma-4-31b-it  |     super().__init__(**kwargs)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1472, in __init__
gemma-4-31b-it  |     self._set_model_specific_special_tokens(special_tokens=self.extra_special_tokens)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1210, in _set_model_specific_special_tokens
gemma-4-31b-it  |     self.SPECIAL_TOKENS_ATTRIBUTES = self.SPECIAL_TOKENS_ATTRIBUTES + list(special_tokens.keys())
gemma-4-31b-it  |                                                                            ^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | AttributeError: 'list' object has no attribute 'keys'
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 52, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma.py", line 120, in __init__
gemma-4-31b-it  |     self.sp_model.Load(vocab_file)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 961, in Load
gemma-4-31b-it  |     return self.LoadFromFile(model_file)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 316, in LoadFromFile
gemma-4-31b-it  |     return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | TypeError: not a string
gemma-4-31b-it exited with code 1 (restarting)
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 36, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 45, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma_fast.py", line 100, in __init__
gemma-4-31b-it  |     super().__init__(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_fast.py", line 178, in __init__
gemma-4-31b-it  |     super().__init__(**kwargs)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1472, in __init__
gemma-4-31b-it  |     self._set_model_specific_special_tokens(special_tokens=self.extra_special_tokens)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1210, in _set_model_specific_special_tokens
gemma-4-31b-it  |     self.SPECIAL_TOKENS_ATTRIBUTES = self.SPECIAL_TOKENS_ATTRIBUTES + list(special_tokens.keys())
gemma-4-31b-it  |                                                                            ^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | AttributeError: 'list' object has no attribute 'keys'
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 52, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma.py", line 120, in __init__
gemma-4-31b-it  |     self.sp_model.Load(vocab_file)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 961, in Load
gemma-4-31b-it  |     return self.LoadFromFile(model_file)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/sentencepiece/__init__.py", line 316, in LoadFromFile
gemma-4-31b-it  |     return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | TypeError: not a string
gemma-4-31b-it exited with code 1
ubuntu@l40s-180-us-west-or-1:~/aether-model-node/control/Aether_Runner$ git pull
docker compose down
docker compose build --no-cache
docker compose up -d
docker compose logs -f
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 5 (delta 4), reused 5 (delta 4), pack-reused 0 (from 0)
Unpacking objects: 100% (5/5), 1.11 KiB | 1.11 MiB/s, done.
From https://github.com/AetharaAI/Aether_Runner
   9a596ae..ec0bf34  main       -> origin/main
Updating 9a596ae..ec0bf34
Fast-forward
 aether_runner/backends/transformers_backend.py | 51 +++++++++++++++++++++++++++++++++++++++++++++------
 1 file changed, 45 insertions(+), 6 deletions(-)
WARN[0000] Warning: No resource found to remove for project "aether_runner". 
[+] Building 110.5s (14/14) FINISHED                                                                                                                                  
 => [internal] load local bake definitions                                                                                                                       0.0s
 => => reading from stdin 677B                                                                                                                                   0.0s
 => [internal] load build definition from Dockerfile                                                                                                             0.0s
 => => transferring dockerfile: 593B                                                                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                              0.4s
 => [internal] load .dockerignore                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                  0.0s
 => [1/7] FROM docker.io/library/python:3.11-slim@sha256:9358444059ed78e2975ada2c189f1c1a3144a5dab6f35bff8c981afb38946634                                        0.0s
 => [internal] load build context                                                                                                                                0.0s
 => => transferring context: 27.55kB                                                                                                                             0.0s
 => CACHED [2/7] WORKDIR /app                                                                                                                                    0.0s
 => [3/7] RUN apt-get update && apt-get install -y --no-install-recommends     ffmpeg     && rm -rf /var/lib/apt/lists/*                                        22.2s
 => [4/7] COPY requirements.txt requirements-inference.txt ./                                                                                                    0.0s 
 => [5/7] RUN pip install --no-cache-dir -r requirements.txt                                                                                                     7.7s 
 => [6/7] RUN if [ "true" = "true" ]; then pip install --no-cache-dir -r requirements-inference.txt; fi                                                         69.7s 
 => [7/7] COPY . .                                                                                                                                               0.1s 
 => exporting to image                                                                                                                                          10.2s 
 => => exporting layers                                                                                                                                         10.2s 
 => => writing image sha256:c47b56cfb6ef0156a7774a5851233c6f8ca2c12ba09eb1f86aef9441233a576c                                                                     0.0s 
 => => naming to docker.io/library/aether-runner:latest                                                                                                          0.0s 
 => resolving provenance for metadata file                                                                                                                       0.0s 
[+] build 1/1
 ✔ Image aether-runner:latest Built                                                                                                                             110.6s
[+] up 1/1
 ✔ Container gemma-4-31b-it Started                                                                                                                               0.6s
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 39, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 48, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma_fast.py", line 100, in __init__
gemma-4-31b-it  |     super().__init__(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_fast.py", line 178, in __init__
gemma-4-31b-it  |     super().__init__(**kwargs)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1472, in __init__
gemma-4-31b-it  |     self._set_model_specific_special_tokens(special_tokens=self.extra_special_tokens)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1210, in _set_model_specific_special_tokens
gemma-4-31b-it  |     self.SPECIAL_TOKENS_ATTRIBUTES = self.SPECIAL_TOKENS_ATTRIBUTES + list(special_tokens.keys())
gemma-4-31b-it  |                                                                            ^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | AttributeError: 'list' object has no attribute 'keys'
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 56, in load
gemma-4-31b-it  |     self._tokenizer = self._load_patched_fast_tokenizer(auto_tokenizer)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 100, in _load_patched_fast_tokenizer
gemma-4-31b-it  |     return auto_tokenizer.from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma_fast.py", line 100, in __init__
gemma-4-31b-it  |     super().__init__(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_fast.py", line 117, in __init__
gemma-4-31b-it  |     fast_tokenizer = TokenizerFast.from_file(fast_tokenizer_file)
gemma-4-31b-it  |                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | Exception: No such file or directory (os error 2)
gemma-4-31b-it exited with code 1 (restarting)
gemma-4-31b-it  | Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 39, in load
gemma-4-31b-it  |     self._processor = auto_processor.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/processing_auto.py", line 424, in from_pretrained
gemma-4-31b-it  |     raise ValueError(
gemma-4-31b-it  | ValueError: Unrecognized processing class in /models/cyankiwi/gemma-4-31B-it-AWQ-4bit. Can't instantiate a processor, a tokenizer, an image processor or a feature extractor for this model. Make sure the repository contains the files of at least one of those processing classes.
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 48, in load
gemma-4-31b-it  |     self._tokenizer = auto_tokenizer.from_pretrained(
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma_fast.py", line 100, in __init__
gemma-4-31b-it  |     super().__init__(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_fast.py", line 178, in __init__
gemma-4-31b-it  |     super().__init__(**kwargs)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1472, in __init__
gemma-4-31b-it  |     self._set_model_specific_special_tokens(special_tokens=self.extra_special_tokens)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 1210, in _set_model_specific_special_tokens
gemma-4-31b-it  |     self.SPECIAL_TOKENS_ATTRIBUTES = self.SPECIAL_TOKENS_ATTRIBUTES + list(special_tokens.keys())
gemma-4-31b-it  |                                                                            ^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | AttributeError: 'list' object has no attribute 'keys'
gemma-4-31b-it  | 
gemma-4-31b-it  | During handling of the above exception, another exception occurred:
gemma-4-31b-it  | 
gemma-4-31b-it  | Traceback (most recent call last):
gemma-4-31b-it  |   File "/usr/local/bin/uvicorn", line 8, in <module>
gemma-4-31b-it  |     sys.exit(main())
gemma-4-31b-it  |              ^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
gemma-4-31b-it  |     return self.main(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
gemma-4-31b-it  |     rv = self.invoke(ctx)
gemma-4-31b-it  |          ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
gemma-4-31b-it  |     return ctx.invoke(self.callback, **ctx.params)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
gemma-4-31b-it  |     return callback(*args, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 433, in main
gemma-4-31b-it  |     run(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 606, in run
gemma-4-31b-it  |     server.run()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 75, in run
gemma-4-31b-it  |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
gemma-4-31b-it  |     return runner.run(main)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
gemma-4-31b-it  |     return self._loop.run_until_complete(task)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 79, in serve
gemma-4-31b-it  |     await self._serve(sockets)
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 86, in _serve
gemma-4-31b-it  |     config.load()
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 441, in load
gemma-4-31b-it  |     self.loaded_app = import_from_string(self.app)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
gemma-4-31b-it  |     module = importlib.import_module(module_str)
gemma-4-31b-it  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
gemma-4-31b-it  |     return _bootstrap._gcd_import(name[level:], package, level)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
gemma-4-31b-it  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
gemma-4-31b-it  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
gemma-4-31b-it  |   File "/app/aether_runner/main.py", line 31, in <module>
gemma-4-31b-it  |     model_registry.load()
gemma-4-31b-it  |   File "/app/aether_runner/services/model_registry.py", line 41, in load
gemma-4-31b-it  |     adapter.maybe_load(eager=self.eager_load)
gemma-4-31b-it  |   File "/app/aether_runner/adapters/generic_hf.py", line 24, in maybe_load
gemma-4-31b-it  |     self.backend.load()
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 56, in load
gemma-4-31b-it  |     self._tokenizer = self._load_patched_fast_tokenizer(auto_tokenizer)
gemma-4-31b-it  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/app/aether_runner/backends/transformers_backend.py", line 100, in _load_patched_fast_tokenizer
gemma-4-31b-it  |     return auto_tokenizer.from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/auto/tokenization_auto.py", line 1156, in from_pretrained
gemma-4-31b-it  |     return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2113, in from_pretrained
gemma-4-31b-it  |     return cls._from_pretrained(
gemma-4-31b-it  |            ^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_base.py", line 2359, in _from_pretrained
gemma-4-31b-it  |     tokenizer = cls(*init_inputs, **init_kwargs)
gemma-4-31b-it  |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/models/gemma/tokenization_gemma_fast.py", line 100, in __init__
gemma-4-31b-it  |     super().__init__(
gemma-4-31b-it  |   File "/usr/local/lib/python3.11/site-packages/transformers/tokenization_utils_fast.py", line 117, in __init__
gemma-4-31b-it  |     fast_tokenizer = TokenizerFast.from_file(fast_tokenizer_file)
gemma-4-31b-it  |                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gemma-4-31b-it  | Exception: No such file or directory (os error 2)
gemma-4-31b-it exited with code 137
ubuntu@l40s-180-us-west-or-1:~/