

# File alHashUtil.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Math**](dir_a966ac3a74b4b7a5925df4209ce9b3f1.md) **>** [**alHashUtil.cpp**](al_hash_util_8cpp.md)

[Go to the documentation of this file](al_hash_util_8cpp.md)


```C++
#include <Math/alHashUtil.h>

namespace al
{

u32 calcHashCode( const char* str )
{
        u32  result  = 0;
        char curChar = *str;

        while ( ( curChar = *str ) )
        {
                result = result * 31 + curChar;
                str++;
        }

        return result;
}

} // namespace al
```


