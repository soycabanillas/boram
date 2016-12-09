{
  "targets": [
    {
      "target_name": "mpvinterop",
      "sources": ["src/mpv/mpvinterop.cc"],
      "libraries": ["ppapi", "ppapi_cpp", "ppapi_gles2"],
      "conditions": [
        ["OS=='linux'", {
          "defines": ["_GLIBCXX_USE_CXX11_ABI=0"],
          "include_dirs": ["$(NACL_SDK_ROOT)/include"],
          "library_dirs": ["$(NACL_SDK_ROOT)/lib/linux_host/Release"],
          "libraries": ["mpv"],
          "ldflags": ["-static-libstdc++"],
        }, "OS=='win'", {
          "defines": ["BORAM_WIN_BUILD"],
          "include_dirs": ["C:/nacl_sdk/pepper_49/include", "C:/mpv-dev/include"],
          "library_dirs": ["C:/nacl_sdk/pepper_49/lib/win_x86_32_host/Release", "C:/mpv-dev/32"],
          "libraries": ["libmpv.dll.a"],
        }],
      ],
    },
  ],
  "conditions": [
    ["OS=='linux'", {
      "targets": [
        {
          "target_name": "ffmpeg",
          "libraries": ["-lavcodec", "-lavformat", "-lavutil"],
        },
      ],
    }],
  ],
}