

# File srv\_Api.cpp

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**sources**](dir_6ad72fc0abbc32b2f59992fddd21f3c1.md) **>** [**srv**](dir_9265a2f0e35d56b43a6785601066bd6e.md) **>** [**srv\_Api.cpp**](srv___api_8cpp.md)

[Go to the documentation of this file](srv___api_8cpp.md)


```C++
#include <nn/srv/detail/srv_Service.h>
#include <nn/srv/srv_Api.h>

namespace nn {
namespace srv {

    namespace {

        static int s_InitializeCount = 0;

    } // namespace

    #ifdef NON_MATCHING
    Result GetServiceHandle(Handle* out, const char* service, s32 r2, u32 r3)
    {
        if (s_InitializeCount > 0)
            return Result(Result::Level_Permanent, Result::Summary_InvalidState, Result::ModuleType_SRV, Result::Description_NotInitialized);
        if (8 < r2)
            return Result(Result::Level_Permanent, Result::Summary_WrongArgument, Result::ModuleType_SRV, 5);

        return detail::Service::GetServiceHandle(out, service, r2, r3);
    }
    #endif

} // namespace srv
} // namespace nn
```


