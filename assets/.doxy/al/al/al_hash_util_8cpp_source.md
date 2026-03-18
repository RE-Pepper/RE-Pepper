

# File alHashUtil.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Math**](dir_17d2d8808d20549c6aef9df204bad76e.md) **>** [**alHashUtil.cpp**](al_hash_util_8cpp.md)

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


