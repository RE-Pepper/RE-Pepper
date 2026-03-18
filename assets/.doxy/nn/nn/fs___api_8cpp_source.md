

# File fs\_Api.cpp

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**sources**](dir_6ad72fc0abbc32b2f59992fddd21f3c1.md) **>** [**fs**](dir_097b33632b9d2d03ac5c68ff0a08f9ba.md) **>** [**fs\_Api.cpp**](fs___api_8cpp.md)

[Go to the documentation of this file](fs___api_8cpp.md)


```C++
#include <cstring>
#include <nn/err/CTR/err_Api.h>
#include <nn/fs/CTR/MPCore/detail/fs_UserFileSystem.h>
#include <nn/fs/detail/fs_FileSystemBase.h>
#include <nn/fs/fs_Api.h>
#include <nn/srv/srv_Api.h>

namespace nn {
namespace fs {

    namespace {
        nn::Handle s_FileServerSession;

        int /* ? */ s_FileSystemBaseImpl;
        detail::FileSystemBase s_FileSystemBase;
    } // namespace

} // namespace fs
} // namespace nn
```


