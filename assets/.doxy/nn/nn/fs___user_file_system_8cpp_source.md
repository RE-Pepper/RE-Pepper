

# File fs\_UserFileSystem.cpp

[**File List**](files.md) **>** [**CTR**](dir_7849431c7928768d2ea5b99ae6b7ec2d.md) **>** [**MPCore**](dir_2196d03e0de293840a64d7b974b5527c.md) **>** [**detail**](dir_b36ae53510e48c468601761e9e45f075.md) **>** [**fs\_UserFileSystem.cpp**](fs___user_file_system_8cpp.md)

[Go to the documentation of this file](fs___user_file_system_8cpp.md)


```C++
#include <nn/fs/CTR/MPCore/detail/fs_UserFileSystem.h>

namespace nn {
namespace fs {
    namespace CTR {
        namespace MPCore {
            namespace detail {
                namespace {
                    Handle g_FileServerHandle;
                } // namespace

                static bool s_Something = true;
                static bool s_IsLatencyEmulationEnable = false;
            } // namespace detail
        } // namespace MPCore
    } // namespace CTR

    void ForceDisableLatencyEmulation()
    {
        CTR::MPCore::detail::s_IsLatencyEmulationEnable = false;
    }

} // namespace fs
} // namespace nn
```


